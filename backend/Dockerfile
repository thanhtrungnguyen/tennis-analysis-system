# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install Python dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . /code/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
