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
import gradio as gr

def generate(image, audio):

    return "Coming Soon"

demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Image(type="filepath"),
        gr.Audio(type="filepath")
    ],
    outputs="text",
    title="Mahabub AI Singer Studio"
)

demo.launch()
import gradio as gr
from liveportrait_runner import generate

def run(image, audio):

    output = generate(image, audio)

    return output

demo = gr.Interface(
    fn=run,
    inputs=[
        gr.Image(type="filepath"),
        gr.Audio(type="filepath")
    ],
    outputs=gr.File(),
    title="Mahabub AI Singer Studio"
)

demo.launch()
