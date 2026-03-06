# L2 | Process Architecture

## Purpose

L2 defines the **runtime process architecture** of the system.

While L0 defines the conceptual model and L1 defines the data contracts,
L2 specifies **how cognition is decomposed into cooperating runtime processes**.

The objective of this layer is to ensure that the system can remain:

- responsive to external stimuli
- capable of deep reasoning and planning
- stable under long-running operation
- observable and recoverable under failure

---

## Process Topology

The runtime is composed of the following processes:

| Process | Responsibility |
|------|------|
| **P1 – Perception Fusion** | Collects sensory inputs and normalizes them into perception events |
| **P2 – Internal State Engine** | Maintains desires, emotions, fatigue, and other homeostatic variables |
| **P3 – External Stimulus Processor** | Interprets external stimuli and generates cognitive intents |
| **P3.5 – Ideation and Recycling** | Generates candidate intents from internal state and memory |
| **P4 – Attention Scheduler** | Arbitrates foreground focus and task priority |
| **P5 – Commitment Engine** | Decides whether an intent becomes a commitment |
| **Planner** | Converts commitments into executable plans |
| **Executor** | Executes plan steps and manages checkpoints |
| **Background Services** | Memory consolidation and cognitive recompilation |

These processes together form the **runtime cognitive pipeline**.

---

# Dual Cognitive Paths

The architecture separates cognition into two stimulus paths:

- an **external stimulus path** driven by environmental input
- an **internal drive path** driven by motivational state

Both paths converge at the **Attention Scheduler (P4)**.

---

## External Stimulus Path (Environment-Driven)

Responsible for handling incoming signals from the outside world.

Body Channel Perception → P1 → P3 → P4


Flow description:

1. External signals are detected by the **Perception System**.
2. **P1** fuses raw signals into normalized perception events.
3. **P3** interprets stimuli and generates candidate cognitive intents.
4. Intents are forwarded to **P4** for attention arbitration.

Characteristics:

- event-driven
- latency-sensitive
- optimized for responsiveness to users and environment
- does not require internal ideation

---

## Internal Drive Path (Motivation-Driven)

Responsible for generating candidate actions from internal state.

P2 → P3.5 → P4


Flow description:

1. **P2** updates internal state (desires, emotions, fatigue).
2. Internal tension or obligations trigger ideation.
3. **P3.5** generates candidate intents using memory and learned patterns.
4. These intents are sent to **P4** for attention arbitration.

Characteristics:

- asynchronous
- driven by internal motivation rather than stimuli
- not latency-critical
- responsible for autonomous behavior generation

---

# Attention Convergence

Both stimulus paths converge at the **Attention Scheduler (P4)**.

P4 selects **exactly one foreground focus** at any moment.

This selection determines:

- what the agent is currently doing
- which intent receives cognitive resources
- which task enters the conscious decision pipeline

All other intents remain in queues or background evaluation.

---

# Conscious Execution Chain

Once attention grants foreground focus, the system follows a unified execution chain:

P4 → P5 → Planner → Executor → Body Channels


Responsibilities:

| Component | Role |
|------|------|
| **P4 – Attention** | Selects the foreground intent |
| **P5 – Commitment Engine** | Decides commit / defer / decline |
| **Planner** | Decomposes commitments into executable steps |
| **Executor** | Dispatches steps and manages checkpoints |
| **Body Channels** | Execute actions and produce observable outcomes |

Execution results are **not returned directly**.  
They are observed through the perception system and re-enter the cognitive loop.

Body Action → Environment Change → Body Channel Perception → P1


This maintains architectural consistency with embodied systems.

---

# Scheduling Philosophy

The runtime follows four scheduling principles.

### 1. Event-Driven Where Latency Matters

External stimuli are processed through event-driven triggers
to ensure responsive interaction.

### 2. Periodic Where Stability Matters

Internal state updates occur at periodic intervals to maintain
predictable computational cost.

### 3. Asynchronous Where Reasoning Is Expensive

Ideation, planning, and deep reasoning tasks run asynchronously
because they may involve long-running computation.

### 4. Queue Boundaries for Observability

Each process communicates through explicit queues or buses,
which provides clear monitoring points and simplifies debugging.

---

# Coordination Surfaces

Processes interact through several shared infrastructure layers.

### Event Bus

The Event Bus carries **immutable runtime events**.

Examples include:

- perception events
- cognitive decisions
- commitment lifecycle events
- action results

Events form the **authoritative history of the runtime**.

---

### Snapshot Bus

Snapshots expose **current system state** for fast reads.

Examples include:

- attention focus
- emotional state
- active commitments
- fatigue and desire levels

---

### Memory Substrate

Memory provides long-term and short-term context.

All cognitive processes read from and write to memory layers.

---

### Security Policy Layer

All execution requests pass through a security policy layer
that enforces runtime safety constraints.

---

# Reliability Principles

The runtime is designed for long-lived operation.

### Checkpoint-First Execution

Long-running tasks must create checkpoints
to allow safe interruption and recovery.

### Resume-Safe Obligations

Deferred work is represented as obligations,
ensuring tasks can resume after interruption.

### Bounded Retry Behavior

Failures must fall into known classes
with bounded retry strategies.

### Graceful Degradation

Under resource pressure, the system reduces optional work
instead of blocking critical processes.

---

# Public Success Criteria

The process architecture is considered successful when:

- no single slow subsystem blocks the entire runtime
- perception and response paths remain responsive under load
- interrupted tasks can resume with bounded loss
- runtime queues and processes remain observable