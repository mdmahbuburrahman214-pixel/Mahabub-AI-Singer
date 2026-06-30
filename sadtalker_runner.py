import subprocess

def generate(image_path, audio_path):

    cmd = [
        "python",
        "SadTalker/inference.py",
        "--driven_audio", audio_path,
        "--source_image", image_path,
        "--result_dir", "assets/output"
    ]

    subprocess.run(cmd, check=True)

    return "assets/output"
