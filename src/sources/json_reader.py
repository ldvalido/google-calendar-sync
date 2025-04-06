import json
from datetime import datetime
from dto import EventDTO

def read_events_from_json(file_path: str):
    events = []
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            event = EventDTO(
                title=item['title'],
                description=item.get('description', ''),
                date=datetime.strptime(item['date'], '%Y-%m-%d').date()
            )
            events.append(event)
    return events
