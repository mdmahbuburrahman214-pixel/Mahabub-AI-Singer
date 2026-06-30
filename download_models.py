import os
import gdown

os.makedirs("checkpoints", exist_ok=True)

MODELS = {
    # পরে আসল Model URL বসানো হবে
}

for name, url in MODELS.items():
    output = os.path.join("checkpoints", name)
    if not os.path.exists(output):
        print(f"Downloading {name}...")
        gdown.download(url, output, quiet=False)

print("All models downloaded.")
