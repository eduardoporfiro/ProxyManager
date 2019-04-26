FROM python:3.6

WORKDIR /code
COPY . /code
RUN  pip install -r requirements.txt