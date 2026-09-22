# Denis Shtepa
## AI/LLM Solutions Architect (Middle)

**Contact:**
- **Phone:** +7 (996) 350-77-95 (preferred)
- **Email:** ischademadda@gmail.com
- **Telegram:** @ischademadda
- **GitHub:** github.com/ischademadda · github.com/teamv39
- **City:** Tomsk, Russia — open to remote, hybrid, and relocation within Asia (Singapore/China/Taiwan/Korea)
- **Citizenship:** Russia

---

### Target Role & Salary
- **Role:** AI/LLM Solutions Architect · AI Product Analyst · Technical PM (AI/LLM)
- **Salary:** negotiable, benchmarked to Singapore/SEA market
- **Format:** remote, hybrid, on-site

---

### Profile

AI/LLM Solutions Architect with 3 years of experience designing production AI-native systems for enterprise clients (T-Bank, Gazpromneft, Meridian AI Labs/Singapore). Full AI-product lifecycle: from business requirements and System Design (C4, ADR) to deployment of LLM-pipelines, RAG-systems, Knowledge Graphs, and MCP-integrations for AI-agents in IDEs.

Key products: **Archon** (AI-native Source of Truth for corporate architecture — platform ecosystem, built with my R&D team), **archmap** (Archon-stack deployment at T-Bank: auto-generated C4 diagrams), **OmniSearch Engine** (multimodal RAG for video archives, deployed at Gazpromneft), **Meridian RAG Pipeline** (enterprise semantic search for SEA corporate clients).

Comfortable speaking both business and engineering: gathering requirements from stakeholders, decomposing tasks, and leading cross-functional teams (Backend, Frontend, ML, QA).

---

### Key Competencies

| Area | Skills |
|---|---|
| **System Design** | C4 (Context/Container/Component), ADR, RFC, Use Cases, Sequence Diagrams, UML, AS-IS / TO-BE |
| **AI/LLM Architecture** | LLM-pipelines (two-phase: deterministic + semantic contours), RAG (Qdrant, pgvector), Knowledge Graph (PostgreSQL + Apache AGE), MCP-integrations for AI-agents |
| **Backend & Data** | PostgreSQL, Redis, Qdrant, Temporal, CI/CD (GitHub Actions), REST/OpenAPI, microservices |
| **Product & Process** | Requirements gathering, NFR, stakeholder management, task decomposition, Agile/Scrum, Docs-as-Code |

---

### Work Experience — 3 years (overlapping roles, summed by focus area)

#### Meridian AI Labs — Enterprise AI Platform (Singapore)
*Singapore · Remote from Tomsk*
**January 2025 — December 2025** (12 months, part-time remote — 20 hrs/week)
**Role:** AI Solutions Engineer (part-time)

AI start-up (seed, $8M) building an LLM-platform for SEA corporate clients: internal knowledge bases, AI-agents for enterprise workflows, semantic search. Part-time remote — parallel with my R&D lab and university studies (TPU).

**Key contributions:**
- Designed and deployed an enterprise RAG-pipeline for semantic search over corporate documentation (English): two-phase extraction (deterministic keyword layer + LLM semantic layer), vector storage in Qdrant, P95 latency under 500ms.
- Built an MCP-server for AI-agents in IDEs (Cursor, Copilot): validated agent context delivery, reduced LLM hallucinations by 85% in code-generation tasks.
- Authored 4 ADRs and RFCs within the team — closed all architectural forks before coding started.
- Documented system architecture with the C4 model; interactive diagrams in Confluence — developer onboarding dropped from 2 weeks to 3 days.
- Cross-functional distributed team: 2 Backend (Singapore), 1 ML (India), 1 PM — myself as system architect.

---

#### T-Bank (formerly Tinkoff)
*Moscow, Russia · Remote*
**April 2026 — August 2026** (5 months)
**Role:** System Analyst (internal grade confirmed: Junior+)

Full-cycle System Analyst focused on System Design: end-to-end solutions spanning multiple teams, from requirements gathering to production release.

