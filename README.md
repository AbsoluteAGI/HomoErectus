# HomoErectus

**HomoErectus** is a **cognitive operating system for persistent artificial agents**, designed to move beyond traditional tool-executing AI into agents with **first-person narrative continuity, autonomous ideation, and adaptive learning**.

This system provides the foundation for building **Artificial Minds** that perceive, plan, act, and learn over time.

This public repository currently serves two roles:

- a **public whitepaper** for the layered cognitive architecture
- an **early runtime skeleton** aligned with the active private implementation

## Current Status

The full runtime is in the final debugging and stabilization phase.

The complete public code release is **coming soon**.  
Until then, this repository exposes the architecture documents and a minimal public skeleton that reflects the intended system shape.

---

## Architecture Overview

HomoErectus is organized as a layered **Agent Cognitive OS**:

```text
L8  Initialization / Birth
L7  Sleep / Cognitive Compiler
L6  Motivation System
L5  Body & Perception
L4  Memory Architecture
L3  Cognitive Pipeline
L2  Runtime Processes
L1  Data Contracts
L0  Existence Model
```

Each layer defines a specific aspect of cognition:

- **L0 Existence Model** – Agent as a continuously running, self-motivated entity.
- **L1 Data Contracts** – Shared event, snapshot, intent, and obligation protocols.
- **L2 Process Architecture** – Runtime process decomposition and dual cognitive paths.
- **L3 Cognitive Pipeline** – Integration of perception, attention, commitment, planning, execution, and feedback.
- **L4 Memory Architecture** – L1 working memory, L2 narrative memory, L3 knowledge memory, L4 skill memory, L5 personality memory.
- **L5 Body & Perception** – Channel abstraction for action and sensing, security zones, self-perception.
- **L6 Desire, Emotion & Preference** – Motivational dynamics that drive attention, planning, and behavior.
- **L7 Sleep & Cognitive Compilation** – Offline optimization for memory consolidation, pattern extraction, and skill refinement.
- **L8 Initialization & Birth** – Staged activation of a coherent operating agent.

---

## Canonical Cognitive Loop

At runtime, the agent follows a **closed-loop cognitive cycle**:

```text
External stimulus → Body Channel Perception → P1 Perception Fusion → P3 Stimulus Processor
Internal drive    → P2 State Engine → P3.5 Ideation                  |
                                                ↓                    ↓
                                                P4 Attention Scheduler
                                                ↓
                                                P5 Commitment Engine
                                                ↓
                                                Planner
                                                ↓
                                                Executor
                                                ↓
                                                Body Channels → Observation
```

Key principles:

- **Dual Cognitive Paths** – External inputs and internal drives are processed separately but converge at attention.
- **Attention-Centric Execution** – Only one item is foregrounded at a time.
- **Recursive PEOR Execution** – Each commitment is executed via Plan → Execute → Observe → Replan loops, integrating learning and memory.
- **Memory Integration** – Step outcomes are recorded in L2/L3 and distilled into L4 skills for future planning.

---

## Key Features

- **Persistent Self-Aware Agents** – Agents maintain continuous subjective experience.
- **Memory-Driven Learning** – Consolidation from L1 → L2 → L3 → L4 enables skill acquisition and adaptation.
- **Motivationally Guided Behavior** – Desire, emotion, and preference signals modulate attention and decision-making.
- **Recursive PEOR Planning** – Plan–Execute–Observe–Replan loops enable robust long-horizon task execution.
- **Safe and Auditable Execution** – Policy zones, hard blocks, and traceable action feedback.
- **Offline Optimization** – Sleep cycles consolidate memory, compile cognitive patterns, and refine heuristics.
- **Flexible Multi-Modal Interface** – Channels support text, audio, vision, and structured tools.

---

## Getting Started

If you are looking for the full production runtime: it is not fully published here yet.  
This repository currently provides the public architecture and a minimal bootstrap skeleton while the main codebase is in final debugging.

### Prerequisites

- Python >= 3.11
- Optional persistence and UI dependencies live in the active private runtime
- This public repository keeps only a minimal runnable skeleton

### Repository Structure

```text
HomoErectus/
├── README.md
├── CONTRIBUTING.md
├── docs/
│   └── architecture/
├── config/
├── src/
├── tests/
├── docker/
└── dashboard-ui/
```

The public repo intentionally exposes only the minimal shape of the runtime:

- `docs/architecture/` contains the public architecture layers
- `src/` contains a lightweight bootstrap entrypoint and package skeleton
- `config/` contains minimal example runtime configuration
- `tests/` contains smoke-level checks for the public skeleton
- `docker/` and `dashboard-ui/` are placeholders for the broader runtime surface

### Running the Public Skeleton

```bash
# start the public bootstrap
python src/run_agent.py --config config/default.toml

# run the public smoke tests
python -m pytest
```

> Note: The production runtime is still in final debugging in a private repository. A fuller public code release is coming soon. For now, this repository exposes the architecture, naming, and a minimal executable skeleton so contributors can follow the intended system shape without relying on unpublished code.

---

## Documentation

The detailed **Public Whitepaper** is available under:

```text
docs/architecture/
```

Each layer (L0–L8) is documented to explain:

- purpose and scope
- core principles
- interactions with other layers
- public success criteria

---

## Contributing

We welcome contributions from developers and researchers who want to explore **Agent Cognitive OS design**:

- add new skills and domains
- experiment with perception or planning modules
- enhance documentation and diagrams
- share feedback on runtime implementation

Please review the `CONTRIBUTING.md` for guidelines.

---

## License

This project is released under the **Apache License**.

---

## Public Success Criteria

- Agent maintains continuous operation with coherent internal state
- Attention, commitment, and execution states remain consistent
- Memory consolidation supports learning and skill acquisition
- Motivational system influences behavior as expected
- Actions and feedback are auditable and safe
- Sleep and compilation cycles improve runtime efficiency
