# L1 | Data Contracts and State Semantics

## Purpose

L1 defines the **shared data contracts** used across the cognitive architecture.

These contracts provide the **coordination layer** of the system, allowing independent
subsystems to communicate through structured events and snapshots rather than
direct internal dependencies.

In practical terms, L1 is the **event-driven language of the runtime**.

Every process in the system publishes and consumes these contracts to maintain
coherent system behavior.

L1 serves as the **runtime language** that implements the architectural
principles defined in L0.

---

## Design Goals

1. **Process Interoperability**  
   Independent runtime components must communicate without tight coupling.

2. **Schema Evolution**  
   Data structures must be versioned so that the architecture can evolve
   without breaking existing components.

3. **History vs State Separation**  
   Immutable historical facts and mutable runtime state must be clearly distinguished.

4. **Traceability**  
   System behavior must be reconstructible from data contracts alone.

5. **Operational Safety**  
   Safety-relevant metadata must be machine-readable and auditable.

---

## Event-Driven Coordination

The runtime operates as an **event-driven architecture**.

Subsystems do not call each other directly.  
Instead they exchange structured contracts through the event system.

Events form the authoritative history of the system and enable
**event-sourced reconstruction of runtime behavior**.

Subsystem A ──emit──► Event  
│  
▼  
Event Bus  
│  
▼  
Subsystem B ──consume──► Event  


This design provides:

- loose coupling between modules
- recoverability after failures
- full behavioral traceability
- easier debugging and auditing

---

## Core Contract Families

The architecture defines several categories of contracts.

### Event Contracts

Events represent **immutable runtime facts**.

Examples include:

- perception signals
- cognitive decisions
- commitment lifecycle events
- action results

Events form the **historical record** of the system.

Properties:

- append-only
- timestamped
- origin-annotated
- immutable once published

---

### Snapshot Contracts

Snapshots represent the **current system state**.

Examples include:

- current attention focus
- current emotional state
- active commitments
- fatigue and desire levels

Snapshots are **overwritable views** optimized for fast reads.

Events describe *what happened*.  
Snapshots describe *what is currently true*.

---

### Intent Contracts

Intent contracts represent **normalized cognitive units** produced during
perception and reasoning.

An intent captures the system's interpretation of a stimulus or internal drive
in a form that can be evaluated by the decision system.

Typical uses:

- candidate actions
- conversational responses
- exploratory behaviors

---

### Planning Contracts

Planning contracts represent **structured task execution**.

These include:

- commitments
- plan steps
- checkpoints
- execution outcomes

They allow the system to manage long-running tasks, interruptions,
and resumable workflows.

---

### Obligation Contracts

Obligations represent **deferred or resumable work**.

They allow the system to:

- pause tasks
- wait for external feedback
- resume work after interruption
- manage long-horizon commitments

Obligations are essential for maintaining continuity across time.

---

### Body Contracts

Body contracts define how the cognitive system interacts with the environment.

These include:

- action commands
- channel metadata
- security annotations
- action feedback envelopes

They provide the interface between cognition and execution.

---

## Contract Invariants

The following invariants must always hold.

1. **Events Are Immutable**  
   Once emitted, an event cannot be modified.

2. **Contracts Are Versioned**  
   All cross-process payloads carry schema version identifiers.

3. **Action Feedback Is Correlation-Safe**  
   Every action result references the originating action context.

4. **Execution State Is Explicit**  
   Planning and resume states must be encoded explicitly rather than inferred.

5. **Safety Metadata Is Structured**  
   Security-relevant fields must be machine-readable.

---

## State Modeling Principles

State contracts follow several principles:

### Recoverability

State machines must allow recovery after interruption or restart.

### Explicit Transitions

State transitions must be observable and recorded through events.

### Deterministic Resume

Checkpoints must contain enough information for a suspended task
to resume deterministically.

---

## Public Success Criteria

The L1 contract system is considered successful when:

- any subsystem can consume another subsystem's payloads without private assumptions
- schema upgrades remain backward compatible or safely version-gated
- incident analysis can reconstruct decision paths from contracts alone
- runtime coordination remains stable even as subsystems evolve