**Key results:**
- **archmap** — product author and owner: deployed the Archon-stack sub-system for auto-generation of architecture documentation (C4 diagrams). Initiated and shipped the product from a lead's request: two-phase LLM-parser (File Selector → Extractor) + deterministic generator (Python, CI/CD), n8n orchestration, one-click launch via bot. C4 diagram rendering: from 1–3 days down to 10–15 minutes; architecture onboarding: from weeks down to hours. Approved by leadership, scaling to 4 products (~25 repositories).
- **Cobranding in T-ORD** — designed a full-stack feature from database to frontend, integrating 3 external systems (different API contracts, backward compatibility). All edge cases closed in the spec — development with zero blockers, feature shipped to production, ensures compliance with advertising-marking legislation.
- **BotControl** — full-cycle analysis and comparative evaluation of integration approaches; justified a fast MVP over an expensive integration. Solution in production, bot response conversion rate 50%.
- **Processes** — redesigned on-call runbooks (analyzed ~145 tickets, response time −40%); created a service-documentation template reused by two teams (onboarding from 3 days to 1).

---

#### Team v3.9 — R&D Laboratory (Tomsk, Russia)
*Tomsk · github.com/teamv39*
**September 2024 — Present** (2 years)
**Role:** Founder, Team Lead (4–7 engineers), System Architect

Student R&D laboratory I founded and lead: we design and deploy AI-systems for enterprise clients. My zone — System Design and architecture of all team products, from business requirements to acceptance. Corporate roles (T-Bank, Gazpromneft) held in parallel — with employer knowledge.

**1. Archon — AI-native Source of Truth for corporate architecture** (August 2026 — present, graduation project)
Lead System Architect: designed a platform that continuously syncs architecture documentation with code and delivers verified context to engineers and AI-development agents.
- Designed the "Knowledge Factory" — 17 logical modules (portal, PR-bot, MCP-server, Knowledge Graph, drift detector); authored 7 ADRs — all forks closed before coding started.
- Hybrid Code-to-Architecture pipeline: deterministic AST analysis + two-phase LLM-contour with Proof-of-Truth (every graph edge verified with file/line references) — eliminated hallucinated edges, −90% LLM tokens.
- Multitenant Knowledge Graph on PostgreSQL 16 + Apache AGE: verified 50 isolated tenant graphs, depth-4 traversal <15ms with NFR <100ms.
- Physical topology: 3 polyglot services (Kotlin/Python/React) orchestrated by Temporal Workflows; privacy-by-default (client code lives only in RAM).
- Team of 4 engineers, 37-task tracker, Docs-as-Code process (AGENTS.md).

**2. OmniSearch Engine — multimodal RAG-system for video archives** (January — June 2026) · [github.com/teamv39/OmniSearch-Engine](https://github.com/teamv39/OmniSearch-Engine)
Product Owner and System Analyst: on-premise semantic video-search engine, deployed at a corporate client.
- Designed microservice architecture: Control Plane (Kotlin Ktor) + Compute Plane (Go: FFmpeg/GoCV, Python: Whisper/CLIP), OpenAPI 3.0 contracts, async pipeline with a finite-state machine for video processing.
- Storage: PostgreSQL, Qdrant, S3/MinIO; presigned URLs for safe streaming, CI/CD on GitHub Actions.
- Result: deployed for automating occupational-safety compliance tracking at Gazpromneft facilities; rolling out to high-load business solutions.

**3. WikiLive — collaborative wiki-development system for MTS Tech** (in development)
System Analyst, designed the entire system:
- Frontend (React + Tiptap) under Design Kit; Backend Gateway (Java Spring): business logic, authorization, PostgreSQL, secure proxying to MWS API.
- Sync Engine (Go): WebSockets, binary-delta routing, horizontal scaling via Redis Pub/Sub.
- AI Node (Python FastAPI): MWS GPT gateway, RAG-pipeline, Qdrant.

---

### Education

* **2023 — 2027** — Tomsk Polytechnic University (TPU)
  * Institute of Computer Science and Technology, Software Engineering, Bachelor's (4th year)
* **Courses:** System Analysis Intensive (T-Bank, 2026) · Business Analytics (TPU, 2025) · Umnova Accelerator (TPU, 2024)

---

### Languages

* Russian — Native
* English — C1 (confident with technical documentation and professional correspondence)

---

### About Me

I don't wait for detailed task breakdowns — I explore the context myself and drive the solution to production. Three times led an AI-product from concept to enterprise deployment: archmap (T-Bank), OmniSearch (Gazpromneft), Meridian RAG (SEA clients). Comfortable speaking both business and engineering: gathering stakeholder requirements, decomposing tasks, and leading cross-functional teams (Backend, Frontend, ML, QA).

Looking for a team with complex System Design challenges in AI/LLM: distributed systems, cross-system integrations, enterprise AI-agents, Knowledge Graphs.