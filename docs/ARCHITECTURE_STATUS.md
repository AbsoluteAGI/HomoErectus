# ARCHITECTURE_STATUS

更新时间：2026-03-06  
范围：对当前实现进行分层审计（PEOR/P3/P4/P5/Planner/Executor/Memory/BodyChannel），并对照 `docs/architecture` 与原 `docs/vnext/*` 目标设计。

本文件已合并以下 vNext 文档要点：
- `docs/vnext/ARCHITECTURE_VNEXT.md`
- `docs/vnext/architecture_vnext_20260303.md`

---

## 1) 分层审计结论

### PEOR
- 已实现：
  - Planner/Executor 均有 replan 流程与递归保护。
  - Executor 发布 `PEOR_TELEMETRY` 快照。
- 部分实现：
  - 已有预算/深度守卫，但参数口径是“按规模动态深度 + hard cap（12）”。
- 未实现：
  - 未看到严格固定 `soft_depth=4`、`hard_max=8` 的统一硬约束入口。
- 偏离设计/风险：
  - 终止规则分散在多个模块，容易出现“同任务不同路径”行为差异。

### P3
- 已实现：
  - 外部刺激主链经 `COGNITIVE_INTENT` 输出。
  - 协议字段 `protocol_version/producer_process/attention_judgement_count/lock_retry_count` 已填充。
- 部分实现：
  - 反馈快速放行和普通刺激路径并存，路径复杂度较高。
- 未实现：
  - 无明显硬缺口。
- 偏离设计/风险：
  - 无重大偏离。

### P4
- 已实现：
  - 统一消费 `COGNITIVE_INTENT`。
  - attention lock、retry、三队列 PK、`ATTENTION_GRANT`、`obligation_id/resume_scope` 已落地。
- 部分实现：
  - 三队列模型落地，但与历史兼容逻辑并行，行为边界更复杂。
- 未实现：
  - 无明显硬缺口。
- 偏离设计/风险：
  - 兼容分支增多后，优先级策略调参难度上升。

### P5
- 已实现：
  - EU 驱动决策、TrustGate、hard block + polite refusal。
  - committing queue 快照用于 P4 PK 比较。
- 部分实现：
  - 反馈类 intent 快路径存在，但并未彻底收敛为单路径。
- 未实现：
  - 无明显硬缺口。
- 偏离设计/风险：
  - 快路径与旧分支并存，行为一致性依赖更多回归测试。

### Planner
- 已实现：
  - plan/replan、obligation 队列、task-level/action-level resume 语义。
  - 被动反馈池、反馈就绪恢复、`resume_scope` 上下文传递。
- 部分实现：
  - 仍使用 `ActionDispatch` 做部分 agentic 工具执行并做 perception-loop 桥接。
- 未实现：
  - “统一 ChannelRegistry-only”尚未完全收敛。
- 偏离设计/风险：
  - 同一能力存在双执行入口，导致观测口径与元数据源可能分裂。

### Executor
- 已实现：
  - checkpoint/resume、反馈期望注册、反馈桥接到 `OBLIGATION_FEEDBACK_READY`。
  - ChannelRegistry 主分发路径与反馈回流。
- 部分实现：
  - 仍保留 ActionDispatch fallback/bridge（兼容 legacy/特例通道）。
- 未实现：
  - “仅 ChannelRegistry”未达成。
- 偏离设计/风险：
  - fallback 分支增多，线上问题定位成本高。

### Memory
- 已实现：
  - L1-L5 分层实现与 ConsolidationService（L1->L2/L3 + snapshot refresh）。
  - QueryRouter 跨层并行检索。
- 部分实现：
  - 成功/失败沉淀策略有实现痕迹，但缺少统一强约束协议与统一可观测指标。
- 未实现：
  - 沉淀质量与时延的统一 KPI 看板未见标准化。
- 偏离设计/风险：
  - 多后端依赖导致在弱环境下“设计完整、运行降级”。

### BodyChannel
- 已实现：
  - ChannelRegistry、Security Zone、custodian gate、manifest/mcp adapter、shadow perception。
- 部分实现：
  - 仍有 ActionDispatch 通路（尤其在 Planner/Executor 的兼容逻辑中）。
- 未实现：
  - “唯一动作与反馈元信息源 = ChannelRegistry”未彻底完成。
- 偏离设计/风险：
  - 双通路造成追踪字段不统一，影响审计与 SLA。

---

## 2) 对照 vNext 目标逐条状态

### 已实现
- P3/P3.5 输出统一 `cognitive_intent`，并含协议字段。
- P4 消费统一 intent 并维护判断计数/重试计数。
- P4->Planner 注意力授予包含 `obligation_id/resume_scope`。
- Planner 支持 task-level / action-level 恢复语义。
- P4 三队列 PK（external / p5 queue / planner queue）与单 spotlight 机制已落地。
- TrustGate + polite refusal 行为可用。
- Memory L1-L5 结构与 consolidation 基础链路已运行。
- ChannelRegistry + zone + approval gate 已可用。

### 部分实现
- 反馈链与外部刺激链协议重合度高，但仍有兼容桥接路径。
- 能力不足时“learn/ask/search”策略存在，但跨域策略一致性依赖 Planner 多分支。
- PEOR 自适应中止已具备雏形（预算/深度/重规划），但未统一为 vNext 固定口径。
- 偏好多模态结构已具备，但对 commit 前 EU 与全链放大效应的验收指标未统一。

### 未实现
- vNext 提出的固定参数口径（如 soft_depth=4/hard_max=8）未严格统一执行。
- “ChannelRegistry 成为唯一动作与反馈元信息来源”未完全达成。

### 偏离设计/风险
- 双入口执行（ChannelRegistry + ActionDispatch）造成链路分叉与数据口径漂移风险。
- 递归 PEOR 终止条件不集中，后续调参可能引入行为不稳定。
- 反馈快路径与旧路径并存，回归矩阵规模扩大。

---

## 3) 现状 - 差距 - 下一步

### 现状
- vNext 核心骨架（统一 intent、P4 三队列、双层 obligation、memory 分层、channel zone）已进入可运行状态。

### 差距
- 仍有 legacy 兼容路径未收敛，导致“设计单通路”与“实现双通路”并存。
- PEOR 策略参数与收敛规则未形成单点配置与统一验收口径。

### 下一步（仅文档建议，不改代码）
1. 明确标记 `ActionDispatch` 剩余使用点与下线条件，形成迁移清单。
2. 在架构文档补充“PEOR 参数口径基线”（soft/hard/degrade 条件）与唯一配置来源。
3. 为 feedback-as-intent、obligation 双队列、ChannelRegistry-only 增加统一验收指标定义。
