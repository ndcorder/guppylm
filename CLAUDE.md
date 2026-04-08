# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

BMOLM is a ~9M parameter toy LLM trained from scratch on 60K synthetic conversations. The model plays BMO, the tiny living game console from Adventure Time. Vanilla transformer, single-turn only, 128-token context window.

- GitHub: `ndcorder/BMOlm`
- HuggingFace model: `arman-bd/bmolm-9M`
- HuggingFace dataset: `arman-bd/bmolm-60k-generic`
- Browser demo at `docs/` served via GitHub Pages

## Commands

```bash
# Full pipeline: generate data + train tokenizer
python -m bmolm prepare

# Train the model (outputs to checkpoints/)
python -m bmolm train

# Interactive chat (requires trained model)
python -m bmolm chat

# Single prompt
python -m bmolm chat --prompt "hi bmo"

# Download pre-trained model from HuggingFace
python -m bmolm download

# Run eval cases against trained model
python -m bmolm eval

# Export to ONNX for browser demo
python tools/export_onnx.py                # quantized uint8
python tools/export_onnx.py --no-quantize  # float32

# Push dataset/model to HuggingFace (needs HF_TOKEN + HF_REPO in .env)
python tools/export_dataset.py --push
python tools/export_model.py --push

# Generate Colab notebooks
make notebook
```

## Dependencies

`torch`, `tokenizers`, `tqdm`, `numpy`, `datasets`. Install via `pip install -r requirements.txt`. No test framework is configured.

## Architecture

The CLI entrypoint is `bmolm/__main__.py` which dispatches subcommands (`prepare`, `train`, `chat`, `download`, `eval`).

**Pipeline flow:** `generate_data.py` (synthetic conversations) -> `prepare_data.py` (writes JSONL + trains BPE tokenizer) -> `train.py` (training loop) -> `inference.py` (chat).

**Model:** Standard decoder-only transformer in `model.py`. 6 layers, 384 hidden dim, 6 heads, ReLU FFN, LayerNorm, learned positional embeddings, weight-tied LM head. No system prompt at inference — personality is baked into weights.

**Data generation** (`generate_data.py`): Template composition with randomized components across 60 topic categories. Each category has its own `gen_*` function producing BMO-style conversations about games, buttons, screens, circuits, and the Tree Fort.

**Config** (`config.py`): Two dataclasses — `BMOConfig` (model hyperparameters) and `TrainConfig` (training hyperparameters). All defaults are hardcoded; no CLI arg parsing for config overrides.

**Inference** (`inference.py`): `BMOInference` class loads a checkpoint + tokenizer, formats prompts with ChatML-style `<|im_start|>`/`<|im_end|>` tokens, runs autoregressive generation. Supports both embedded config in checkpoints and standalone `config.json` files (with HuggingFace key aliases).

**Browser demo** (`docs/index.html`): Runs quantized ONNX model via onnxruntime-web. Self-contained — no build step.

## Data Layout

- `data/` — generated at prepare time: `train.jsonl`, `eval.jsonl`, `tokenizer.json`
- `checkpoints/` — generated at train time: `best_model.pt`, `config.json`, step snapshots
- `docs/` — browser demo assets (committed): `model.onnx`, `tokenizer.json`, `index.html`

## Key Constraints

- 128-token max sequence length; single-turn conversations only
- Vocab size 4,096 (BPE); special tokens: `<pad>`=0, `<|im_start|>`=1, `<|im_end|>`=2
- No test suite — `eval_cases.py` contains held-out prompts evaluated qualitatively via `python -m bmolm eval`
- Tools in `tools/` use `sys.path.insert` to import from `bmolm/` directly rather than relative imports
