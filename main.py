import pandas as pd
import os.path
import datetime
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

# === CONFIGURACIÓN ===
CSV_FILE = 'eventos.csv'
CALENDARIO_NOMBRE = 'Calendario Bursátil'
TIMEZONE = 'America/Argentina/Buenos_Aires'
SCOPES = ['https://www.googleapis.com/auth/calendar']

# === AUTENTICACIÓN CON OAUTH ===
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('calendar', 'v3', credentials=creds)

# === BUSCAR O CREAR CALENDARIO ===
def obtener_o_crear_calendario(nombre):
    page_token = None
    while True:
        calendarios = service.calendarList().list(pageToken=page_token).execute()
        for cal in calendarios.get('items', []):
            if cal['summary'] == nombre:
                return cal['id']
        page_token = calendarios.get('nextPageToken')
        if not page_token:
            break
    nuevo = {
        'summary': nombre,
        'timeZone': TIMEZONE
    }
    calendario_creado = service.calendars().insert(body=nuevo).execute()
    return calendario_creado['id']

calendar_id = obtener_o_crear_calendario(CALENDARIO_NOMBRE)

# === LEER CSV Y CREAR EVENTOS ===
df = pd.read_csv(CSV_FILE)

for _, row in df.iterrows():
    titulo = row['titulo']
    descripcion = row.get('descripcion', '')
    fecha = row['fecha']  # formato YYYY-MM-DD

    evento = {
        'summary': titulo,
        'description': descripcion,
        'start': {'date': fecha, 'timeZone': TIMEZONE},
        'end': {'date': fecha, 'timeZone': TIMEZONE},
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},  # correo 24 hs antes
                {'method': 'popup', 'minutes': 24 * 60},
            ],
        },
    }

    creado = service.events().insert(calendarId=calendar_id, body=evento).execute()
    print(f"✅ Evento creado: {creado.get('summary')} ({fecha})")

