-- Initialize PostgreSQL database with pgvector extension
-- This script runs automatically when the database is first created

-- Enable pgvector extension for vector operations
CREATE EXTENSION IF NOT EXISTS vector;

-- Drop old tables if they exist (cleanup/simplification)
DROP TABLE IF EXISTS transcript_vector;
DROP TABLE IF EXISTS transcripts;

-- Create transcriptions table
CREATE TABLE IF NOT EXISTS transcriptions (
    podcast TEXT NOT NULL,
    episode_number INTEGER NOT NULL,
    meta JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (podcast, episode_number)
);

-- Create search table (formerly transcript_vector)
CREATE TABLE IF NOT EXISTS search (
    id SERIAL PRIMARY KEY,
    podcast TEXT NOT NULL,
    episode_number INTEGER NOT NULL,
    content TEXT,
    embedding vector(768),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (podcast, episode_number) REFERENCES transcriptions(podcast, episode_number) ON DELETE CASCADE,
    CONSTRAINT uq_search_id_podcast_episode UNIQUE (id, podcast, episode_number)
);

-- Create index on embeddings for fast vector similarity search
CREATE INDEX IF NOT EXISTS search_embedding_idx
ON search USING ivfflat (embedding vector_l2_ops)
WITH (lists = 100);

-- Create index on episode lookup
CREATE INDEX IF NOT EXISTS search_episode_idx
ON search(podcast, episode_number);

-- Create updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger for transcriptions table
DROP TRIGGER IF EXISTS update_transcriptions_updated_at ON transcriptions;
CREATE TRIGGER update_transcriptions_updated_at
    BEFORE UPDATE ON transcriptions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
