FROM python:3.8

WORKDIR /Example-API
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /Example-API/server
COPY server/ .
WORKDIR /Example-API/test
COPY test/ .
WORKDIR /Example-API/src
COPY src/ .
WORKDIR /Example-API
CMD ["python3", "./server/server.py"]