#!/bin/bash
set -e

echo "====================================="
echo " Mahabub AI Singer Studio Installer"
echo "====================================="

apt-get update
apt-get install -y ffmpeg git wget

pip install --upgrade pip

pip install -r requirements.txt

mkdir -p assets/input
mkdir -p assets/output
mkdir -p checkpoints

echo "Installation Complete."
