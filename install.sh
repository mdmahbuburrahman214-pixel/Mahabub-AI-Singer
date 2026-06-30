#!/bin/bash

set -e

echo "========================================="
echo " Mahabub AI Singer Studio Installer"
echo "========================================="

python -m pip install --upgrade pip

pip install -r requirements.txt

echo "Installation Complete."
