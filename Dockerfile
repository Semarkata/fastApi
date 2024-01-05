FROM python:alpine3.19

# Install Fast API
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn

# install dependencies
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Start Fast API server
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

EXPOSE 8080