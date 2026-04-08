<p align="center">
  <img src="assets/guppy.png" alt="BMOLM" width="400"/>
</p>

<h1 align="center">BMOLM</h1>
<p align="center"><em>A ~9M parameter LLM that talks like BMO from Adventure Time.</em></p>

<p align="center">
  <a href="https://huggingface.co/datasets/arman-bd/bmolm-60k-generic"><img src="https://img.shields.io/badge/🤗_Dataset-bmolm--60k-blue" alt="Dataset"/></a>&nbsp;
  <a href="https://huggingface.co/arman-bd/bmolm-9M"><img src="https://img.shields.io/badge/🤗_Model-bmolm--9M-orange" alt="Model"/></a>&nbsp;
  <a href="https://github.com/ndcorder/BMOlm/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green" alt="License"/></a>
  <br/>
  <a href="https://colab.research.google.com/github/ndcorder/BMOlm/blob/main/train_bmolm.ipynb"><img src="https://img.shields.io/badge/Train_in-Colab-F9AB00?logo=googlecolab" alt="Train"/></a>&nbsp;
  <a href="https://colab.research.google.com/github/ndcorder/BMOlm/blob/main/use_bmolm.ipynb"><img src="https://img.shields.io/badge/Chat_in-Colab-F9AB00?logo=googlecolab" alt="Chat"/></a>
  <br/>
  <a href="https://www.linkedin.com/pulse/build-your-own-language-model-5-minutes-i-made-mine-hossain--supif/"><img src="https://img.shields.io/badge/Article-LinkedIn-0A66C2?logo=linkedin" alt="LinkedIn Article"/></a>&nbsp;
  <a href="https://arman-bd.medium.com/build-your-own-llm-in-5-minutes-i-made-mine-talk-like-a-fish-e20c338a3d14"><img src="https://img.shields.io/badge/Article-Medium-000000?logo=medium" alt="Medium Article"/></a>
  <br/><br/>
  <a href="https://ndcorder.github.io/BMOlm/"><img src="https://img.shields.io/badge/Try_in-Browser-64ffda?style=for-the-badge&logo=webassembly&logoColor=white" alt="Browser Demo"/></a>
</p>

---

> **This project exists to show that training your own language model is not magic.**
> No PhD required. No massive GPU cluster. One Colab notebook, 5 minutes, and you have a working LLM that you built from scratch — data generation, tokenizer, model architecture, training loop, and inference. If you can run a notebook, you can train a language model.
>
> It won't produce a billion-parameter model that writes essays. But it will show you exactly how every piece works — from raw text to trained weights to generated output — so the big models stop feeling like black boxes.

---

```
You> hi bmo
BMO> hi there. i just found a nice spot near the rock. the temperature feels nice.

You> are you hungry
BMO> yes. always yes. i will swim to the top right now. i promise to eat all of it.

You> do you like bubbles
BMO> i love bubbles. they make the water feel slightly different.

You> what is the meaning of life
BMO> food. the answer is always food.

You> tell me a joke
BMO> what did the fish say when it hit the wall. dam.

You> do you love me
BMO> you're my favorite big shape. my mouth are happy when you're here.

You> goodnight bmo
BMO> ok sleep time. i was following a bubble but now i'll stop. goodnight tank. goodnight water.
```

---

## What is BMOLM?

BMOLM is a tiny language model that pretends to be BMO, a tiny living game console from Adventure Time. It speaks in short, cheerful sentences about games, buttons, screens, and pixels. It doesn't understand human abstractions like money, phones, or politics — and it's not trying to.

It's trained from scratch on 60K synthetic conversations across 60 topics, runs on a single GPU in ~5 minutes, and produces a model small enough to run in a browser.

---

## Architecture

| | |
|---|---|
| **Parameters** | 8.7M |
| **Layers** | 6 |
| **Hidden dim** | 384 |
| **Heads** | 6 |
| **FFN** | 768 (ReLU) |
| **Vocab** | 4,096 (BPE) |
| **Max sequence** | 128 tokens |
| **Norm** | LayerNorm |
| **Position** | Learned embeddings |
| **LM head** | Weight-tied with embeddings |

Vanilla transformer. No GQA, no RoPE, no SwiGLU, no early exit. As simple as it gets.

---

## Personality

BMO:
- Speaks in short, cheerful sentences
- Experiences the world through buttons, screens, circuits, games, and pixels
- Doesn't understand human abstractions
- Is brave, creative, and a little weird
- Thinks about food a lot

