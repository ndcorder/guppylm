"""Entry point for: python -m bmolm"""

import os
import sys

CHECKPOINT_PATH = "checkpoints/best_model.pt"
TOKENIZER_PATH = "data/tokenizer.json"
HF_REPO = "arman-bd/bmolm-9M"
HF_BASE = f"https://huggingface.co/{HF_REPO}/resolve/main"


def download_model():
    """Download pre-trained BMOLM from HuggingFace."""
    import urllib.request

    files = [
        (f"{HF_BASE}/pytorch_model.bin", CHECKPOINT_PATH),
        (f"{HF_BASE}/tokenizer.json", TOKENIZER_PATH),
        (f"{HF_BASE}/config.json", "checkpoints/config.json"),
    ]

    print(f"Downloading BMOLM from {HF_REPO}...\n")
    for url, dest in files:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        name = os.path.basename(dest)
        print(f"  {name}...", end=" ", flush=True)
        urllib.request.urlretrieve(url, dest)
        size_mb = os.path.getsize(dest) / 1e6
        print(f"{size_mb:.1f} MB")

    print("\nDone! Run: python -m bmolm chat")


def main():
    if len(sys.argv) < 2:
        print("BMOLM — A tiny living game console brain")
        print()
        print("Usage:")
        print("  python -m bmolm train        Train the model")
        print("  python -m bmolm prepare      Generate data & train tokenizer")
        print("  python -m bmolm chat         Chat with BMO")
        print("  python -m bmolm download     Download pre-trained model from HuggingFace")
        return

    cmd = sys.argv[1]
    sys.argv = sys.argv[1:]

    if cmd == "prepare":
        from .prepare_data import prepare
        prepare()

    elif cmd == "train":
        from .train import train
        train()

    elif cmd == "download":
        download_model()

    elif cmd == "chat":
        if not os.path.exists(CHECKPOINT_PATH):
            print("Model not found. Download the pre-trained model first:\n")
            print("  python -m bmolm download\n")
            print("Or train your own:\n")
            print("  python -m bmolm prepare")
            print("  python -m bmolm train")
            return

        from .inference import main as inference_main
        inference_main()

    else:
        print(f"Unknown command: {cmd}")
        print("Run 'python -m bmolm' for usage.")


main()
