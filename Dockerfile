FROM python:3.11.5

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN chmod a+x src/fa_project/app.sh

ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
