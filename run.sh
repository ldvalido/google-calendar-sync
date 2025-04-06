#!/bin/bash
docker run --rm -it \
  -v $(pwd)/credentials.json:/app/credentials.json \
  -v $(pwd)/eventos.csv:/app/eventos.csv \
  calendar-tool \
  --source eventos.csv --format csv --output google
