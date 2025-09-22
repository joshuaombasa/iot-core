#!/bin/bash
set -euo pipefail

echo "Setting up Vibration Monitor..."

# Update system and install dependencies
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment for isolation
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install required Python packages
if [ -f "requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "requirements.txt not found, skipping Python package installation."
fi

echo "Setup complete. To activate the environment, run: source venv/bin/activate"
