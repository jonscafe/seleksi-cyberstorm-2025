# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask pyjwt

EXPOSE 10004

ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]