# Streamlit App Update: Support Timestamp-Enabled OpenSearch Index

## Context

A new timestamp-enabled OpenSearch index has been created alongside the existing index. This new index includes timestamp information for each chunk, allowing the RAG system to generate timestamped YouTube URLs that open episodes at the exact moment where relevant snippets occur.

## Index Structure

The timestamp-enabled index has all the same fields as the standard index, plus these additional fields:

- **`youtube_url`** (keyword): Full YouTube URL (e.g., `https://www.youtube.com/watch?v=BVM6TUSfn3E`)
- **`youtube_video_id`** (keyword): Just the video ID (e.g., `BVM6TUSfn3E`)
- **`timestamp`** (integer): Chunk start time in seconds (e.g., 1296 for 21:36)
- **`chunk_index`** (integer): Position of chunk within the episode

## Environment Variables

The timestamp-enabled index name is determined by:
- `INDEX_NAME_WITH_TIMESTAMPS` environment variable (if set)
- Otherwise defaults to `{INDEX_NAME}_timestamps` (e.g., if `INDEX_NAME=transcripts`, then `transcripts_timestamps`)

## Required Changes

### 1. Update Index Name Configuration

Add support for selecting which index to use (standard or timestamp-enabled). You can either:
- Add a configuration option/environment variable to choose the index
- Or add a toggle in the Streamlit UI to switch between indices

### 2. Update Search Query to Include Timestamp Fields

When querying the timestamp-enabled index, ensure your search results include the new fields:

```python
# Example: Include timestamp fields in the _source
search_body = {
    "query": {...},
    "_source": ["title", "url", "content", "youtube_url", "youtube_video_id", "timestamp", "chunk_index", ...]
}
```

### 3. Construct Timestamped YouTube URLs

When displaying episode URLs in search results, check if `timestamp` and `youtube_video_id` are available. If they are, construct a timestamped URL:

**URL Format:**
- Base YouTube URL: `https://www.youtube.com/watch?v={video_id}`
- Timestamped URL: `https://youtu.be/{video_id}?t={timestamp}`

**Example:**
- Video ID: `BVM6TUSfn3E`
- Timestamp: `1296` (seconds)
- Result: `https://youtu.be/BVM6TUSfn3E?t=1296`

**Implementation:**
```python
def build_episode_url(hit):
    """Build episode URL with timestamp if available"""
    url = hit.get('_source', {}).get('url', '')
    youtube_video_id = hit.get('_source', {}).get('youtube_video_id')
    timestamp = hit.get('_source', {}).get('timestamp')
    
    # If we have YouTube video ID and timestamp, use timestamped URL
    if youtube_video_id and timestamp is not None:
        return f"https://youtu.be/{youtube_video_id}?t={timestamp}"
    
    # Otherwise, fall back to original URL
    return url
```

### 4. Handle Missing Timestamps Gracefully

Some chunks may not have timestamps (e.g., old transcripts without Whisper segments). Always check if `timestamp` is not None before constructing timestamped URLs:

```python
if timestamp is not None:
    # Use timestamped URL
else:
    # Use regular episode URL
```

### 5. Display Timestamps in UI (Optional Enhancement)

Consider displaying the timestamp in a human-readable format alongside the URL:

```python
def format_timestamp(seconds):
    """Convert seconds to MM:SS or HH:MM:SS format"""
    if seconds is None:
        return None
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"

# In your UI:
if timestamp:
    st.write(f"⏱️ {format_timestamp(timestamp)}")
```

## Example Search Result Structure

When querying the timestamp-enabled index, search results will have this structure:

```python
{
    "_source": {
        "title": "Episode Title",
        "url": "https://rss.com/podcasts/vector-podcast/599924",
        "content": "Chunk text content...",
        "youtube_url": "https://www.youtube.com/watch?v=BVM6TUSfn3E",  # May be None
        "youtube_video_id": "BVM6TUSfn3E",  # May be None
        "timestamp": 1296,  # Integer seconds, may be None
        "chunk_index": 5,
        # ... other existing fields
    }
}
```

## Testing Checklist

- [ ] Update index name to use timestamp-enabled index
- [ ] Verify search queries return timestamp fields
- [ ] Test URL construction with timestamps
- [ ] Test fallback to regular URL when timestamp is None
- [ ] Test with episodes that have YouTube URLs
- [ ] Test with episodes that don't have YouTube URLs
- [ ] Verify timestamped URLs open YouTube at correct time

## Notes

- The timestamp-enabled index can coexist with the standard index
- Both indices can be queried independently
- The standard index remains unchanged and continues to work as before
- Episodes without Whisper segments will have `timestamp: None`
- Episodes without YouTube URLs in description will have `youtube_url: None` and `youtube_video_id: None`

