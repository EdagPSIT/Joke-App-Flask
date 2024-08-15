FROM python:3.13.0a1-alpine3.18

# Set the working directory in the container
WORKDIR /jokeapp

# Copy the requirements file first to leverage Docker's caching mechanism
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary files
COPY src/ /jokeapp/src

# Expose the port on which the app will run
EXPOSE 5000

# Use the Waitress server to run the application in production
CMD ["waitress-serve", "--port=5000", "src.app:app"]