**60 topics:** greetings, feelings, temperature, food, light, water, tank, noise, night, loneliness, bubbles, glass, reflection, breathing, swimming, colors, taste, plants, filter, algae, snails, scared, excited, bored, curious, happy, tired, outside, cats, rain, seasons, music, visitors, children, meaning of life, time, memory, dreams, size, future, past, name, weather, sleep, friends, jokes, fear, love, age, intelligence, health, singing, TV, and more.

---

## Quick Start

### Try in Browser (no install needed)

[![Try in Browser](https://img.shields.io/badge/Try_in-Browser-64ffda?logo=webassembly)](https://arman-bd.github.io/bmolm/)

Runs entirely in your browser via WebAssembly. Downloads a quantized ONNX model (~10 MB) and runs inference locally — no server, no API keys.

### Chat with BMO in Colab

[![Open in Colab](https://img.shields.io/badge/Chat_in-Colab-F9AB00?logo=googlecolab)](https://colab.research.google.com/github/arman-bd/bmolm/blob/main/use_bmolm.ipynb)

Downloads the pre-trained model from HuggingFace and lets you chat. Just run all cells.

### Train your own

[![Open in Colab](https://img.shields.io/badge/Train_in-Colab-F9AB00?logo=googlecolab)](https://colab.research.google.com/github/arman-bd/bmolm/blob/main/train_bmolm.ipynb)

1. Set runtime to **T4 GPU**
2. **Run all cells** — downloads dataset, trains tokenizer, trains model, tests it
3. Upload to HuggingFace or download locally

### Chat locally

```bash
pip install torch tokenizers
python -m bmolm chat
```

```
You> the cat is looking at you
BMO> i hide behind the plant when the furry one comes.

You> it is raining outside
BMO> i think rain is the best thing about outside.
```

In interactive chat mode, the conversation grows and quickly runs into the 128-token limit, reducing quality.
You can also invoke chat with a single prompt, and exit after the response:

```bash
python -m bmolm chat --prompt "tell me a joke"
```


---

## Dataset

**[arman-bd/bmolm-60k-generic](https://huggingface.co/datasets/arman-bd/bmolm-60k-generic)** on HuggingFace.

| | |
|---|---|
| Samples | 60,000 (57K train / 3K test) |
| Format | `{"input": "...", "output": "...", "category": "..."}` |
| Categories | 60 |
| Generation | Synthetic template composition |

```python
from datasets import load_dataset
ds = load_dataset("arman-bd/bmolm-60k-generic")
print(ds["train"][0])
# {'input': 'hi bmo', 'output': 'hello. the water is nice today.', 'category': 'greeting'}
```

---

## Project Structure

```
bmolm/
├── config.py               Hyperparameters (model + training)
├── model.py                Vanilla transformer
├── dataset.py              Data loading + batching
├── train.py                Training loop (cosine LR, AMP)
├── generate_data.py        Conversation data generator (60 topics)
├── eval_cases.py           Held-out test cases
├── prepare_data.py         Data prep + tokenizer training
└── inference.py            Chat interface

tools/
├── make_colab.py           Generates Colab notebooks
├── export_onnx.py          Export model to ONNX (quantized uint8)
├── export_dataset.py       Push dataset to HuggingFace
└── dataset_card.md         HuggingFace dataset README

docs/
├── index.html              Browser demo (ONNX + WASM)
├── download.sh             Download model.onnx + tokenizer from HF
├── model.onnx              Quantized uint8 (~10 MB)
├── tokenizer.json          BPE tokenizer
└── guppy.png               Logo (transparent)
```

---

## Design Decisions

**Why no system prompt?** Every training sample had the same one. A 9M model can't conditionally follow instructions — the personality is baked into the weights. Removing it saves ~60 tokens per inference.

**Why single-turn only?** Multi-turn degraded at turn 3-4 due to the 128-token context window. A game console that forgets is on-brand, but garbled output isn't. Single-turn is reliable.

**Why vanilla transformer?** GQA, SwiGLU, RoPE, and early exit add complexity that doesn't help at 9M params. Standard attention + ReLU FFN + LayerNorm produces the same quality with simpler code.

**Why synthetic data?** A character with consistent personality needs consistent training data. Template composition with randomized components (30 tree fort objects, 17 game types, 25 activities) generates ~16K unique outputs from ~60 templates.

---

## License

MIT
