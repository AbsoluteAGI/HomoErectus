# L0 | Existence Model

## Mission

HomoErectus is a **cognitive operating system for persistent artificial agents**.

The goal of the system is not task execution speed, but **coherent behavior across time, context, and evolving environments**.

Agents built on HomoErectus operate as **continuously running cognitive systems**, rather than stateless request–response tools.

---

## System Nature

HomoErectus treats an agent as a **persistent process** with:

- internal motivational state
- bounded attention
- episodic memory
- decision commitments
- embodied interaction with the environment

The system is designed so that **behavior emerges from internal state and accumulated experience**, rather than from externally provided prompts alone.

---

## Core Architecture Idea

The architecture models conscious-like operation through the cooperation of three functional subsystems:

| Subsystem | Role |
|---|---|
| **Attention** | Selects the current cognitive foreground |
| **Commitment** | Decides whether an intent becomes action |
| **Planning** | Converts commitments into executable behavior |

Together these subsystems form the **conscious execution layer** of the agent.

Other subsystems operate continuously in the background to support this layer.

---

## Foundational Principles

### 1. Memory as Substrate
All cognition operates on shared memory structures rather than isolated pipelines.

### 2. Dual Cognitive Pathways
Fast reflexive responses coexist with slower deliberative reasoning.

### 3. Attention as Foreground Control
Attention determines the agent's subjective focus but does not halt background processing.

### 4. Event + State Model
System history is preserved through immutable events while current conditions are represented by snapshots.

### 5. Continuous Operation
The system maintains internal activity even without external requests.

### 6. Safety as Runtime Capability
Governance and safety checks are integrated into the execution layer rather than treated as external filters.

---

## Cognitive Loop

At runtime the system continuously cycles through the following process:

1. **Perception**  
   External and internal signals are collected.

2. **Intent Formation**  
   Signals are normalized into cognitive intents.

3. **Attention Allocation**  
   One item becomes the foreground focus.

4. **Commitment Decision**  
   The system decides whether to act, defer, or decline.

5. **Planning and Execution**  
   Actions are decomposed and executed through available capabilities.

6. **Observation**  
   Outcomes are perceived and evaluated.

7. **Memory Consolidation**  
   Experiences are integrated into long-term memory structures.

---

## Runtime Modes

The system operates in three runtime modes:

| Mode | Description |
|---|---|
| **Awake** | Full cognition and action capability |
| **Sleep** | Memory consolidation and cognitive recompilation |
| **Restricted** | Conservative operation with stronger safety gating |

---

## Public Success Criteria

A successful deployment demonstrates:

- responsive behavior under mixed-latency environments
- coherent decision-making across long time horizons
- explainable reasoning under uncertainty
- safe and auditable action execution
- measurable adaptation from experience

---

## Design Position

HomoErectus is not intended to be:

- a prompt orchestration framework
- a stateless task runner
- a single-model chatbot system

Instead, it provides the **foundational runtime architecture for persistent artificial minds**.