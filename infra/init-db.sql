-- Initialize PostgreSQL database with pgvector extension
-- This script runs automatically when the database is first created

-- Enable pgvector extension for vector operations
CREATE EXTENSION IF NOT EXISTS vector;

-- Create transcripts table
-- Stores episode metadata and full transcript content
CREATE TABLE IF NOT EXISTS transcripts (
    podcast TEXT NOT NULL,
    episode_number INTEGER NOT NULL,
    title TEXT,
    description TEXT,
    url TEXT,
    pub_date TIMESTAMP,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (podcast, episode_number)
);

-- Create vector_chunks table
-- Stores chunked transcript text with embeddings for semantic search
CREATE TABLE IF NOT EXISTS vector_chunks (
    id SERIAL PRIMARY KEY,
    podcast TEXT NOT NULL,
    episode_number INTEGER NOT NULL,
    chunk_text TEXT NOT NULL,
    embedding vector(768),  -- 768-dimensional embeddings from all-mpnet-base-v2
    chunk_index INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (podcast, episode_number) REFERENCES transcripts(podcast, episode_number) ON DELETE CASCADE
);

-- Create index on embeddings for fast vector similarity search
CREATE INDEX IF NOT EXISTS vector_chunks_embedding_idx
ON vector_chunks USING ivfflat (embedding vector_l2_ops)
WITH (lists = 100);

-- Create index on episode lookup
CREATE INDEX IF NOT EXISTS vector_chunks_episode_idx
ON vector_chunks(podcast, episode_number);

-- Create updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger for transcripts table
DROP TRIGGER IF EXISTS update_transcripts_updated_at ON transcripts;
CREATE TRIGGER update_transcripts_updated_at
    BEFORE UPDATE ON transcripts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Grant necessary permissions (adjust as needed for your setup)
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO postgres;
