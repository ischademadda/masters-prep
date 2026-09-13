# CSC Study Plan — персонализированные версии (Tsinghua / PKU)

> **Дата:** 11.09.2026
> **Формат:** каждая версия — самостоятельный документ 850-950 слов на английском, экспортировать в PDF отдельно (подпись + дата). Подавать как Study Plan в заявку CSC Type B.
> **Версия A:** Tsinghua SIGS — Data Science and Information Technology, Prof. Zheng Haitao (первая программа в заявке Tsinghua; вторая указывается по правилам их портала).
> **Версия B:** PKU — MSc Software Engineering (AI & Service Engineering), Prof. Xuanzhe Liu.
> **Публикации профессоров проверены** (см. `professors_shortlist_2027.md`); если в письме профессор укажет другую свою свежую работу — подставь её вместо указанной.
> **Мастер-шаблон** (нейтральный, для SJTU/ZJU и других): `csc_study_plan_2027.md`.

---

# ВЕРСИЯ A — Tsinghua SIGS (Prof. Zheng Haitao)

### STUDY PLAN — MSc in Data Science and Information Technology, Tsinghua Shenzhen International Graduate School

**Applicant:** Denis Shtepa | BSc Software Engineering, Tomsk Polytechnic University, 2027

### 1. Introduction and Motivation

The acceleration of code generation by AI agents has created a fundamental contradiction in modern software engineering: we can write code ten times faster, but our understanding of the system as a whole degrades just as quickly. During my internship as a System Analyst at T-Bank, I experienced this firsthand. Development teams adopted Cursor and Copilot within months, yet architectural documentation fell two weeks behind — and the same agents that wrote the code began hallucinating non-existent APIs and introducing cyclic dependencies into production.

This problem led me to initiate and lead two platform projects that define my academic direction: archmap and Archon. My goal for the Master's program at Tsinghua SIGS is to move from building a prototype of an AI-native Source of Truth to researching how platform-scale knowledge graphs can make architecture an executable, self-verifying layer for the enterprise. The Shenzhen ecosystem around SIGS — the densest concentration of platform-scale engineering in the world — is the ideal laboratory for this research.

### 2. Academic Background

I am a fourth-year BSc student in Software Engineering at Tomsk Polytechnic University (TPU). My curriculum centers on System Design, Distributed Systems, Databases, and Business Analysis; my GPA is 3.93/5.0 (projected 4.0+ by graduation) and my English is C1. My academic strength is project-driven system analysis: I was selected for the T-Bank Intensive in System Analysis (2026) and promoted to Junior+ after four months for shipping production features. My diploma project, Archon, is a team R&D effort in which I serve as Lead System Architect and Product Owner — responsible for product vision, the decomposition of 17 modules into 3 deployable services, and seven Architecture Decision Records that closed all blockers before coding began.

### 3. Research and Project Experience

**Archon — AI-native Source of Truth and Docs-as-Code platform (team of 4, diploma project, 2026).** Archon keeps architectural knowledge synchronized with source code and serves verified context to engineers and AI agents via Model Context Protocol (MCP), interactive C4 diagrams, and Git-sync PR bots. My contributions: (1) the Code-to-Architecture pipeline — deterministic AST parsing (Tree-sitter) combined with two-phase LLM extraction, where a File Selector agent reads only file trees (saving 90% of tokens) and every extracted graph edge must present evidence_files with file paths and line numbers or is discarded — the "Proof-of-Truth" rule; (2) multi-tenant Knowledge Graph R&D — PostgreSQL 16 with Apache AGE in a Graph-per-Tenant design (each tenant an isolated schema), validated on 50 tenants with impact-analysis traversal under 15ms at depth 4 against a 100ms NFR; (3) delivery management of 37 tasks across two milestones.

**OmniSearch Engine — on-premise multimodal RAG for video archives (team of 7).** Semantic search over video archives (Whisper + CLIP + Qdrant) with Control Plane (Kotlin/Ktor) separated from Compute Plane (Go/FFmpeg, Python), OpenAPI 3.0 contracts, and an asynchronous state machine. Adopted by Gazprom Neft for HSE compliance automation.

**archmap — automated C4 documentation generator (solo, T-Bank).** An LLM + deterministic pipeline generating LikeC4 diagrams from code; cut C4 delivery from 1–3 days to 10–15 minutes and was adopted for 4 products (~25 repositories).

**CRDT-Engine — distributed collaborative editing (solo).** Fugue sequence CRDT, LWW-registers, vector clocks, and a Redis Pub/Sub broker-worker architecture.

### 4. Why Tsinghua SIGS — and the Knowledge Engineering Group

