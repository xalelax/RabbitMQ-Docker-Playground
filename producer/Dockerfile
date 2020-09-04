FROM python:3.8.5-buster

WORKDIR /usr/src/producer
ENV FLASK_APP producer.py

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .