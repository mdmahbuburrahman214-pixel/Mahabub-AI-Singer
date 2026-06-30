#!/usr/bin/env python3

import os
import sys
from pathlib import Path

import requests
from tqdm import tqdm

CHECKPOINT_DIR = Path("checkpoints")
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------------
# Add official model download URLs here
# Example:
#
# MODELS = {
#     "model_name.pth":
#     "https://example.com/model_name.pth"
# }
# -------------------------------------------------------------------

MODELS = {
}


def download_file(url: str, output_path: Path):

    response = requests.get(url, stream=True)

    response.raise_for_status()

    total = int(response.headers.get("content-length", 0))

    with open(output_path, "wb") as file, tqdm(
        desc=output_path.name,
        total=total,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as progress:

        for chunk in response.iter_content(chunk_size=8192):

            if chunk:
                file.write(chunk)
                progress.update(len(chunk))


def main():

    if len(MODELS) == 0:

        print("\nNo models configured.\n")
        print("Please add official model URLs inside MODELS dictionary.")
        sys.exit(0)

    print("\nDownloading AI Models...\n")

    for filename, url in MODELS.items():

        output = CHECKPOINT_DIR / filename

        if output.exists():

            print(f"✓ {filename} already exists.")
            continue

        try:

            download_file(url, output)

            print(f"✓ Downloaded {filename}")

        except Exception as e:

            print(f"✗ Failed: {filename}")
            print(e)

    print("\nAll downloads completed.")


if __name__ == "__main__":
    main()
