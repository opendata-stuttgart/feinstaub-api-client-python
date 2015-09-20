FROM python:3.5-slim

USER root
RUN pip install --upgrade pip

ADD . /opt/code
WORKDIR /opt/code

RUN pip install -r /opt/code/requirements.txt

CMD python client.py
