from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
import pickle
from dto import EventDTO

SCOPES = ['https://www.googleapis.com/auth/calendar']
TIMEZONE = 'America/Argentina/Buenos_Aires'

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def find_or_create_calendar(service, name):
    calendars = service.calendarList().list().execute().get('items', [])
    for cal in calendars:
        if cal['summary'] == name:
            return cal['id']
    calendar = {'summary': name, 'timeZone': TIMEZONE}
    created = service.calendars().insert(body=calendar).execute()
    return created['id']

def push_events_to_google_calendar(events: list[EventDTO], calendar_name: str):
    service = authenticate_google_calendar()
    calendar_id = find_or_create_calendar(service, calendar_name)
    
    for event in events:
        event_body = {
            'summary': event.title,
            'description': event.description,
            'start': {'date': event.date.isoformat(), 'timeZone': TIMEZONE},
            'end': {'date': event.date.isoformat(), 'timeZone': TIMEZONE},
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 24 * 60}
                ]
            }
        }
        created = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        print(f"✅ Created: {created.get('summary')} on {event.date}")
