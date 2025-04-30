first, unzip all the .zip files in your project directory:

unzip '*.zip'



# If you prefer not to use Docker
## Create virtual environment



python3 -m venv env





## Activate the environment (Linux/macOS)


source env/bin/activate





## If on Windows, run this instead:


.\env\Scripts\activate





## Install dependencies


pip install -r requirements.txt





## Run the Streamlit app


streamlit run Home.py

# Use Docker
### if You want to use Docker:
📦 Prerequisites

    Docker installed and running

    (Optional) Docker Compose if you prefer to use docker-compose.yml

1. Build the Docker image:
docker build -t streamlit-app .
2. Run the Docker container:
docker run -p 8501:8501 streamlit-app
3. Open your browser and go to:
 http://localhost:8501


# 🧩 (Optional) Run with Docker Compose
1. Run the App
docker-compose up --build
2. Stop the App
docker-compose down





## License

This repository is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.

**You may not use this code for commercial purposes.**

ESHRA DASHBOARD © 2025 by Ismail Sadouki is licensed under CC BY-NC 4.0

