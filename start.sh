#!/bin/bash

gunicorn 'app.main:app' \
    --bind ${ADDRESS:-0.0.0.0}:${PORT:-8000} \
    --workers ${WORKERS:-1} \
    --worker-class uvicorn.workers.UvicornWorker \
    --log-level info \
    --access-logfile="-"