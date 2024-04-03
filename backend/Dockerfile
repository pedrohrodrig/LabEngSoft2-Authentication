FROM python:3.10-slim

WORKDIR /app

COPY Pipfile* ./
RUN pip install pipenv && pipenv install
COPY . /app

EXPOSE 8000

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]
