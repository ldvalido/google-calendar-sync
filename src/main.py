import argparse
from sources.csv_reader import read_events_from_csv
from sources.json_reader import read_events_from_json
from targets.google_calendar import push_events_to_google_calendar
from targets.ics_writer import export_events_to_ics

def main():
    parser = argparse.ArgumentParser(description="Import financial events and export to calendar.")
    parser.add_argument('--source', required=True, help="Path to the data file (CSV or JSON).")
    parser.add_argument('--format', required=True, choices=['csv', 'json'], help="Data file format.")
    parser.add_argument('--output', required=True, choices=['google', 'ics'], help="Output type.")
    parser.add_argument('--calendar', default='Calendario Bursátil', help="Google Calendar name (if output is google).")
    parser.add_argument('--ics_path', default='events.ics', help="ICS file path (if output is ics).")

    args = parser.parse_args()

    # Load data
    if args.format == 'csv':
        events = read_events_from_csv(args.source)
    elif args.format == 'json':
        events = read_events_from_json(args.source)
    else:
        raise ValueError("Unsupported format")

    # Export
    if args.output == 'google':
        push_events_to_google_calendar(events, args.calendar)
    elif args.output == 'ics':
        export_events_to_ics(events, args.ics_path)

if __name__ == '__main__':
    main()
