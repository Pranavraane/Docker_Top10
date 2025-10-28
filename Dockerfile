FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY app.py /app/app.py

RUN pip3 install flask

EXPOSE 5000

CMD ["python3", "app.py"]
