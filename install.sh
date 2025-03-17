#!/bin/bash
set -e

echo "Installing your Python application..."

# Create a directory for the application
mkdir -p ~/.myapp

# Download the application files
curl -s https://your-domain.com/main.py -o ~/.myapp/main.py

# Install dependencies
pip install -r https://your-domain.com/requirements.txt

# Make the script executable
chmod +x ~/.myapp/main.py

# Create a symlink to make it available in PATH
ln -sf ~/.myapp/main.py /usr/local/bin/myapp

echo "Installation complete! Run 'myapp' to start the application."