I choose Tsinghua SIGS for three reasons. First, platform scale: the questions my diploma project raises — multi-tenancy, polyglot orchestration, enterprise knowledge graphs — are solved daily at scale in the Shenzhen ecosystem, and SIGS sits at its center. Second, the research direction of Prof. Zheng Haitao's Knowledge Engineering group is the direct continuation of my work. His research on knowledge graph completion (TKDE) addresses exactly what Archon faces at scale: how a graph stays truthful and complete when populated by imperfect, LLM-assisted extraction. His work on parameter-efficient fine-tuning (Nature Machine Intelligence, 2023) and OpenPrompt (ACL 2022) describes the machinery I would apply to make my Extractor agent cheaper and more reliable. And RLHF-V (CVPR 2024) formalizes alignment of generative models with human feedback — the same class of grounding constraint I implemented as an engineering rule with Proof-of-Truth. Studying evidence-grounded alignment and graph completion together, in one group, is exactly the research transition I seek. Third, SIGS's Data Science and Information Technology program combines rigorous systems research with the industrial immersion of Shenzhen — matching my trajectory from system builder to platform researcher.

### 5. Study Plan During the Master's (2 Years)

**Year 1 — Foundations and validation at scale.** I will join the Knowledge Engineering group as a research assistant from the first semester. My first research goal is to scale Archon's Graph-per-Tenant model from 50 to 500+ tenants and benchmark Apache AGE against native graph databases (NebulaGraph, TuGraph) for enterprise multi-tenancy — publishing the comparison as a first paper. In parallel, I will formalize the Proof-of-Truth rule into a measurable hallucination metric: precision and recall of extracted dependencies evaluated on 20+ large open-source codebases (CNCF landscape). Coursework: Knowledge Graph Engineering, Machine Learning Systems, Distributed Systems, Database Systems. I will also continue Chinese (HSK 3 in progress, targeting HSK 4–5 for academic fluency).

**Year 2 — Thesis and industrial validation.** Thesis topic: "Executable Architecture-as-Context: A Multi-tenant Knowledge Graph Platform for Zero-Drift Documentation and AI Agent Grounding" — evaluating the Archon approach on real enterprise codebases at scale. I plan a platform-team internship in Shenzhen (Tencent, Huawei, or ByteDance) to validate the approach in industry, and to open-source the core extraction framework.

### 6. Future Plan

After graduation I aim to work as a Platform / Technical Product Manager building AI-native developer platforms, and in the long term to help enterprises in the Russia/CIS region adopt Zero-Drift architecture governance — bridging rapid AI-assisted development and sustainable platform engineering. I bring to SIGS two years of R&D team leadership, two shipped production platforms, and a research direction already validated at prototype scale.

---
*(~920 слов)*

---

# ВЕРСИЯ B — PKU SEI (Prof. Xuanzhe Liu)

### STUDY PLAN — MSc in Software Engineering (AI & Service Engineering), Peking University

**Applicant:** Denis Shtepa | BSc Software Engineering, Tomsk Polytechnic University, 2027

### 1. Introduction and Motivation

The acceleration of code generation by AI agents has created a fundamental contradiction in modern software engineering: we can write code ten times faster, but our understanding of the system as a whole degrades just as quickly. During my internship as a System Analyst at T-Bank, I experienced this firsthand. Development teams adopted Cursor and Copilot within months, yet architectural documentation fell two weeks behind — and the same agents that wrote the code began hallucinating non-existent APIs and introducing cyclic dependencies into production.

My answer was to build the missing layer: archmap, an automated documentation generator, and then Archon — an AI-native Source of Truth platform that grounds agents in verified architecture. But building this platform convinced me that its central problem is not in the application layer at all. It is a systems problem: agent traffic over knowledge graphs and vector stores is a new, under-served LLM-serving workload. PKU's Software Engineering Institute, where this serving layer is being invented, is the ideal place to pursue it.

### 2. Academic Background

I am a fourth-year BSc student in Software Engineering at Tomsk Polytechnic University (TPU). My curriculum centers on System Design, Distributed Systems, Databases, and Business Analysis; my GPA is 3.93/5.0 (projected 4.0+ by graduation) and my English is C1. I was selected for the T-Bank Intensive in System Analysis (2026) and promoted to Junior+ after four months for shipping production features. My diploma project, Archon, is a team R&D effort in which I serve as Lead System Architect and Product Owner — responsible for product vision, the decomposition of 17 modules into 3 deployable services orchestrated by Temporal workflows, and seven Architecture Decision Records that closed all blockers before coding began.

### 3. Research and Project Experience

