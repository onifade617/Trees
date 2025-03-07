# Pull base image
FROM python:3.10

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

# Expose port
EXPOSE 8000

# Run server
CMD ["gunicorn", "blogs.wsgi:application", "--bind", "0.0.0.0:8000"]