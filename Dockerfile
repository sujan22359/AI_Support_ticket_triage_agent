FROM python:3.12-alpine

WORKDIR /app

# Install system dependencies for building Python packages
RUN apk update && \
    apk add --no-cache \
        build-base \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
