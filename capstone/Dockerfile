FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN apt-get update 
RUN apt-get -y upgrade
RUN python -m pip install --upgrade pip
RUN pip install Django requests pandas mysqlclient scikit-learn pillow gunicorn

COPY . /opt/django/
WORKDIR /opt/django/capstone_app/


