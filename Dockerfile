# Pull base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /Trees

# Install dependencies
COPY Pipfile Pipfile.lock /Trees/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /Trees/