FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies (as root)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jinja2==3.0.3

# Copy the rest of your app's code (as root)
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app with host=0.0.0.0 to be accessible outside the container (as root)
CMD ["python", "app.py"]
