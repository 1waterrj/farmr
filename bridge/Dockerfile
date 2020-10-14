FROM python:latest

RUN pip install paho-mqtt
RUN pip install influxdb

ADD bridge.py /

CMD ["python","./bridge.py"]
