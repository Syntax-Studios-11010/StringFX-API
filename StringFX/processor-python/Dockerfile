# Use an official lightweight Python runtime
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file first to leverage Docker caching
COPY ./Requirements.txt /code/Requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/Requirements.txt

# Copy the rest of your application code
COPY ./app /code/app

# Expose the port FastAPI runs on
EXPOSE 8001

# Command to run the FastAPI app via uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]