FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt flask

COPY app.py .

ENV SECRET_KEY="SuperSecretPassword123"

EXPOSE 5000

CMD ["python", "app.py"]
