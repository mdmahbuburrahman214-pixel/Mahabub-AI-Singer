mkdir -p assets/input
mkdir -p assets/output
mkdir -p checkpoints

echo "Downloading AI Models..."
python download_models.py

echo "Installation Complete."
git clone https://github.com/KwaiVGI/LivePortrait.git
cd LivePortrait
pip install -r requirements.txt
cd ..
mkdir -p assets/input
mkdir -p assets/output
mkdir -p checkpoints

echo "Downloading AI Models..."
python download_models.py

echo "Installation Complete."
