# Use the latest Python image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the pip packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]
