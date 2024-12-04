#!/bin/bash

set -euo pipefail

# Load environment variables
if [ -f ".env" ]; then
  source .env
fi

# Validate required environment variables
required_vars=("OPENAI_API_KEY")
for var in "${required_vars[@]}"; do
  if [ -z "${!var}" ]; then
    echo "Error: Environment variable '$var' is not set." >&2
    exit 1
  fi
done

# Set default port if not set
port="${PORT:-8000}"

# Start the application
echo "$(date +"%Y-%m-%d %H:%M:%S") Starting OpenAI API wrapper..."
exec uvicorn src.main:app --host 0.0.0.0 --port ${port}
```