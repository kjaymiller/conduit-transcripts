"""Parse RSS feed to extract episode information and audio URLs."""

import xml.etree.ElementTree as ET
from typing import List, Dict, Optional
import httpx
import typer


def parse_rss_feed(rss_url: str) -> List[Dict[str, str]]:
    """
    Parse an RSS feed and extract episode information.
    
    Args:
        rss_url: URL of the RSS feed
        
    Returns:
        List of dictionaries containing episode metadata and audio URLs
    """
    typer.echo(f"Fetching RSS feed from {rss_url}")
    response = httpx.get(rss_url)
    response.raise_for_status()
    
    root = ET.fromstring(response.text)
    
    # Define namespaces
    namespaces = {
        'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'podcast': 'https://podcastindex.org/namespace/1.0',
    }
    
    # Find all items in the feed
    items = root.findall('.//item')
    episodes = []
    
    for item in items:
        # Extract title (handle CDATA)
        title_elem = item.find('title')
        if title_elem is not None:
            title = title_elem.text if title_elem.text else ""
            # Clean up CDATA if present
            title = title.strip()
        else:
            title = "Unknown Title"
        
        # Extract description (handle CDATA)
        desc_elem = item.find('description')
        if desc_elem is not None:
            description = desc_elem.text if desc_elem.text else ""
            description = description.strip()
        else:
            description = ""
        
        # Extract publication date
        pub_date_elem = item.find('pubDate')
        pub_date = pub_date_elem.text if pub_date_elem is not None and pub_date_elem.text else ""
        
        # Extract link
        link_elem = item.find('link')
        link = link_elem.text if link_elem is not None and link_elem.text else ""
        
        # Extract audio URL from enclosure
        enclosure = item.find('enclosure')
        audio_url = None
        if enclosure is not None:
            audio_url = enclosure.get('url')
        
        # Extract episode number from itunes:episode if available
        episode_elem = item.find('.//itunes:episode', namespaces)
        episode_number = None
        if episode_elem is not None and episode_elem.text:
            try:
                episode_number = int(episode_elem.text)
            except (ValueError, AttributeError):
                pass
        
        # Extract image URL from itunes:image if available
        image_elem = item.find('.//itunes:image', namespaces)
        image_url = None
        if image_elem is not None:
            image_url = image_elem.get('href')
        
        if audio_url:
            episode_data = {
                'title': title,
                'description': description,
                'pub_date': pub_date,
                'url': link,
                'audio_url': audio_url,
                'episode_number': episode_number,
                'image_url': image_url,
            }
            episodes.append(episode_data)
    
    typer.echo(f"Found {len(episodes)} episodes in RSS feed")
    return episodes


def get_episode_by_number(rss_url: str, episode_number: int) -> Optional[Dict[str, str]]:
    """
    Get a specific episode by episode number from the RSS feed.
    
    Args:
        rss_url: URL of the RSS feed
        episode_number: Episode number to retrieve
        
    Returns:
        Episode dictionary or None if not found
    """
    episodes = parse_rss_feed(rss_url)
    for episode in episodes:
        if episode.get('episode_number') == episode_number:
            return episode
    return None


def get_latest_episode(rss_url: str) -> Optional[Dict[str, str]]:
    """
    Get the latest episode from the RSS feed (first item).
    
    Args:
        rss_url: URL of the RSS feed
        
    Returns:
        Latest episode dictionary or None if feed is empty
    """
    episodes = parse_rss_feed(rss_url)
    return episodes[0] if episodes else None


def get_audio_url_from_rss_episode(episode: Dict[str, str]) -> tuple[Dict[str, str], str]:
    """
    Extract metadata and audio URL from an episode dictionary.
    
    Args:
        episode: Episode dictionary from RSS feed
        
    Returns:
        Tuple of (metadata_dict, audio_url)
    """
    metadata = {
        'title': episode.get('title', 'Unknown'),
        'url': episode.get('url', ''),
        'description': episode.get('description', ''),
        'pub_date': episode.get('pub_date', ''),
        'image_url': episode.get('image_url', ''),
    }
    audio_url = episode.get('audio_url', '')
    return (metadata, audio_url)

