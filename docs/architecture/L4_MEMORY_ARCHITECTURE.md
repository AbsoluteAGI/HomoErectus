# L4 | Memory Architecture

## Purpose

L4 defines the **memory substrate** of HomoErectus, supporting continuity of experience, retrieval, adaptation, and long-horizon learning.

This layer ensures that cognition is grounded in memory, enabling the agent to:

- retain past outcomes,
- adapt behavior based on experience,
- maintain a coherent self-model,
- learn skills and improve planning.

---

## Layered Memory Model

The memory system is divided into five layers:

| Layer | Description | Key Role |
|-------|-------------|----------|
| **L1 Working Memory** | Short-term, active context | Holds current perception, task states, and recently generated idea seeds; fast, volatile storage |
| **L2 Narrative Memory** | Episodic continuity | Maintains first-person “experience” of the agent, supporting subjective coherence across time |
| **L3 Knowledge Memory** | Structured knowledge | Stores multi-dimensional world knowledge, social relationships, preferences, and causal models |
| **L4 Skill Memory** | Reusable skills | Consolidates repeated successful plans and actions into skill templates for Planner reuse |
| **L5 Identity / Personality Memory** | Stable agent traits | Stores agent self-concept, personality parameters, desires, preferences, and emotion-related hyperparameters |

## Public Implementation Alignment

The active runtime may expose memory through multiple modules and services while preserving the same layered model.

Public-safe examples of aligned surfaces include:

| Architectural layer | Example implementation surface |
|---|---|
| L1 Working Memory | `l1_working` |
| L2 Narrative Memory | `l2_narrative` |
| L3 Knowledge Memory | `l3_norm_query_service`, credential and entity stores |
| L4 Skill Memory | `l4_skill` |
| L5 Identity / Personality Memory | `l5_personality` |
| Cross-layer retrieval | `query_router` |
| Consolidation services | `consolidation`, `consolidation_service`, `gc` |

---

## Consolidation Strategy

Memory evolves through staged consolidation:

1. **Capture L1 activity**  
   - When L1 nears capacity, completed tasks and relevant events are migrated to L2, ensuring **lossless memory release**.

2. **Distill narratives and knowledge**  
   - L2 stores experiences as episodic, first-person narratives.  
   - L3 organizes structured knowledge:  
     - World facts  
     - Social relationships (individuals, organizations, pets)  
     - Agent-relative properties: trust, authority, closeness, preference, and expected behavior based on L5 personality  
     - Causal relationships and patterns  

3. **Promote to Skills and Identity**  
   - Frequently successful sequences in planning and execution abstracted into L4 skill templates.  
   - Patterns affecting long-term behavior update L5 parameters.

### Minimal Durability Rule

For a runtime to claim continuity, the following must survive restart:

- open commitments and obligations
- recent narrative episodes needed for resume
- identity and personality seed state
- active compiled or skill artifacts currently used by planning

Purely ephemeral L1 state is acceptable only in bootstrap-restricted mode.

---

## Retrieval Strategy

Memory retrieval is:

- **Multi-source**: can query across L1–L5 layers
- **Task-aware**: favors relevant, context-specific content
- **Criteria**:
  - **Recency** for operational relevance
  - **Semantic similarity** for concept matching
  - **Structured queries** for entity, relationship, and constraint resolution

Minimum public-safe retrieval surfaces:

- direct lookup by entity or identifier
- recent episode retrieval for resume and explanation
- skill or recipe lookup for planner reuse
- domain-aware query routing when multiple stores are available

---

## Memory Governance

1. **Capacity-aware compaction**  
   - L1 actively releases memory to L2 when nearing capacity  
2. **Attention-marked prioritization**  
   - Experiences flagged by the attention system are retained or prioritized for consolidation  
3. **Separation of transient and durable knowledge**  
   - Temporary working memory vs. long-term narrative and knowledge memory  
4. **Auditability**  
   - Memory transformations are logged and traceable

5. **Explicit Ownership**  
   - Each layer should have a clear write path and promotion rule rather than ad hoc mutation from arbitrary processes

## Write Path Expectations

To avoid layer confusion, the default write responsibilities should be:

| Producer | Primary target |
|---|---|
| perception and execution events | L1 working memory |
| completed or salient episodes | L2 narrative memory |
| extracted facts and relations | L3 knowledge memory |
| repeated successful procedures | L4 skill memory |
| stable preference and identity updates | L5 personality memory |

---

## Public Success Criteria

A well-functioning memory system:

- Preserves useful continuity without runaway storage growth
- Improves future decision-making using past outcomes
- Enables reliable retrieval across operational domains
- Performs consolidation both during active operations and low-activity periods
- Ensures social, world, and skill knowledge are coherent, consistent, and accessible to planning

---

## Notes

- **Social Memory in L3** is critical:  
  - Each social entity (person, organization, pet) has attributes relative to the agent: closeness, trust, authority, preference, and expected behavior based on L5.  
  - Social relationships influence planning, attention, and desire satisfaction.  

- **Skills in L4** are domain- and subdomain-aware, providing templates to the Planner for generating confident plans.

- **Identity in L5** underpins the agent’s behavior across all layers, influencing decision-making, preferences, and emotion-driven dynamics.

- **Integration Across Layers**:  
  - L1 → L2 for episodic consolidation  
  - L2 → L3/L4 for knowledge extraction and skill learning  
  - L3/L4 → Planner and P4/P5 for confident action generation  
  - L5 parameters guide prioritization, desire gaps, and personality-consistent behavior

## Failure and Recovery Expectations

The memory subsystem should degrade gracefully:

- if L3 or L4 is temporarily unavailable, the runtime may continue in restricted mode using L1 and L2
- if durable narrative storage is unavailable, new long-horizon commitments should not be admitted as normal work
- consolidation failures should be retryable and auditable rather than silently skipped
