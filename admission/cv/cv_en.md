# Denis Shtepa — Technical Product Manager (Platform) | System Designer

**Location:** Tomsk, Russia | **Email:** ischademadda@gmail.com | **Telegram:** @ischademadda  
**GitHub:** [github.com/ischademadda](https://github.com/ischademadda) · [github.com/teamv39](https://github.com/teamv39)  
**Languages:** English (IELTS Academic scheduled 5 Dec 2026), Russian Native, Chinese HSK (in progress)  
**Education:** BSc Software Engineering, Tomsk Polytechnic University (TPU), Expected 2027 (GPA: 3.93/5.0)  

---

## SUMMARY
Technical Product Manager and System Designer with 2+ years leading an engineering R&D team (4–7 engineers). Built **archmap** from 0 to 1 at T-Bank (covered about 40 microservice repositories, generating C4 architecture documentation in about 15 minutes per repository); currently leading the design and early implementation of **Archon**, an AI-native architecture knowledge platform (diploma project). Specialized in Platform Product Management, System Design (C4 / ADR / OpenAPI), and AI-native architecture (LLM pipelines, Knowledge Graphs, MCP). Seeking a Master's degree in Computer Science / Software Engineering to conduct applied systems research.

---

## LEADERSHIP & EXPERIENCE

### Team v3.9 — Applied R&D Lab | Founder, Team Lead & System Designer
*Tomsk, Russia | Sep 2024 — Present (2 years) | Team: 4–7 engineers*

#### 1. Archon — AI-Native Source of Truth & Architecture Platform (Diploma Project, in development)
*Lead System Architect & Product Owner | Kotlin, Python, Temporal, PostgreSQL + Apache AGE, Qdrant, React/LikeC4*
* **Core Product Vision:** Addressing architectural drift by designing an automated Knowledge Graph platform that synchronizes C4 architecture with codebases and feeds verified context to AI engineering agents via MCP.
* **Architecture:** Decomposed the system into 17 logical modules packaged as 3 polyglot services orchestrated by Temporal Workflows (ADR-0007); authored 7 ADRs defining core architectural trade-offs (multi-tenancy, packaging, MCP) prior to implementation. Base service skeleton in progress.
* **Deterministic + LLM Pipeline:** Designed a hybrid Code-to-Architecture extraction pipeline: deterministic AST parsing (Tree-sitter) + 2-phase LLM extraction with a strict "Proof-of-Truth" rule (discarding any edge without line-level source code proof), with a File Selector stage designed to minimize LLM token consumption.
* **Scalable Graph Storage:** Selected multi-tenant Graph-per-Tenant isolation on PostgreSQL 16 + Apache AGE (ADR); defined NFR for Impact Analysis traversal (<100ms at depth 4) to be validated in benchmarks.

#### 2. OmniSearch Engine — On-Premise Multimodal Video RAG System (R&D)
*Product Owner & System Designer | Kotlin Ktor, Go (FFmpeg/GoCV), Python (Whisper/CLIP), Qdrant, MinIO S3*
* **System Design:** Architected microservices separating Control Plane (Kotlin Ktor) and Compute Plane (Go worker pool, Python ML nodes). Designed OpenAPI 3.0 contracts and asynchronous media processing finite-state machine.
* **Applied Scenario:** Designed on-premise semantic search over video archives (audio transcription via Whisper + visual frame embeddings via CLIP) for industrial safety monitoring; built a working prototype and demonstrated it live to **Gazprom Vostok Neft** specialists (prototype only, not deployed in production).

#### 3. Archonity — Static Execution-Path Analyzer (TechArena 2026 hackathon, Huawei R&D case)
*Rust, Python, Tree-sitter, local LLM via llama.cpp*
* **Engineering:** Co-developed (team of 3; ~285 of ~590 commits) a static analyzer predicting which methods, calls, remote requests and SQL tables a user scenario touches in the 41-microservice Train Ticket benchmark: deterministic Rust engine, a local LLM that only maps scenario text to endpoints, file-and-line evidence for every predicted edge.

---

### T-Bank | System Analyst (Junior+, Full-Cycle System Design)
*Moscow, Russia (Remote) | Apr 2026 — Aug 2026 (5 months)*

* **archmap Platform (Sole Developer & Owner):** After a platform lead voiced the need for a direction map, built an automated C4 architecture generator solo, aligned with leads. Combined AST extraction, LLMs, and LikeC4 with CI/CD integration. Generated C4 documentation in about 15 minutes per repository; approved by management and scaled to about 40 repositories.
* **Cross-System Integrations:** Designed end-to-end specifications for co-branding features across 3 external systems with backward-compatible REST APIs; eliminated delivery blockers at the specification phase.
* **Operational Optimization:** Refactored on-call runbooks across 145 incidents, reducing response time by 40%.

---

## SKILLS & COMPETENCIES
* **Product & Architecture:** System Design, C4 Model, LikeC4, PlantUML, OpenAPI/REST, ADR/RFC, BPMN, Use Cases, NFR, Impact Analysis.
* **Distributed Systems & AI:** Microservices, Event-Driven Architecture, Temporal, Knowledge Graphs (Apache AGE), Vector Databases (Qdrant), RAG, Model Context Protocol (MCP).
* **Technologies:** Kotlin, Go, Python, PostgreSQL, Redis, Docker, Git.
* **Leadership:** Team Leadership (4–7 engineers), Agile/Scrum, Delivery Management, Stakeholder Communication.
