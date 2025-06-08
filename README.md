# 🧠 TorsionNet

> **Topological Reasoning Engine to Detect Hallucinations in Transformer Models**

TorsionNet is a research-grade project that explores a groundbreaking hypothesis in AI safety and explainability:

> Hallucinations in large language models are not just training flaws — they are **topological failures** in reasoning space.

This project demonstrates a hybrid framework combining **transformer language models** (like GPT-2) with **algebraic topology** and **concept graph torsion** to:

* Model semantic constraints,
* Detect logical hallucinations,
* Enforce discrete, non-continuous reasoning boundaries.

---

## 🔌 Why This Project Matters

Current LLMs operate in **continuous vector spaces**, where any concept can smoothly blend into any other. This is a mathematical artifact of the architecture (e.g., attention mechanisms and embedding projections), and leads to:

✅ Rich interpolative reasoning
🚫 Invalid concept transitions (hallucinations) like `"Paris is the capital of Jupiter"`

**Real intelligence** requires **discrete, non-interpolable boundaries** — enforced mathematically via **torsion** and **sheaf cohomology**.

---

## 🧮 Core Concepts

| Concept                 | Description                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| **Concept Graph**       | A directed graph of discrete semantic units (e.g., `Paris → France → Europe`)                     |
| **Torsion Constraint**  | A logical discontinuity between concepts (e.g., `Paris →∅ Jupiter`) — encoded as a forbidden edge |
| **Semantic Ring**       | An algebraic structure where concepts form loops or cycles of meaning                             |
| **Cohomological Error** | A hallucination arising from violating topological constraints during token prediction            |

---

## 📁 Project Structure

```bash
torsionnet/
├── run.py                     # Main pipeline: generation + torsion check
├── requirements.txt
├── README.md
├── config/
│   └── config.yaml            # Model + torsion settings
├── data/
│   └── concepts.json          # Concept graph and invalid transitions
├── notebooks/
│   └── playground.ipynb       # Jupyter experiments
├── src/
│   ├── transformer/
│   │   └── wrapper.py         # GPT-2 interface
│   ├── topology/
│   │   ├── graph.py           # Concept graph & torsion rules
│   │   └── validator.py       # Hallucination detection logic
│   └── visualizer/
│       └── app.py             # Flask API for graph visualization
```

---

## 🚀 How to Run

### 1. Clone and Install

```bash
git clone https://github.com/sukanyaghosh74/TorsionNet.git
cd TorsionNet
pip install -r requirements.txt
```

### 2. Generate Output and Check for Hallucinations

```bash
python run.py
```

Sample output:

```
Prompt: Paris is...
Generated: Paris is the capital of Jupiter and has many moons.
🚫 Invalid Transition Detected: Paris → Jupiter
```

### 3. Launch Visual API (optional)

```bash
python src/visualizer/app.py
```

Go to: [http://127.0.0.1:5000/concepts](http://127.0.0.1:5000/concepts)

---

## 🔎 Internals: How It Works

### 🧠 TransformerWrapper

Wraps a pre-trained GPT-2 model using HuggingFace. Outputs token-level text for prompts.

### 🌐 Concept Graph (`concepts.json`)

Represents discrete semantic spaces. Built using:

* Nodes: valid concepts (e.g., `Paris`, `France`)
* Forbidden Edges: invalid transitions (e.g., `Paris → Jupiter`)

### 🔍 TorsionChecker

Validates text against the concept graph:

* Tokenizes output
* Checks if any forbidden edges exist in the reasoning path
* Flags hallucinations if they cross topological boundaries

---

## 🧠 Future Directions

* 🔬 **Torsion-Regularized Transformers**: Modify the attention mechanism to bias against invalid topology transitions during generation.
* 🌐 **Auto-expansion of Concept Graph**: Extract valid/incompatible concepts from WordNet, Wikipedia, or Wikidata.
* 🎨 **Graphical UI for Real-Time Hallucination Monitoring**
* 📈 **Cohomological Heatmaps**: Visualize regions of semantic instability in the latent space

---

## 📚 Inspired By

* [David Hodge's post on topological hallucinations](https://www.linkedin.com/posts/dhodge360_%F0%9D%97%9C-%F0%9D%98%84%F0%9D%97%AE%F0%9D%98%80-%F0%9D%98%84%F0%9D%97%BF%F0%9D%97%BC%F0%9D%97%BB%F0%9D%97%B4-%F0%9D%97%AE%F0%9D%97%AF%F0%9D%97%BC%F0%9D%98%82%F0%9D%98%81-%F0%9D%97%B5%F0%9D%97%AE%F0%9D%97%B9%F0%9D%97%B9%F0%9D%98%82%F0%9D%97%B0%F0%9D%97%B6%F0%9D%97%BB%F0%9D%97%AE%F0%9D%98%81%F0%9D%97%B6%F0%9D%97%BC%F0%9D%97%BB%F0%9D%98%80-activity-7337238955177746433-cKEC?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAELwLrYBt0Kc-TjVnoLJKLO9z431kaRM3WI&utm_campaign=copy_link)
* Alain Connes’ **Noncommutative Geometry**
* Michael Spivak’s **A Comprehensive Introduction to Differential Geometry**
* Category Theory & Sheaf Cohomology in AI semantics

---

## 📌 Citation / Acknowledgment

> "TorsionNet: Topological Reasoning to Prevent Transformer Hallucinations"
> Authored by: Sukanya Ghosh
> Inspired by foundational ideas in category theory, topology, and emergent AI reasoning.

---

## 📜 License

MIT License — Free for personal and academic use.
