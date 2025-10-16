FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jinja2==3.0.3 flask

COPY . .

# Runs as root - insecure (violates D05)
# No user restrictions, no dropped Linux capabilities
EXPOSE 5000

CMD ["python", "app.py"]
