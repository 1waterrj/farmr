FROM python:3.7-alpine

RUN apk add --update \
    bash \
    gcc \
    git \
    jpeg-dev \
    linux-headers \
    musl-dev \
    zlib-dev

RUN pip install -U pip

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
