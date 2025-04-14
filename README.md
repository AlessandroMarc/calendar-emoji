# Calendar Emoji

Automatically add relevant emojis to Google Calendar events using AI.

## Features

-   Scans upcoming Google Calendar events
-   Uses OpenAI to suggest relevant emojis based on event titles
-   Adds emojis to event titles that don't already have them
-   Logs all operations for tracking

## Setup

### Prerequisites

-   Python 3.7+
-   Google Cloud Platform account with Calendar API enabled
-   OpenAI API key

### Installation

1. Clone the repository
   git clone <https://github.com/yourusername/calendar-emoji.git>
   cd calendar-emoji

2. Set up virtual environment
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Set up credentials

-   Place your Google API credentials file in `credentials/credentials.json`
-   Create a `.env` file with your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Usage

Run the script:

python -m src.main

For scheduled execution, set up a cron job (Linux/macOS) or Task Scheduler (Windows).

## License

MIT
