# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

RUN python -m pip install poetry &&\
  pip install pip==20.0.2 &&\
  apt update

COPY pyproject.toml /srv/app/
WORKDIR /srv/app
RUN poetry config virtualenvs.create false &&\
  poetry install --no-dev --no-interaction --no-ansi

COPY . /srv/app/

RUN useradd -r -s /sbin/nologin app
RUN chown -R app:app /srv/app
USER app

CMD ["sh", "-c", "python manage.py make_default_admin \
      && python manage.py make_default_groups_and_permissions \
      && python manage.py make_fellowship_application_university_assessment \
      && python manage.py make_deadlines \
      && gunicorn -w 3 -k uvicorn.workers.UvicornWorker agof_ssp.asgi:application --bind 0.0.0.0:8000"]