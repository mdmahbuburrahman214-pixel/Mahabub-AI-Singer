import subprocess

def generate(image_path, audio_path):

    cmd = [
        "python",
        "LivePortrait/inference.py",
        "--source",
        image_path,
        "--driving",
        audio_path,
        "--output_dir",
        "assets/output"
    ]

    subprocess.run(cmd, check=True)

    return "assets/output"
import subprocess

def run(image, driving):

    cmd = [
        "python",
        "LivePortrait/inference.py",
        "-s", image,
        "-d", driving
    ]

    subprocess.run(cmd, check=True)

    return "LivePortrait/animations"
