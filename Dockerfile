FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
COPY ./app /app

