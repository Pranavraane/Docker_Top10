FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Running as root user (default) - insecure practice
# No creation or use of a non-root user
# Exposing port without consideration of minimal exposure
EXPOSE 5000    # Exposing all application services to default Docker network (potentially all containers)
# No healthcheck added - no runtime health monitoring
CMD ["python", "app.py"]

