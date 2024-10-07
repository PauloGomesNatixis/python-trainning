
# ```bash
# touch Dockerfile
# ```

# 10. Add the following code to `Dockerfile`:

# ```Dockerfile
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install project dependencies
RUN poetry install --only main

# Entrypoint
RUN chmod a+x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]