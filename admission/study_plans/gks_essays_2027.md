# GKS-G Мотивационные эссе — KAIST / SNU (на осень 2027)

> **Назначение:** Global Korea Scholarship — Graduate (GKS-G), University Track  
> **Вузы:** KAIST (School of Computing / Graduate School of AI), SNU TEMEP  
> **Формат GKS:** 2 эссе — (1) Personal Statement, (2) Study Plan / Research Proposal + эссе про лидерство (встроено)  
> **Язык:** Английский, каждое ~800-1000 слов. Пишется от первого лица.  
> **Автор:** Denis Shtepa, TPU, Team Lead Team-v3-9-a

---

## Эссе 1: Personal Statement & Motivation (Почему Корея и почему ты)

### 1.1 Self-Introduction

I am Denis Shtepa, a 4th-year Software Engineering student at Tomsk Polytechnic University and Team Lead of the R&D lab Team-v3-9-a (4-7 engineers). For two years I have led our team not as a coder, but as a System Designer and Product Owner — designing architecture, writing RFCs and ADRs, and shipping platforms from zero to production.

My journey started with a contradiction I observed during my internship at T-Bank (Russia's leading tech bank): AI agents like Cursor and Copilot wrote code 10x faster, but architectural documentation in Confluence became obsolete in two weeks, causing those same agents to hallucinate APIs and break production. Instead of accepting this, I initiated **archmap** — an automated C4 documentation generator — and later **Archon**, our diploma project: an AI-native Source of Truth platform.

What defines me is ownership. When a lead asked to "build an architecture map", I did not wait for a detailed spec. I drafted the RFC, designed the LLM + deterministic pipeline, built the prototype in Python, and integrated it with n8n and a TiMe-bot for one-click launch. The result — C4 delivery from 1-3 days to 15 minutes, scaled to 4 products / ~25 repositories — was approved by management. This product mindset, combined with system design, is why I aim to become an International Platform Product Manager.

### 1.2 Why Korea & Why KAIST/SNU

Korea is the global reference for Platform Product Management. Companies like Kakao, Naver, and Samsung operate super-apps and enterprise platforms at a scale and integration depth that does not exist elsewhere. The Korean approach — rigorous engineering (KAIST) combined with technology management (SNU TEMEP) — exactly matches my gap: I know how to design systems, I need to learn how to scale platforms as products.

I choose **KAIST** because its School of Computing bridges systems research and AI-native platforms. Professor [Name, e.g., Prof. X — Software Architecture / Knowledge Systems Lab] works on [e.g., large-scale software architecture analysis], which directly continues my Archon work on Knowledge Graphs (PostgreSQL + Apache AGE, 50 tenants, <15ms traversal). I choose **SNU TEMEP** as my second choice because it is Korea's top program for Technology Management, Economics and Policy — the business side of Platform PM that I lack.

Studying in Korea is not just an academic choice; it is an immersion in a culture that ships fast, iterates relentlessly, and respects both engineering depth and product execution — the same values I built my team on.

### 1.3 Leadership & Team Experience

Leadership for me is making decisions under uncertainty and keeping the team unblocked.

In **Archon**, I led the decomposition of 17 logical modules into 3 deployable services (ADR-0007: Temporal Polyglot Workflows). The team debated for weeks: 17 microservices vs. 3 services. I facilitated the decision by framing it with ADRs: we chose 3 services to reduce operational complexity by 70% while keeping module independence. I authored 7 ADRs that closed 100% of blockers before coding — this is my leadership style: decide in writing, with trade-offs explicit.

Operationally, I run delivery via GitHub Projects (37 tasks, milestones Phase 0/1), Docs-as-Code (AGENTS.md), and weekly product logs. When our LLM extraction hallucinated dependencies, I did not blame the model — I introduced **Proof-of-Truth**: every graph edge must have `evidence_files` with file paths and line numbers, otherwise it is discarded. This cut token waste by 90% and built trust in the system.

My team grew from 2 to 7, and I learned that a lead's job is not to be the best coder, but to make context available. That is the platform PM I want to be.

### 1.4 Why GKS

GKS is not just funding for me — it is a bridge. As a Russian student, opportunities for fully-funded international master's are limited. GKS's support (including the Korean language year) would allow me to focus entirely on research and platform product management, and to contribute back by connecting the Korean platform ecosystem with the CIS region in the future. I am fully committed to learning Korean (target TOPIK 3 during the language year) and to being an active ambassador for GKS.

---

## Эссе 2: Study Plan & Research Proposal (Что будешь делать в магистратуре)

### 2.1 Academic Goals

My goal is to become a **Platform / Technical Product Manager** who can own both the system design and the product strategy of AI-native developer platforms.

At KAIST/SNU I will focus on three pillars:
1.  **Software Architecture at Scale:** Advanced Software Architecture, Distributed Systems, Graph Databases.
2.  **AI Systems:** Machine Learning Systems, Knowledge Graph Engineering, MLOps / LLM Systems.
3.  **Platform Product Management:** Technology Management, Product Strategy, Platform Economics (especially at SNU TEMEP).

### 2.2 Research Proposal — Executable Architecture-as-Context

**Title:** *Executable Architecture-as-Context: A Multi-tenant Knowledge Graph Platform for Zero-Drift Documentation and AI Agent Grounding*

**Background:** My diploma project Archon proved that a Knowledge Graph built from code (AST + LLM) can stay in sync with reality and feed verified context to AI agents via MCP (Model Context Protocol), reducing hallucinations and saving up to 80% tokens. However, our evaluation is limited to 6 reference services and 50 synthetic tenants.

**Research Plan (2 years):**

*Year 1 — Foundation & Validation at Scale:*
- Replicate Archon's Graph-per-Tenant model (PostgreSQL + Apache AGE) and benchmark it against native graph DBs (Neo4j, NebulaGraph, TuGraph) at 500+ tenants. Our current result (<15ms at depth 4) needs validation at scale.
- Extend the two-phase LLM pipeline (File Selector -> Extractor) with a formal hallucination metric. Measure precision/recall of extracted dependencies on 20+ open-source enterprise repositories (e.g., from CNCF).
- Publish one paper at a workshop (e.g., ICSE SEIP or APSEC) on "Proof-of-Truth for LLM-based Architecture Extraction".

*Year 2 — Thesis & Product Validation:*
- Thesis: Build a unified retrieval layer that combines vector search (Qdrant, as in my OmniSearch project) and graph traversal for hybrid Q&A over architecture. Evaluate on real developer tasks: "What is the blast radius of changing this API?"
- Internship at a Korean platform team (Kakao/Naver/Coupang) to validate the Platform PM approach in industry — how platform teams manage ADRs, quality gates, and MCP-like context delivery at scale.
- Open-source the core extraction framework.

**Why this lab:** This directly aligns with Prof. [Name]'s work on [e.g., software architecture recovery / knowledge graphs]. I have read [Paper 1, Paper 2] and see a clear path to contribute my Temporal orchestration and multi-tenant graph experience.

### 2.3 Future Plan After Graduation

Short-term (1-3 years): Work as a Platform / Technical Product Manager in Korea or an international tech company, shipping developer platforms and AI-native tooling.

Long-term: Return to the broader Eurasian ecosystem or work cross-border to help enterprises adopt Zero-Drift practices. I want to be the person who makes architecture an executable context, not a stale Confluence page — a vision I started with archmap and Archon, and want to scale with what I learn in Korea.

I will also contribute to the GKS alumni network, mentoring future applicants from Russia/CIS and sharing my experience in platform product management.

---

### Checklist для подачи GKS

- [ ] Персонализируй под каждый вуз: замени [Prof. Name] и 1-2 статьи, укажи лабораторию
- [ ] Эссе 1 и 2 — не копипаста CSC Study Plan, у GKS другой акцент (лидерство + почему Корея)
- [ ] Два рекомендательных письма: научрук ТПУ + лид из Т-Банка (акцент на archmap как продукт)
- [ ] GPA транскрипт с апостилем, IELTS 6.5+ (цель 7.0)
- [ ] Подача University Track напрямую в KAIST/SNU в феврале-марте 2027 (параллельно с CSC)
- [ ] Медсправка по форме GKS, все доки на английском

### Полезные ссылки

- Study in Korea: https://www.studyinkorea.go.kr
- KAIST Graduate Admissions: https://admission.kaist.ac.kr
- SNU TEMEP: https://temep.snu.ac.kr
