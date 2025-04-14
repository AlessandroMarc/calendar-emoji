"""Main module for adding emojis to calendar events."""

import os
import logging
import datetime
from calendar_api import get_upcoming_events, update_event_title
from emoji_detector import starts_with_emoji
from open_ai import get_emoji_suggestion
from cache import EmojiCache

# Set up logging
log_file = os.path.join(
    'logs',
    f'calendar_emoji_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_file),
              logging.StreamHandler()])
logger = logging.getLogger(__name__)


def add_emojis_to_calendar_events(days=7):
    """Add emojis to calendar events that don't already have them."""
    logger.info(
        f"Starting emoji addition process for events in the next {days} days")

    try:
        # Initialize cache
        emoji_cache = EmojiCache()

        events = get_upcoming_events(days)
        logger.info(f"Found {len(events)} upcoming events")

        processed_count = 0
        cache_hit_count = 0
        api_call_count = 0

        for event in events:
            event_id = event['id']
            title = event.get('summary', '')

            # Skip if title is empty
            if not title:
                logger.warning(
                    f"Skipping event with empty title (ID: {event_id})")
                continue

            # Skip if title already starts with an emoji
            if starts_with_emoji(title):
                logger.info(f"Skipping (already has emoji): {title}")
                continue

            try:
                # Check cache before API call
                cached_emoji = emoji_cache.get(title)
                if cached_emoji:
                    emoji = cached_emoji
                    cache_hit_count += 1
                else:
                    # Get emoji suggestion from API
                    logger.info(f"Getting emoji suggestion for: {title}")
                    emoji = get_emoji_suggestion(title, emoji_cache)
                    api_call_count += 1

                if emoji:
                    # Update event title with emoji
                    new_title = f"{emoji} {title}"
                    logger.info(f"Updating: {title} → {new_title}")

                    update_event_title(event_id, new_title)
                    processed_count += 1
                else:
                    logger.warning(
                        f"No emoji suggestion received for: {title}")

            except Exception as e:
                logger.error(f"Error processing event '{title}': {str(e)}")

        logger.info(f"Processing complete. Updated {processed_count} events.")
        logger.info(
            f"Cache statistics: {cache_hit_count} hits, {api_call_count} API calls"
        )
        return processed_count

    except Exception as e:
        logger.error(f"Error in main process: {str(e)}")
        raise


if __name__ == '__main__':
    try:
        add_emojis_to_calendar_events()
    except Exception as e:
        logger.critical(f"Application failed: {str(e)}")
