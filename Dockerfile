FROM python:3-alpine

LABEL author="alaa"
LABEL description="Dockerfile for Python script which prints Hello, Name"
COPY *.json /app/
COPY email_generator.py /app/
CMD python3 /app/email_generator.py
