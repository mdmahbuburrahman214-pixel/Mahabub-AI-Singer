mkdir -p assets/input
mkdir -p assets/output
mkdir -p checkpoints

echo "Downloading AI Models..."
python download_models.py

echo "Installation Complete."
