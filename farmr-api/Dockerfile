## base image
FROM python:3.7.5-slim-buster

## install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean


RUN pip install -U pip

RUN mkdir -p /app
WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt

RUN addgroup -g 1001 farmr && adduser -G farmr -h /app -u 1001 -D farmr

USER farmr