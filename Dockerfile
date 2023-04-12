FROM python:3.10-alpine

WORKDIR /fastapi_app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry \
    && poetry config virtualenvs.create false\
    && poetry install --without dev --no-root

COPY . .

RUN chmod a+x *.sh
