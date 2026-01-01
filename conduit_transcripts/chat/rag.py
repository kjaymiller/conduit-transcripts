"""Chat generation logic."""

import logging
from typing import AsyncGenerator, List

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from conduit_transcripts.config import settings
from conduit_transcripts.search import actions

logger = logging.getLogger(__name__)


async def generate_episode_response(
    query: str, episode_number: int
) -> AsyncGenerator[str, None]:
    """Generate a response to a query based on a specific episode's content."""
    try:
        # 1. Retrieve relevant chunks
        results = actions.vector_search(query, limit=5, episode_number=episode_number)

        if not results:
            yield "I couldn't find any relevant information in this episode to answer your question."
            return

        # 2. Construct context
        context_parts = []
        for r in results:
            context_parts.append(f"... {r.content_snippet} ...")

        context = "\n\n".join(context_parts)

        # 3. Setup LLM and Prompt
        llm = ChatOllama(
            model=settings.LLM_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
        )

        prompt = ChatPromptTemplate.from_template(
            """You are a helpful assistant discussing a specific podcast episode.
            Use the following context from the episode transcript to answer the user's question.
            If the answer is not in the context, say you don't know based on this episode.
            Keep your answer concise and conversational.
            
            Context:
            {context}
            
            User Question: {question}
            """
        )

        chain = prompt | llm | StrOutputParser()

        # 4. Stream response
        async for chunk in chain.astream({"context": context, "question": query}):
            yield chunk

    except Exception as e:
        logger.error(f"Error generating response: {e}")
        yield f"Sorry, I encountered an error: {str(e)}"
