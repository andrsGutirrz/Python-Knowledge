#!/bin/bash

# Run the FastAPI application using Poetry and Uvicorn
poetry run uvicorn --host=0.0.0.0 --port=8080 app.api.main:app
