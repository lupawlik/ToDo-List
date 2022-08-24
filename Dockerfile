FROM python:3.10-buster

ENV PYTHONUNBUFFERD=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

