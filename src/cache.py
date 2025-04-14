"""Cache module for storing and retrieving emoji suggestions."""

import os
import json
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class EmojiCache:
    """Cache for storing emoji suggestions for event titles."""

    def __init__(self, cache_file: str = "credentials/emoji_cache.json"):
        """Initialize the cache.

        Args:
            cache_file: Path to the cache file
        """
        self.cache_file = cache_file
        self.cache: Dict[str, str] = {}
        self.load_cache()

    def load_cache(self) -> None:
        """Load the cache from file."""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    self.cache = json.load(f)
                logger.info(
                    f"Loaded {len(self.cache)} emoji mappings from cache")
            else:
                logger.info("No cache file found, starting with empty cache")
                self.cache = {}
        except Exception as e:
            logger.error(f"Error loading cache: {str(e)}")
            self.cache = {}

    def save_cache(self) -> None:
        """Save the cache to file."""
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)

            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved {len(self.cache)} emoji mappings to cache")
        except Exception as e:
            logger.error(f"Error saving cache: {str(e)}")

    def get(self, title: str) -> Optional[str]:
        """Get emoji for a title from cache.

        Args:
            title: Event title to look up

        Returns:
            Emoji if found, None otherwise
        """
        # Normalize the title for better matching (lowercase, strip extra spaces)
        normalized_title = ' '.join(title.lower().split())

        # Try exact match first
        if normalized_title in self.cache:
            logger.info(f"Cache hit (exact): '{title}'")
            return self.cache[normalized_title]

        # Try keyword matching for partial matches
        for cached_title, emoji in self.cache.items():
            # Split into words and check if all words in cached_title appear in normalized_title
            cached_words = cached_title.split()
            if len(
                    cached_words
            ) > 1:  # Only consider multi-word titles for partial matching
                if all(word in normalized_title for word in cached_words):
                    logger.info(
                        f"Cache hit (partial): '{title}' matched with '{cached_title}'"
                    )
                    return emoji

        logger.info(f"Cache miss: '{title}'")
        return None

    def set(self, title: str, emoji: str) -> None:
        """Store emoji for a title in cache.

        Args:
            title: Event title
            emoji: Emoji to associate with the title
        """
        # Normalize the title
        normalized_title = ' '.join(title.lower().split())

        # Store in cache
        self.cache[normalized_title] = emoji
        logger.info(f"Added to cache: '{normalized_title}' → '{emoji}'")

        # Save cache to file
        self.save_cache()
