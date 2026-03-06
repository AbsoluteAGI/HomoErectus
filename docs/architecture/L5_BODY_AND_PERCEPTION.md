# L5 | Body and Perception

## Purpose

L5 defines the **interface between cognition and the external world**.

It specifies how the agent:

- senses its environment,
- executes actions,
- receives feedback,
- and maintains awareness of its own capabilities.

This layer forms the **boundary between mind and world**.

---

# Body Abstraction

The body layer is **capability-based rather than device-specific**.

Instead of binding cognition to concrete hardware or APIs, the architecture defines a
generic **channel abstraction** that represents any sensing or action capability.

Examples of possible channels include:

- text interaction
- file system access
- browser interaction
- audio input/output
- vision or screen capture
- tool execution

This abstraction allows the cognitive system to operate independently from the
underlying execution environment.

---

# Channel Model

Channels are registered and managed through a **channel registry**.

Each channel exposes a standard interface describing:

| Property | Description |
|--------|-------------|
| Channel ID | Unique identifier |
| Capability Type | perception or action |
| Modality | text, audio, vision, structured data |
| Status | active / inactive |
| Policy Level | security classification |

The registry supports:

- capability discovery
- lifecycle management
- policy enforcement
- extensible adapters for local and remote tools

---

# Security Zoning

Execution capabilities are organized into **security zones**.

This allows the agent to interact with tools and environments while enforcing
different trust levels.

| Zone | Description |
|----|-------------|
| Zone 0 | Core system capabilities |
| Zone 1 | Sandbox environment |
| Zone 2 | Host-level access with authorization |
| Zone 3 | Remote services and APIs |

Higher-risk zones require stronger policy checks and may require explicit approval.

---

# Perception Principles

Perception channels transform raw environmental signals into normalized
perception events.

Key principles:

1. **Normalization before cognition**

All input data must be normalized before entering the cognitive pipeline.

2. **Unified perception format**

Different modalities (text, audio, vision) are converted into a shared event
representation.

3. **Temporal ordering**

Perception events preserve timestamps and provenance information.

4. **Feedback through perception**

Action outcomes are observed through perception rather than returned directly.

This maintains architectural consistency with embodied systems.

---

# Action Principles

Actions are executed through registered action channels.

Each action request includes:

- the intended operation
- required capability
- parameters
- originating intent or commitment reference

Execution outcomes are recorded as perception events so that cognition observes
the consequences of its own actions.

This design supports:

- auditability
- causal reasoning
- learning from outcomes

---

# Self-Perception

The agent maintains awareness of its own capabilities through **self-perception**.

Self-perception periodically inspects the available channels and updates the
internal body schema.

When the body configuration changes:

1. a body change event is emitted,
2. the internal body schema is updated,
3. the experience is recorded in narrative memory.

This allows the agent to learn what it can and cannot do.

---

# Public Success Criteria

The body layer is considered successful when:

- new capabilities can be added without modifying cognitive architecture
- perception and action remain symmetric interfaces
- policy boundaries are enforceable and auditable
- feedback from actions is observable through the perception pipeline
- the agent maintains a consistent understanding of its own capabilities