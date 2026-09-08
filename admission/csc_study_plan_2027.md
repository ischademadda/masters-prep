# CSC Study Plan — Master in Software Engineering / Data Science (800-1000 слов)

> **Назначение:** Подача на CSC Type B (Tsinghua, PKU, SJTU, ZJU) на осень 2027. Пишется на английском, 800+ слов.
> **Тема:** From Code-to-Architecture to AI-native Platform Management
> **Программа:** MSc Software Engineering (AI & Service Engineering) / Data Science & Information Technology
> **Автор:** Denis Shtepa, BSc Software Engineering, TPU, 2027

---

## STUDY PLAN

### 1. Introduction & Motivation

The acceleration of code generation by AI agents has created a fundamental contradiction in modern software engineering: we can write code ten times faster, but our understanding of the system as a whole degrades just as quickly. During my internship as a System Analyst at T-Bank, I experienced this firsthand. While development teams adopted Cursor and Copilot, architectural documentation in Confluence fell behind in two weeks, causing AI agents to hallucinate non-existent APIs and break production with cyclic dependencies.

This problem led me to initiate and lead two platform projects that define my academic and professional direction: **archmap** and **Archon**. My goal for a Master's degree in China is to move from building a prototype of an AI-native Source of Truth to researching how platform-scale knowledge graphs can make architecture an executable, self-verifying layer for the entire enterprise. China, as the world leader in large-scale platform engineering and AI-native systems (Tsinghua, PKU, and the Shenzhen ecosystem), is the ideal place to pursue this.

### 2. Academic Background

I am a 4th-year BSc student in Software Engineering at Tomsk Polytechnic University (TPU), Institute of Information Technology. My curriculum has focused on System Design, Distributed Systems, Databases, and Business Analysis. My GPA is [4.X/5.0] and my English level is C1 (IELTS target 7.5).

My academic strength is not purely theoretical but project-driven system analysis. I was selected for the T-Bank Intensive in System Analysis (2026) and promoted to Junior+ after 4 months for shipping production features. My diploma project, **Archon**, is a team R&D effort where I act as Lead System Architect and Product Visionary, responsible for product scope, modular decomposition (17 modules), and 7 Architecture Decision Records (ADRs) that unblocked development before coding began.

### 3. Research & Project Experience

**Archon — AI-native Source of Truth & Enterprise Docs-as-Code Platform (Team of 4, Diploma Project, 2026)**
Archon is a Managed SaaS platform that continuously synchronizes architectural documentation with source code and delivers verified context to engineers and AI agents via Model Context Protocol (MCP), interactive C4 diagrams, and Git Sync PR-bots.

My contributions as Team Lead:
- **System Decomposition:** Designed 17 orthogonal modules grouped into 5 blocks (Showcase, Decision, Brain, Factory, Foundation) and packaged them into 3 deployable services (archon-core-service in Kotlin, archon-ai-service in Python, archon-portal in React) orchestrated by Temporal Polyglot Workflows (ADR-0007).
- **Code-to-Architecture Pipeline:** Formalized Extraction Contract v1.0 and a two-phase hybrid pipeline: deterministic AST parsing (Tree-sitter) + semantic LLM extraction (File Selector Agent that reads only file trees to save 90% tokens, then Architecture Extractor Agent) + Reconciliation with Proof-of-Truth (every graph edge requires evidence_files with file paths and line numbers, otherwise discarded).
- **Knowledge Graph R&D:** Led R&D on PostgreSQL 16 + Apache AGE for multi-tenant Graph-per-Tenant isolation (each tenant = separate PostgreSQL schema via ag_catalog). Validated creation and deletion of 50 isolated tenant graphs without degradation; Impact Analysis traversal at depth 4 in <15ms (NFR <100ms).
- **Delivery Management:** Own the GitHub Projects board (37 tasks, milestones Phase 0 and Phase 1), Docs-as-Code process (AGENTS.md), and all 7 ADRs (ADR-0001 to ADR-0007).

**OmniSearch Engine — On-Premise Multimodal RAG System for Video Archives (Team of 7, 2026)**
A microservice RAG system for semantic search over video archives (Whisper + CLIP + Qdrant).
My role as System Designer: separated Control Plane (Kotlin/Ktor) and Compute Plane (Go/FFmpeg, Python/FastAPI), designed OpenAPI 3.0 contracts, async state machine (UPLOADED -> PROCESSING_MEDIA -> PROCESSING_ML -> READY), and vector storage in Qdrant. The project was adopted by Gazprom Vostok Neft for HSE compliance automation.

