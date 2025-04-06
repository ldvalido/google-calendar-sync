from sources.csv_reader import read_events_from_csv
from dto import EventDTO
import tempfile

def test_read_events_from_csv():
    csv_data = "title,description,date\nTest,Desc,2025-04-05"
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".csv") as f:
        f.write(csv_data)
        f.seek(0)
        events = read_events_from_csv(f.name)

    assert len(events) == 1
    assert isinstance(events[0], EventDTO)
    assert events[0].title == "Test"
