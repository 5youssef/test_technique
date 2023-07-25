# Use the official Python image as the base image
FROM python:3.9

# Set environment variables (modify as needed)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django app folder into the container
COPY . /app/

# Expose the Django development server port (modify if needed)
EXPOSE 8000

# Command to start the Django development server
CMD ["python", "manage.py", "runserver", "localhost:8000"]
