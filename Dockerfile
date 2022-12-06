FROM python:3.11.0-slim-buster

ADD ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app