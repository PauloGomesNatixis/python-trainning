# # Use the official Python 3.12 image as the base
# FROM python:3.12

# # Install Poetry for dependency management
# RUN pip install poetry

# # Set the working directory inside the container
# WORKDIR /jupiter

# # Copy all files from the current directory to the working directory
# COPY . .

# # Install dependencies defined in pyproject.toml using Poetry
# RUN poetry install

# # Expose the Jupyter Notebook port
# EXPOSE 8888

# # Command to run Jupyter Notebook
# CMD ["poetry", "run", "jupyter-server", "--allow-root", "--ip=0.0.0.0", "--port=8888"]
# #CMD ["poetry","run","jupiter","notebook","--allow-root","--ip=0.0.0.0","--port=8888"]



# Use the official Jupyter base notebook image
FROM jupyter/base-notebook

# Set the working directory inside the container
WORKDIR /jupyter

# Copy your Jupyter notebooks or files into the container (optional)
COPY . .

# Expose the Jupyter Notebook port
EXPOSE 8888

# Command to run Jupyter Notebook
CMD ["start-notebook.sh"] 
#, "--NotebookApp.token=''", "--NotebookApp.password=''"]
