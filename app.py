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
import os
import shutil
import subprocess
import gradio as gr

os.makedirs("assets/input", exist_ok=True)
os.makedirs("assets/output", exist_ok=True)

def generate(image, audio):

    img = "assets/input/image.png"
    wav = "assets/input/audio.wav"

    shutil.copy(image, img)
    shutil.copy(audio, wav)

    cmd = [
        "python",
        "liveportrait_runner.py",
        "--image",
        img,
        "--audio",
        wav
    ]

    subprocess.run(cmd)

    return "assets/output/output.mp4"

demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Image(type="filepath", label="Portrait Image"),
        gr.Audio(type="filepath", label="Song / Voice")
    ],
    outputs=gr.Video(),
    title="Mahabub AI Singer Studio",
    description="Generate AI Singing Video using LivePortrait"
)

demo.launch(share=True)
import gradio as gr
from sadtalker_runner import generate

def run(image, audio):
    output_dir = generate(image, audio)
    return output_dir

demo = gr.Interface(
    fn=run,
    inputs=[
        gr.Image(type="filepath", label="Portrait Image"),
        gr.Audio(type="filepath", label="Song / Voice")
    ],
    outputs=gr.File(label="Generated Video"),
    title="Mahabub AI Singer Studio"
)

demo.launch(share=True)
