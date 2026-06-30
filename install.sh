#!/bin/bash
set -e

echo "========================================"
echo "    Mahabub AI Singer Studio Installer"
echo "========================================"

echo "[1/8] Updating system packages..."
apt-get update -y

echo "[2/8] Installing system dependencies..."
apt-get install -y \
    git \
    wget \
    curl \
    unzip \
    ffmpeg

echo "[3/8] Upgrading pip..."
python -m pip install --upgrade pip setuptools wheel

echo "[4/8] Installing Python requirements..."
pip install -r requirements.txt

echo "[5/8] Creating project folders..."
mkdir -p assets/input
mkdir -p assets/output
mkdir -p checkpoints

echo "[6/8] Cloning LivePortrait..."
if [ ! -d "LivePortrait" ]; then
    git clone https://github.com/KwaiVGI/LivePortrait.git
else
    echo "LivePortrait already exists."
fi

echo "[7/8] Cloning SadTalker..."
if [ ! -d "SadTalker" ]; then
    git clone https://github.com/OpenTalker/SadTalker.git
else
    echo "SadTalker already exists."
fi

echo "[8/8] Downloading AI models..."
python download_models.py

echo ""
echo "========================================"
echo " Installation Completed Successfully!"
echo "========================================"
echo ""
echo "Run the application:"
echo "python app.py"
