FROM python:3.13.0a1-alpine3.18

WORKDIR /jokeapp

# Copy the Flask app code into the container
COPY app.py /jokeapp/app.py
COPY requirements.txt /jokeapp/requirements.txt

# Install Flask
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
