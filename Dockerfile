FROM python:3.11-slim   
# Older image, never "apt update" or patch

WORKDIR /app

# Install outdated and unpinned dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jinja2==3.0.3    
# (Known vulnerabilities in old Jinja2)

# (Do NOT update system packages, intentionally use old image versions)
# (Optional) Intentionally install an old, vulnerable OS package
RUN apt-get update && apt-get install -y curl=7.72.0-1.1

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
