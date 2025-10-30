FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

RUN mkdir /var/log/myapp
RUN chmod 777 /var/log/myapp

CMD ["python", "app.py"]
