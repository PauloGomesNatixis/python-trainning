
# ```bash
# touch Dockerfile
# ```

# 10. Add the following code to `Dockerfile`:

# ```Dockerfile
# get image call python:3.10
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /api

# Copy the project files
COPY pyproject.toml .
RUN mkdir src
COPY src/main.py src/
COPY entrypoint.sh /api/

# Install project dependencies
RUN poetry install --only main

# Entrypoint
RUN chmod a+x /api/entrypoint.sh
ENTRYPOINT ["/api/entrypoint.sh"]

EXPOSE 80

# #USER api

# #CMD [ "poetry","run","uvicorn","api:app","--host","0.0.0.0","8000:8000","fastapi-app","fastapi"]
# CMD [ "poetry","run","uvicorn","src.fastapi-app:fastapi","--host","0.0.0.0","80"]