# Dockerfile

# Step 1: Use the official Python image from Docker Hub
FROM python:3.10-slim

# Step 2: Install Poetry
#ENV POETRY_VERSION=1.5.1

# Install Poetry dependencies and Poetry itself
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the project files into the container
COPY pyproject.toml ./
COPY main.py ./
COPY src/ ./src/


# Step 5: Install dependencies with Poetry
RUN poetry install --no-interaction --no-ansi

# Step 6: Set the entry point to run the Python script
CMD ["poetry", "run", "python", "main.py"]
CMD ["poetry", "run", "python", "src/commands.py"]



#FROM python:3.11-slim

#WORKDIR /app

#RUN pip install poetry