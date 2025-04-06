# Calendar Tool

This tool imports financial events from CSV or JSON files and exports them to a Google Calendar or an ICS file.

## Requirements

- Python 3.7+
- Google API credentials (`credentials.json`)

## Setup with Poetry

Install dependencies using Poetry:

```bash
poetry install
```

## Usage

Run the script from the terminal using the command-line interface (CLI):

```bash
python main.py --source <file_path> --format <csv|json> --output <google|ics>
```

### Options

- `--source`: Path to the CSV or JSON file with event data.
- `--format`: Input format. Accepted values: `csv`, `json`.
- `--output`: Output type. Accepted values: `google` (Google Calendar), `ics` (ICS file).
- `--calendar`: (Optional) Google Calendar name. Default is "Calendario Bursátil".
- `--ics_path`: (Optional) Path to save the ICS file. Default is `events.ics`.

### Examples

Export to Google Calendar:
```bash
python src/main.py --source eventos.json --format json --output google
```

Export to ICS file:
```bash
python src/main.py --source eventos.csv --format csv --output ics --ics_path my_events.ics
```

## Authentication

Make sure you have your `credentials.json` in the root folder. The first time you run the script, a browser will open to authenticate with Google.

🐳 Running with Docker
Build the Docker image

docker build -t calendar-tool .

Run the CLI with Docker

docker run --rm -it \
  -v $(pwd)/credentials.json:/app/credentials.json \
  -v $(pwd)/eventos.csv:/app/eventos.csv \
  calendar-tool \
  --source eventos.csv --format csv --output google


📦 Running with Docker Compose

docker-compose run calendar-tool --source eventos.csv --format csv --output google

🖱️ Shortcut with Bash

Create a file run.sh:

#!/bin/bash
docker run --rm -it \\
  -v $(pwd)/credentials.json:/app/credentials.json \\
  -v $(pwd)/eventos.csv:/app/eventos.csv \\
  calendar-tool \\
  --source eventos.csv --format csv --output google

Make it executable:

chmod +x run.sh
./run.sh


## License

MIT
