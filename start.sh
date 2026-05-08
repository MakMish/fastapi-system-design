#!/bin/bash
celery -A src.tasks.celery_app worker --pool=solo --loglevel=info &
uvicorn src.main:app --host 0.0.0.0 --port $PORT