FROM python:alpine

LABEL maintainer="Saeid Bostandoust <ssbostan@yahoo.com>"

EXPOSE 80

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn
