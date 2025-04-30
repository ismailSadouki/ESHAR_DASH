# Use Python 3.8 image as base (adjust to your version)
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's files into the container
COPY . /app/

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "Home.py"]

