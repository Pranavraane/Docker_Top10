FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000   # Exposing all application services to default Docker network (potentially all containers)
CMD ["python", "app.py"]
