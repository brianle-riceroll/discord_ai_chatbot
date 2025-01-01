#!/bin/bash

# Check if a virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "Installing dependencies..."
    ./.venv/bin/pip install -r requirements.txt
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source ./.venv/bin/activate

# Run the Python script
echo "Running main.py..."
python3 ./src/main.py

# Deactivate the virtual environment after execution
deactivate
