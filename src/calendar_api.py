import os
import datetime
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Set up Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_PATH = os.path.join('credentials', 'credentials.json')
TOKEN_PATH = os.path.join('credentials', 'token.json')


def get_calendar_service():
    """Get authenticated Google Calendar service."""
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_info(
            json.load(open(TOKEN_PATH)))

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)


def get_upcoming_events(days=7):
    """Get upcoming calendar events."""
    service = get_calendar_service()

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    end_time = (datetime.datetime.utcnow() +
                datetime.timedelta(days=days)).isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary',
                                          timeMin=now,
                                          timeMax=end_time,
                                          singleEvents=True,
                                          orderBy='startTime').execute()

    return events_result.get('items', [])


def update_event_title(event_id, new_title):
    """Update the title of a calendar event."""
    service = get_calendar_service()

    # Get the event
    event = service.events().get(calendarId='primary',
                                 eventId=event_id).execute()

    # Update the title
    event['summary'] = new_title

    # Update the event
    updated_event = service.events().update(calendarId='primary',
                                            eventId=event_id,
                                            body=event).execute()

    return updated_event
