FROM python:3.9-slim

WORKDIR /app

COPY app.py .

# Vulnerable: Container is not started read-only, and application can write to the filesystem
RUN mkdir data
VOLUME /app/data

CMD ["python", "app.py"]
