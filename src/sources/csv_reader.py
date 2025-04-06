import csv
from datetime import datetime
from dto import EventDTO

def read_events_from_csv(file_path: str):
    events = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            event = EventDTO(
                title=row['title'],
                description=row.get('description', ''),
                date=datetime.strptime(row['date'], '%Y-%m-%d').date()
            )
            events.append(event)
    return events
