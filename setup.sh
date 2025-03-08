#!/bin/bash
echo "Setting up Vibration Monitor..."
sudo apt update && sudo apt install -y python3-pip
pip install -r requirements.txt
echo "Setup complete!"
