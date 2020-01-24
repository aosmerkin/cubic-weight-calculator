########### Base #############
FROM python:3.6 AS prod

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

COPY calculator calculator
COPY setup.py setup.py

RUN pip install .

ENTRYPOINT ["cubic-weight-calculator"]

########### Dev Base #############
FROM prod AS dev

RUN pip uninstall -y cubic-weight-calculator
RUN pipenv install --dev --system --deploy --ignore-pipfile
COPY tests tests

ENTRYPOINT ["/usr/bin/env"]
CMD python -m pytest --cov=calculator
