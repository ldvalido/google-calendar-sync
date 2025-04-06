from dataclasses import dataclass
from datetime import date

@dataclass
class EventDTO:
    title: str
    description: str
    date: date
