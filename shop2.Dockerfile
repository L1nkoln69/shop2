FROM python:3.10
RUN mkdir /code
WORKDIR /code
COPY Pipfile* /code/
ADD core /code/