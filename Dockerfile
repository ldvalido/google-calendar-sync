# Use slim Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2

# Install system dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl gcc libffi-dev libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set PATH
ENV PATH="/root/.local/bin:$PATH"

# Create app directory
WORKDIR /app

# Copy only necessary files
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --only main

# Copy project files
COPY . .

# Default command (can be overridden)
ENTRYPOINT ["poetry", "run", "python", "main.py"]
