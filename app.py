#!/bin/bash
set -e

echo "========================================"
echo " Mahabub AI Singer Studio Installer"
echo "========================================"

sudo apt-get update
sudo apt-get install -y ffmpeg git wget unzip

python -m pip install --upgrade pip

pip install -r requirements.txt

mkdir -p assets/input
mkdir -p assets/output
mkdir -p checkpoints

# Clone LivePortrait
if [ ! -d "LivePortrait" ]; then
    git clone https://github.com/KwaiVGI/LivePortrait.git
fi

cd LivePortrait
pip install -r requirements.txt
cd ..

echo "Downloading Models..."
python download_models.py

echo "Installation Finished Successfully."
