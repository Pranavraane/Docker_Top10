FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jinja2==3.0.3


COPY . .

# Running as root user (default) - violating security context best practices
# No user restrictions or dropping of capabilities

EXPOSE 5000    # No network or port restriction

CMD ["python", "app.py"]

