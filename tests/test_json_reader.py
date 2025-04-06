from sources.json_reader import read_events_from_json
from dto import EventDTO
import tempfile
import json

def test_read_events_from_json():
    data = [{
        "title": "Test",
        "description": "Desc",
        "date": "2025-04-05"
    }]
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json") as f:
        json.dump(data, f)
        f.seek(0)
        events = read_events_from_json(f.name)

    assert len(events) == 1
    assert isinstance(events[0], EventDTO)
    assert events[0].title == "Test"
