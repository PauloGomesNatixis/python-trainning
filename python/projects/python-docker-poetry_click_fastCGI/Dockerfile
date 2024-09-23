# Dockerfile

# Step 1: Use the official Python image from Docker Hub
FROM python:3.12-slim

# Step 2: Install Poetry
#ENV POETRY_VERSION=1.5.1

# Install Poetry dependencies and Poetry itself
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry



# Step 3: Set the working directory inside the container
WORKDIR /workspace

# Step 4: Copy the project files into the container
COPY pyproject.toml .
#COPY main.py ./
COPY src/ /workspace
#COPY . /workspace
#mas coisa que usar COPY . ./workspace


# Step 5: Install dependencies with Poetry
RUN poetry install --no-root
#--no-interaction --no-ansi

# Expose the application port (this is optional, for documentation purposes)
#EXPOSE 8000


# Step 6: Set the entry point to run the Python script
#CMD ["poetry", "run", "python", "./src/main.py"]
#CMD ["poetry", "run", "fastapi","dev", "main.py"]
# Set the entry point to run FastAPI development server with Poetry
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



#FROM python:3.11-slim

#WORKDIR /app

#RUN pip install poetry