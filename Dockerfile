# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

LABEL Author="MichaelFrohlich"

RUN python -m pip install poetry &&\
  pip install pip==20.0.2 &&\
  apt update

COPY pyproject.toml /srv/app/
WORKDIR /srv/app
RUN poetry config virtualenvs.create false &&\
  poetry install --no-dev --no-interaction --no-ansi

COPY . /srv/app/

RUN ls .

# Install any needed packages specified in requirements.txt
RUN poetry install

VOLUME /app

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000