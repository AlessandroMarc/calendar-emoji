"""Module for interacting with the OpenAI API."""

import os
import requests
import logging
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)


def get_emoji_suggestion(event_title: str, emoji_cache=None) -> str:
    """Get emoji suggestion from cache or OpenAI API.

    Args:
        event_title: Title of the calendar event
        emoji_cache: Optional cache instance to check before calling API

    Returns:
        Suggested emoji
    """
    # Check cache first if provided
    if emoji_cache:
        cached_emoji = emoji_cache.get(event_title)
        if cached_emoji:
            return cached_emoji

    # If not in cache or no cache provided, call OpenAI API
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        raise ValueError(
            "OpenAI API key not found. Please set it in the .env file.")

    logger.info(f"Calling OpenAI API for emoji suggestion: '{event_title}'")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model":
        "gpt-4o-mini",
        "messages": [{
            "role":
            "system",
            "content":
            "You are a helpful assistant that suggests a single appropriate emoji for calendar events. Respond with only the emoji, nothing else."
        }, {
            "role":
            "user",
            "content":
            f"Suggest one emoji for this calendar event: '{event_title}'"
        }],
        "max_tokens":
        10
    }

    response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers=headers,
                             json=data)

    if response.status_code == 200:
        emoji = response.json()["choices"][0]["message"]["content"].strip()

        # Store in cache if provided
        if emoji_cache:
            emoji_cache.set(event_title, emoji)

        return emoji
    else:
        error_msg = f"Error: {response.status_code}, {response.text}"
        logger.error(error_msg)
        raise Exception(error_msg)
