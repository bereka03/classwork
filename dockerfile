# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set environment variables
ENV FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000 \
    APP_USER=flaskuser

# Create a non-root user and group
RUN groupadd -r $APP_USER && useradd -r -g $APP_USER $APP_USER

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Create the instance directory and set permissions
RUN mkdir instance && chown -R $APP_USER:$APP_USER instance
RUN chmod 777 instance

# Change to the non-root user
USER $APP_USER

# Expose the port that Flask app runs on
EXPOSE 5000

# Set the container's entrypoint command
CMD ["flask", "run"]