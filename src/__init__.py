"""Calendar Emoji - Add AI-generated emojis to Google Calendar events."""

__version__ = '0.1.0'
__author__ = 'Your Name'

# Import key functions to make them available at the package level
from src.calendar_api import get_calendar_service, get_upcoming_events, update_event_title
from src.emoji_detector import starts_with_emoji
from src.open_ai import get_emoji_suggestion
from src.cache import EmojiCache
from src.main import add_emojis_to_calendar_events

# Define what's available when using `from src import *`
__all__ = [
    'get_calendar_service',
    'get_upcoming_events',
    'update_event_title',
    'starts_with_emoji',
    'get_emoji_suggestion',
    'EmojiCache',
    'add_emojis_to_calendar_events',
]
