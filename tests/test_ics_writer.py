from targets.ics_writer import export_events_to_ics
from dto import EventDTO
from datetime import datetime

def test_export_events_to_ics(tmp_path):
    event = EventDTO("Test Event", "Desc", datetime(2025, 4, 5, 14))
    ics_path = tmp_path / "test.ics"
    export_events_to_ics([event], str(ics_path))

    assert ics_path.exists()
    content = ics_path.read_text()
    assert "BEGIN:VEVENT" in content
    assert "SUMMARY:Test Event" in content
