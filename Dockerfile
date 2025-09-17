FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR /app/flavorfeed
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "flavorfeed.wsgi:application"]