**Archon — AI-native Source of Truth platform (team of 4, diploma project, 2026).** Archon serves verified architectural context to engineering AI agents via MCP, C4 diagrams, and Git-sync bots. My contributions: (1) the extraction pipeline — deterministic AST parsing (Tree-sitter) plus two-phase LLM extraction with a "Proof-of-Truth" rule (every graph edge must present evidence_files or is discarded; File Selector agent reads only file trees, saving 90% of tokens); (2) the storage layer — a multi-tenant Knowledge Graph on PostgreSQL 16 + Apache AGE (50 isolated tenant schemas, impact-analysis traversal <15ms at depth 4); (3) delivery management of a 37-task board across two milestones. The platform's distinctive workload — many agents issuing recurring, overlapping context queries against graph+vector backends — is precisely what motivates my proposed research below.

**OmniSearch Engine — multimodal RAG for video archives (team of 7).** Whisper + CLIP + Qdrant over a Control/Compute plane split (Kotlin/Ktor vs Go+Python), OpenAPI 3.0 contracts, asynchronous processing state machine; adopted by Gazprom Neft for HSE compliance automation.

**archmap — automated C4 generator (solo, T-Bank).** LLM + deterministic pipeline; C4 delivery from 1–3 days to 10–15 minutes; adopted for 4 products (~25 repositories).

**CRDT-Engine — distributed collaborative editing (solo).** Fugue CRDT, vector clocks, Redis Pub/Sub broker-worker architecture.

### 4. Why PKU SEI — and Prof. Xuanzhe Liu's Group

My platform sits directly on top of the research agenda of Prof. Xuanzhe Liu's group. RAGCache (ACM TOCS 2026) rethinks serving economics for RAG-heavy workloads through knowledge-cache-aware scheduling — Archon's agent traffic is exactly such a workload. Pythia (2026) pioneers agent-native LLM serving, the serving model my MCP agents implicitly assume. BAMAS (AAAI 2026) formalizes budget-aware orchestration of multi-agent systems — today I handle my File Selector/Extractor budget with ad-hoc heuristics that BAMAS-style formulation would replace. FastServe (NSDI 2026) and MegaScale-MoE (EuroSys 2026) cover the latency and training-scale ends of the same stack. I know of no other institute where both sides of my question — the agent-context platform above and the serving infrastructure below — are researched in the same place. My proposed direction is their co-design: what should a "context-serving tier" between persistent knowledge graphs, vector stores, and application agents look like, and how must the serving stack change to support it.

### 5. Study Plan During the Master's (2 Years)

**Year 1 — Characterization and prototyping.** As a research assistant in the group from the first semester, I will first characterize context-access patterns of MCP agents over combined graph and vector retrieval, using traces from Archon's 50-tenant deployment: query mix, reuse, and locality of agent context requests. On that basis I will prototype a context-serving tier — RAGCache-style caching applied to graph-traversal results — and measure latency, token cost, and cache hit rates against the naive pipeline. In parallel, I will replace my ad-hoc extraction budgeting with a formal BAMAS-style budget allocator and quantify the difference. Target output: one workshop or conference paper (ASE/ICSE or a systems venue). Coursework: Advanced Software Architecture, LLM Systems, Distributed Systems. Chinese: continuing from HSK 3 toward HSK 4–5.

**Year 2 — Thesis and industrial validation.** Thesis: "Executable Architecture-as-Context: Co-designing Agent-Context Platforms with LLM Serving for Zero-Drift Documentation" — evaluated on 20+ open-source enterprise codebases and real agent traces. I plan an internship on a platform/serving team (ByteDance, Tencent, or Alibaba Cloud) and to open-source the extraction and context-serving framework.

### 6. Future Plan

After graduation I aim to work as a Platform / Technical Product Manager building AI-native developer platforms, in the long term bringing Zero-Drift architecture practices to enterprises in the Russia/CIS region. I bring to SEI two years of R&D team leadership, two production platforms, and a research question my diploma project has already made concrete: agent context is a serving workload, and it deserves a serving-tier answer.

---
*(~900 слов)*

---

## Чек-лист экспорта

- [ ] Экспортировать КАЖДУЮ версию в отдельный PDF (название файла: `StudyPlan_Tsinghua_Shtepa.pdf` / `StudyPlan_PKU_Shtepa.pdf`)
- [ ] Версия A: убедиться, что программа в заявке Tsinghua = Data Science and Information Technology (первый выбор)
- [ ] Если Zheng Haitao / Xuanzhe Liu ответят на письмо и упомянут другую свою работу — заменить упомянутую публикацию на неё (только 1 замена, не ломать структуру)
- [ ] Дата + подпись в конце PDF (требование CSC-заявки Tsinghua)
- [ ] Для SJTU/ZJU — адаптировать мастер-шаблон `csc_study_plan_2027.md` по той же схеме (раздел 4 = профессор + его работы; раздел 5 = лаборатория) — сделать, когда выберешься с волной писем
