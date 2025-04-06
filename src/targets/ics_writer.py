from dto import EventDTO
from ics import Calendar, Event

def export_events_to_ics(events: list[EventDTO], file_path: str):
    calendar = Calendar()
    for e in events:
        ics_event = Event()
        ics_event.name = e.title
        ics_event.description = e.description
        ics_event.begin = e.date
        ics_event.make_all_day()
        calendar.events.add(ics_event)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(calendar.serialize_iter())
    print(f"📁 ICS file saved at: {file_path}")
