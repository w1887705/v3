# Render Docker deployment for Django
# Uses Python 3.12 (stable)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Basic build deps for wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first (better layer caching)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Copy project
COPY . /app

# Collect static at build time (will use WhiteNoise in production)
# If env vars (like SECRET_KEY) are required for collectstatic, Render can
# set them and you can disable this step; for this project it should work.
RUN python manage.py collectstatic --noinput || true

# Render sets PORT; default to 8000 locally
ENV PORT=8000

# Start server
CMD ["bash", "start.sh"]
