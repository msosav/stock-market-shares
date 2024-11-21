FROM python:3.11-slim

WORKDIR /code

RUN pip install fastapi[standard]

COPY . /code/

EXPOSE 80

CMD ["sh", "-c", "fastapi run api.py --proxy-headers --port 80"]