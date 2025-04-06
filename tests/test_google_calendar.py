from targets.google_calendar import push_events_to_google_calendar
from dto import EventDTO
from datetime import datetime
import pytest
from unittest.mock import patch

@pytest.mark.skip(reason="Requires manual credentials setup")
@patch("targets.google_calendar.build")
def test_push_events_to_google_calendar(mock_build):
    mock_service = mock_build.return_value
    mock_service.events.return_value.insert.return_value.execute.return_value = {}

    event = EventDTO("Test Event", "Desc", datetime(2025, 4, 5, 14), datetime(2025, 4, 5, 15))
    push_events_to_google_calendar([event], "Test Calendar")

    assert mock_service.events.return_value.insert.called
