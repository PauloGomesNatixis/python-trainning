#!/bin/bash

echo "Container starting up..."

set -e

function print_help {
    echo "Available options:"
    echo "bash - Runs bash"
    echo "fastapi - Runs FastAPI"
    echo "flask - Runs Flask"
}

case ${1} in
bash)
    exec bash
    ;;
fastapi)
    exec poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
    ;;
*)
    print_help
    ;;
esac