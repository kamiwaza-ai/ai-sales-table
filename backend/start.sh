#!/bin/bash

# Add the current directory to Python path
cd /app
export PYTHONPATH=/app:$PYTHONPATH

# Start uvicorn
python -m uvicorn main:app --host 0.0.0.0 --port 8080
