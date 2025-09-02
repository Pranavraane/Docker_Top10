text
FROM python:3.11-slim   # Using the base image without updating OS packages
WORKDIR /app
# Using possibly outdated dependencies, without updating system packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
