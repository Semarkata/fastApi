FROM python:alpine3.19

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn

COPY . /app