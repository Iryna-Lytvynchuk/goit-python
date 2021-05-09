
FROM python:3-slim-buster

WORKDIR app

RUN pip install pipenv


COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy

COPY main.py main.py

CMD python main.py