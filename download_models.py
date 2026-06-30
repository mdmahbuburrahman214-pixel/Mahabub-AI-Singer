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
import os
import urllib.request

CHECKPOINT_DIR = "checkpoints"
os.makedirs(CHECKPOINT_DIR, exist_ok=True)

MODELS = {
    # পরের ধাপে LivePortrait-এর অফিসিয়াল model URL যোগ করা হবে
}

for filename, url in MODELS.items():
    path = os.path.join(CHECKPOINT_DIR, filename)

    if os.path.exists(path):
        print(filename, "already exists.")
        continue

    print("Downloading", filename)
    urllib.request.urlretrieve(url, path)

print("All models ready.")
