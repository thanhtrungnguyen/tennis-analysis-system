# Use the official PostgreSQL image as the base image
FROM postgres:17.0-alpine3.20

ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_PORT

# Set environment variables for the database
# You can change these values to match your configuration
ENV POSTGRES_DB=$POSTGRES_DB
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_PORT=$POSTGRES_PORT

# Copy any SQL files you want to execute when the container starts
# Typically used to pre-populate your database
# Uncomment if you have SQL initialization scripts
# COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL default port
EXPOSE $POSTGRES_PORT

# By default, the official PostgreSQL image runs the server
