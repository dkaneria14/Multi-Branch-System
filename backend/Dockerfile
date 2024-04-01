# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Install protobuf-compiler
RUN apt-get update && apt-get install -y protobuf-compiler

# Compile protobuf files
RUN python -m grpc_tools.protoc --python_out=. bank_service.proto --proto_path=. --grpc_python_out=. --pyi_out=.

# Expose the necessary port
EXPOSE 8000

# Define the command to run the application
CMD ["sh", "-c", "python server.py & uvicorn client:app --reload"]


