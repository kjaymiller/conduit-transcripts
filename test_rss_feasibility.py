#!/usr/bin/env python3
"""
Test script to verify RSS feed parsing and audio download feasibility.
This script tests the core functionality without requiring full transcription.
"""

import sys
import pathlib

# Add src to path
sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))

try:
    from rss_parser import parse_rss_feed, get_latest_episode
    from transcribe import download_audio_file
    print("✅ All imports successful")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required dependencies:")
    print("  pip install httpx typer")
    sys.exit(1)

def test_rss_parsing():
    """Test RSS feed parsing"""
    print("\n📡 Testing RSS feed parsing...")
    rss_url = "https://media.rss.com/vector-podcast/feed.xml"
    
    try:
        episodes = parse_rss_feed(rss_url)
        print(f"✅ Successfully parsed RSS feed")
        print(f"   Found {len(episodes)} episodes")
        
        if episodes:
            latest = episodes[0]
            print(f"\n📝 Latest episode:")
            print(f"   Title: {latest.get('title', 'N/A')}")
            print(f"   Audio URL: {latest.get('audio_url', 'N/A')[:80]}...")
            print(f"   Episode #: {latest.get('episode_number', 'N/A')}")
            return latest.get('audio_url')
        else:
            print("⚠️  No episodes found in feed")
            return None
    except Exception as e:
        print(f"❌ Error parsing RSS feed: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_audio_download(audio_url):
    """Test audio file download"""
    if not audio_url:
        print("\n⏭️  Skipping audio download test (no URL)")
        return False
    
    print(f"\n⬇️  Testing audio download...")
    print(f"   URL: {audio_url[:80]}...")
    
    try:
        # Just test the download, not full transcription
        import tempfile
        import httpx
        
        with tempfile.NamedTemporaryFile(mode="+wb", suffix=".mp3", delete=True) as f:
            print(f"   Downloading to temporary file...")
            with httpx.stream("GET", audio_url, follow_redirects=True, timeout=30.0) as response:
                response.raise_for_status()
                size = 0
                for chunk in response.iter_bytes():
                    f.write(chunk)
                    size += len(chunk)
                    if size > 1024 * 1024:  # Stop after 1MB for testing
                        break
                print(f"✅ Successfully downloaded {size / 1024:.1f} KB (test)")
                return True
    except Exception as e:
        print(f"❌ Error downloading audio: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("Vector Podcast RSS Feed Transcription - Feasibility Test")
    print("=" * 60)
    
    audio_url = test_rss_parsing()
    download_success = test_audio_download(audio_url)
    
    print("\n" + "=" * 60)
    print("FEASIBILITY ASSESSMENT:")
    print("=" * 60)
    
    if audio_url and download_success:
        print("✅ FEASIBLE - All core components work!")
        print("\nNext steps:")
        print("  1. Install Whisper: pip install openai-whisper")
        print("  2. Run transcription:")
        print("     python src/transcribe.py rss --latest")
        print("     python src/transcribe.py rss --url <RSS_URL> 1 2 3")
        print("     python src/transcribe.py rss --all")
    else:
        print("⚠️  Some issues detected. Check errors above.")
    print("=" * 60)

if __name__ == "__main__":
    main()


