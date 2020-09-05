FROM python:3.8.5-buster

WORKDIR /usr/src/producer

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY consumer.py .