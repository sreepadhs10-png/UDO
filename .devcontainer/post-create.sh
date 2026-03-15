#!/usr/bin/env bash
set -e

# Ensure Node is installed
npm --version || (curl -fsSL https://deb.nodesource.com/setup_18.x | sudo bash - && sudo apt-get install -y nodejs)

# Upgrade pip
python3 -m pip install --upgrade pip

# Install Python dependencies
if [ -f services/api-nlp/requirements.txt ]; then
  pip3 install -r services/api-nlp/requirements.txt
fi