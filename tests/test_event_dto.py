from dto import EventDTO
from datetime import datetime

def test_event_dto_creation():
    event = EventDTO("Test Event", "Test Desc", datetime(2025, 4, 5, 14))
    assert event.title == "Test Event"
    assert event.description == "Test Desc"
    assert event.date == datetime(2025, 4, 5, 14)
