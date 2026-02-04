# Render Docker deployment for Django
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Basic build deps for wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt


COPY . /app


RUN python manage.py collectstatic --noinput || true

# Render sets PORT; default to 8000 locally
ENV PORT=8000

# Start server
CMD ["bash", "start.sh"]
