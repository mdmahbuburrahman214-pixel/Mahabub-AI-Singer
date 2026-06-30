from huggingface_hub import snapshot_download

print("Downloading SadTalker models...")

snapshot_download(
    repo_id="vinthony/SadTalker-V002rc",
    local_dir="models",
    local_dir_use_symlinks=False
)

print("All models downloaded successfully.")
