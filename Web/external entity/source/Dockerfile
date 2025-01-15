# Use the official Python image as a base
FROM python:3.10-slim

WORKDIR /src

COPY src/ /src/
COPY flag.txt /flag.txt

RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir lxml

# Expose the port the app runs on
EXPOSE 10002

# Define the command to run the application
CMD ["python", "app.py"]