**archmap — Automated C4 Documentation Generator (Solo, T-Bank, 2026)**
From a single request "build an architecture map", I initiated, designed (RFC, pipeline, contracts), and prototyped a service that generates LikeC4 diagrams from code via LLM (File Selector + Extractor) and deterministic generators (json_to_likec4.py), orchestrated in n8n with a TiMe-bot for one-click launch. Result: C4 delivery from 1-3 days to 10-15 minutes, onboarding from weeks to hours. Scaled to 4 products (~25 repos), approved by management. This is my key Product Management case.

**CRDT-Engine — Distributed Real-Time Collaborative Engine (Solo Pet Project)**
A Go-based collaborative editing engine with Strong Eventual Consistency. Implemented Fugue Sequence CRDT, LWW-Registers, G-Set/2P-Set, Vector Clocks, and a Hub/Broker-Worker architecture with Redis Pub/Sub and worker pools sharded by document_id.

These projects show a consistent focus: **how to keep system knowledge accurate at platform scale and make it consumable for humans and AI agents alike.**

### 4. Why China & Why This University

I choose China for three reasons:

1.  **Platform Scale:** No country operates platforms at China's scale (WeChat, Alibaba, ByteDance). The challenges of multi-tenancy, polyglot orchestration, and enterprise knowledge graphs that I faced in Archon are solved daily in the Chinese ecosystem. Tsinghua Shenzhen (Data Science & IT) and PKU Software Engineering are at the center of this research.
2.  **AI-native Research:** My interest in MLOps / AI Platform aligns directly with research labs at Tsinghua (Knowledge Engineering, NLP) and PKU (Software Engineering Institute). I want to research how LLM-based extraction can be made provably reliable (my Proof-of-Truth principle) and how vector + graph retrieval (Qdrant + AGE in my projects) can be unified.
3.  **Bridging Engineering and Product:** Chinese master's programs uniquely combine rigorous software engineering with technology management and entrepreneurship — exactly the Platform Product Manager path I aim for.

Specifically, at [Tsinghua/PKU], I am interested in Professor [Name, e.g., Prof. X in Knowledge Graph / Software Architecture Lab] whose work on [e.g., large-scale knowledge graphs / AI for SE] directly relates to my diploma. I have read [1-2 papers of that professor] and see a clear continuation of my Archon work in their lab.

### 5. Study Plan During Master's (2 Years)

**Year 1 — Foundation & Deepening:**
- Complete core courses: Advanced Software Architecture, Distributed Systems, Machine Learning Systems, Knowledge Graph Engineering, Database Systems (Graph DB).
- Improve Chinese to HSK 5 (currently HSK 3 in progress) and achieve academic fluency.
- Join the lab of Prof. [Name] as a research assistant. Replicate and extend Archon's Graph-per-Tenant model to 500+ tenants and publish a comparative study of Apache AGE vs. NebulaGraph/TuGraph for enterprise multi-tenancy.
- Publish one conference paper on "Proof-of-Truth for LLM-based Architecture Extraction".

**Year 2 — Research & Thesis:**
- Thesis topic: **"Executable Architecture-as-Context: A Multi-tenant Knowledge Graph Platform for Zero-Drift Documentation and AI Agent Grounding"** — a direct evolution of Archon, but evaluated on open-source enterprise codebases at scale.
- Internship at a platform team (e.g., Tencent/Bytedance/Alibaba Cloud) to validate the platform PM approach in industry.
- Defend thesis and aim to open-source the core extraction framework.

### 6. Future Plan & Career Goal

After graduation, I plan to work as a **Platform / Technical Product Manager** in an international technology company, building AI-native developer platforms. In the long term, I aim to return to the Russia/CIS region or work in a cross-border context to help enterprises adopt AI-native Source of Truth practices, bridging the gap between rapid AI-assisted development and sustainable architecture governance.

I am ready to contribute my R&D team leadership experience (2 years, 7 people max), production platform experience, and strong system design background to the academic community of [University Name].

---

### Checklist для подачи CSC

- [ ] Адаптируй под каждый вуз: замени [Tsinghua/PKU] и профессора, добавь 1-2 его статьи
- [ ] Уложись в 800-1000 слов, без воды, с метриками (<15ms, 50 tenants, 90% tokens, 4 products/25 repos)
- [ ] Приложи как `Study Plan` в PDF на бланке (подпись, дата)
- [ ] Два рекомендательных письма: одно от научного руководителя ТПУ, второе — от лида из Т-Банка (акцент на archmap)
- [ ] Нотариальный перевод диплома + транскрипт с GPA

### Источники для поиска профессора

- Tsinghua SIGS: https://www.sigs.tsinghua.edu.cn
- PKU Software Engineering: https://www.sei.pku.edu.cn
- Campuschina: http://www.campuschina.org
