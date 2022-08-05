# pull official base image
FROM python:3.10.4-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY pyproject.toml .
RUN pip install --upgrade pip \
    && pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# copy project
COPY . .

# run entrypoint.sh
CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]