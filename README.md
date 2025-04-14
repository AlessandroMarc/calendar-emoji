# 📅 Calendar Emoji

Automatically add AI-generated emojis to your Google Calendar events, making your schedule more visually appealing and easier to scan.

## ✨ Features

- 🔍 **Smart Scanning**: Automatically scans your upcoming Google Calendar events
- 🤖 **AI-Powered**: Uses OpenAI's GPT models to suggest contextually relevant emojis
- 💾 **Efficient Caching**: Remembers previous suggestions to minimize API calls
- 🚫 **Duplicate Prevention**: Intelligently skips events that already have emojis
- 📊 **Detailed Logging**: Tracks all operations for monitoring and debugging

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Cloud Platform account with Calendar API enabled
- OpenAI API key

### Installation

1. Clone the repository

```bash
git clone https://github.com/AlessandroMarc/calendar-emoji.git
cd calendar-emoji
```

2. Set up virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure credentials

- Create a project in Google Cloud Console
- Enable the Google Calendar API
- Create OAuth credentials (Desktop application)
- Download the credentials JSON file to `credentials/credentials.json`
- Create a `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 🔧 Usage

### Running Manually

```bash
# Run the script
python -m src.main

# Specify number of days to look ahead (default: 7)
python -m src.main --days 14
```

### Scheduling Automatic Runs

#### On macOS/Linux (Cron)

```bash
# Edit crontab
crontab -e

# Add this line to run daily at 1 AM
0 1 * * * cd /path/to/calendar-emoji && /path/to/venv/bin/python -m src.main >> /path/to/calendar-emoji/logs/cron.log 2>&1
```

#### On Windows (Task Scheduler)

1. Open Task Scheduler
2. Create a new Basic Task
3. Set the trigger (e.g., daily at 1 AM)
4. Set the action:
    - Program/script: `C:\path\to\venv\Scripts\python.exe`
    - Arguments: `-m src.main`
    - Start in: `C:\path\to\calendar-emoji`

## 📋 How It Works

1. **Authentication**: Securely connects to your Google Calendar
2. **Event Scanning**: Retrieves upcoming events from your calendar
3. **Emoji Detection**: Checks if events already have emojis
4. **Cache Lookup**: Checks if similar events have received emojis before
5. **AI Suggestion**: For new events, asks OpenAI for appropriate emojis
6. **Calendar Update**: Adds the suggested emoji to the event title

### Examples

| Before             | After                 |
| ------------------ | --------------------- |
| Team Meeting       | 👥 Team Meeting       |
| Doctor Appointment | 🩺 Doctor Appointment |
| Gym Workout        | 💪 Gym Workout        |
| Birthday Party     | 🎂 Birthday Party     |
| Flight to Paris    | ✈️ Flight to Paris    |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Alessandro Marchesin
