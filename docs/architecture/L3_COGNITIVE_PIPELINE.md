# L3 | Cognitive Pipeline

## Purpose

L3 defines the **runtime cognitive pipeline**, specifying how perception, internal state, and ideation generate actions.  
This layer governs the flow from stimuli to execution while integrating attention arbitration, commitment decisions, planning, and memory consolidation.

While L2 describes **which processes exist**, L3 describes **how cognition flows across those processes** to form a continuous, closed-loop system.

---

# Canonical Cognitive Paths

The architecture separates cognition into three primary paths:

1. **External Stimulus Path** – handles inputs from the environment and social channels.  
2. **Internal Ideation Path** – generates autonomous intents from internal motivational state.  
3. **Action Feedback Path** – executes plans and integrates outcomes back into memory.

---

## External Stimulus Path

This path processes **signals originating outside the agent**.

Body Channel Perception → P1 (Perception Fusion) → P3 (External Stimulus Processor) → P4 (Attention Scheduler) → P5 → Planner → Executor → Body Channels


Key properties:

- Event-driven, latency-sensitive
- Converts external stimuli into candidate cognitive intents
- Feeds unified attention arbitration at P4
- Supports immediate responsiveness without waiting for internal ideation

---

## Internal Ideation Path

Triggered by **internal state changes** (desire gaps, fatigue, obligations, or unfulfilled tasks).

P2 (Internal State Engine) → P3.5 (Ideation & Recycling) → P4 (Attention Scheduler) → P5 → Planner → Executor → Body Channels


Key properties:

- Asynchronous, not latency-critical
- Generates novel candidate intents from memory-backed reasoning
- Feeds unified attention arbitration at P4
- Enables autonomous behavior and goal-driven exploration

---

## Convergence: Attention & Execution

Both paths converge at **P4 Attention Scheduler**, which selects exactly **one foreground focus** at a time.  

The selected intent proceeds through the **conscious execution chain**:

P4 (Attention) → P5 (Commitment Engine) → Planner → Executor → Body Channels


- **P5** decides commit / defer / decline
- **Planner** decomposes commitments into executable steps
- **Executor** dispatches steps and manages checkpoints
- **Body Channels** perform actions in the environment
- Execution results are re-observed via Perception to feed memory layers

---

## Commitment Execution: Recursive PEOR Process with Memory Integration

Each **commitment** is executed via a **recursive Plan-Execute-Observe-Replan (PEOR) loop**, integrating learning and memory at every step.

## Public Execution Contract

Even in a minimal public runtime, each commitment should expose these execution surfaces:

| Surface | Purpose |
|---|---|
| `intent_id` | The normalized candidate selected by P4 |
| `commitment_id` | The durable execution handle created by P5 |
| `plan_id` | The current executable plan or plan revision |
| `step_id` | The currently dispatched plan step |
| `checkpoint_id` | The latest resume-safe checkpoint |
| `outcome` | Structured success, divergence, defer, or failure result |

This contract makes PEOR observable without depending on any specific planner implementation.

### Step-by-Step Procedure

1. **Domain Evaluation**
   - Check if the relevant domain and subdomain exist in L3.
   - Determine if existing `skill.md` templates can be applied.

2. **Plan Generation**
   - If a template exists → use as plan blueprint.
   - Else → query an available reasoning component for a confident plan.
   - If no confident plan → trigger learning or consulting subroutine.
   - Fallback → generate a best-effort exploratory plan.

3. **Schema Validation**
   - Hard validate and auto-normalize each step according to L1/L2 contracts.

4. **Execution**
   - Dispatch steps via **Executor → Body Channels**.

5. **Feedback Acquisition**
   - Observe outcomes through perception channels.
   - Capture success or failure of each step.

6. **Feedback Analysis**
   - Compare outcomes with expected results.

7. **Adaptive Replanning**
   - Step succeeds as planned → proceed.
   - Step succeeds but diverges → locally replan subsequent steps, record deviation.
   - Multiple local replans → trigger layer-level PEOR replanning, record iteration.
   - Step fails:
     - Single action → retry and record failure.
     - Nested step → replan this step including subtasks.
     - Repeated failures → escalate to layer-level failure, propagate feedback to parent.

8. **Memory Integration**
   - Step outcomes (success or failure) recorded in **L2 Narrative Memory**.
   - Facts extracted to **L3 Knowledge Memory** (causal chains, facts, preferences).
   - Repeated successful paths are abstracted into **L4 Skill Memory**, building reusable skill templates with proficiency metrics.

9. **Completion**
   - Commitment completes once all steps succeed or are resolved through replanning.
   - All execution, replanning, success, and failure events are recorded for learning and pattern extraction.

### Notes

- Recursive PEOR enables nested subtasks to repeat the loop.
- Learning updates can modify L3/L4 or trigger plan augmentation.
- Confidence-based planning: lower-confidence steps invoke additional learning or exploratory execution.

### Resume and Divergence Rules

- a plan revision must produce a new `plan_id` while preserving the same `commitment_id`
- local replans should preserve parent intent context whenever possible
- divergence should be recorded even when the final outcome is successful
- repeated orphan feedback must be classified and surfaced rather than silently dropped

---

## Intent Normalization

All candidate behaviors entering attention arbitration are normalized into a unified **intent format**.  
This allows attention and commitment to process heterogeneous candidates consistently.

At minimum, an intent should expose:

- source path: external, internal, or recycled
- actor or channel origin
- semantic goal or requested operation
- urgency and expected utility estimates
- policy and capability hints
- references to any triggering event, obligation, or social entity

---

## Attention-Centric Design

Attention (P4) is the **foreground selector**:

- Only one foreground focus at a time
- Background candidates continue to be processed
- Switching incurs cost
- Selection considers urgency, expected utility, commitment alignment, and switching cost

---

## Commitment Semantics

After attention selection, P5 evaluates each candidate:

| Outcome | Meaning |
|---|---|
| Commit | Convert intent to actionable commitment |
| Defer | Keep intent pending for future evaluation |
| Decline | Reject due to constraints or policy |

---

## Planning and Execution

Once committed, the pipeline proceeds:

Commitment → Planner → Executor → Body Channels


Planner:

- decomposes commitments into structured plans
- performs replanning when conditions change
- manages dependencies

Executor:

- dispatches actions to Body Channels
- tracks checkpoints
- coordinates feedback and resume behavior

Implementation note:

The runtime may split planning and execution across multiple modules, but the architectural boundary should remain visible in logs, events, and tests.

---

## Feedback and Resume

Execution results are fed back into **L1/L2/L3**:

- Task-level and action-level resumes are explicit
- Deviations and failures update memory
- Successful repeated paths contribute to L4 Skill Memory

This ensures:

- Safe replan loops
- Continuous learning
- Traceable decision paths

### Feedback Hygiene

To keep the loop stable, the runtime should explicitly classify:

- expected feedback matched to an active step
- late feedback matched to a closed step
- orphan feedback with no active correlation
- self-perception updates caused by body or capability changes

These distinctions are especially important for long-running and partially concurrent execution.

---

## Cognitive Quality Principles

1. Unified intent protocol
2. Deterministic arbitration
3. Explainable decisions
4. Feedback-driven replanning
5. Bounded recursion and budget control

---

## Public Success Criteria

- External and internal cognition share a consistent protocol
- Attention, commitment, and execution states remain coherent
- Feedback triggers safe targeted replan or resume
- Complex tasks converge without unbounded recursion
