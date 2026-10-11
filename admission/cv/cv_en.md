# Denis Shtepa — Technical Product Manager (Platform) | System Designer

**Location:** Tomsk, Russia | **Email:** ischademadda@gmail.com | **Telegram:** @ischademadda  
**GitHub:** [github.com/ischademadda](https://github.com/ischademadda) · [github.com/teamv39](https://github.com/teamv39)  
**Languages:** English C1 (IELTS Academic 7.5 target), Russian Native, Chinese HSK (in progress)  
**Education:** BSc Software Engineering, Tomsk Polytechnic University (TPU), Expected 2027 (GPA: 3.93/5.0)  

---

## SUMMARY
Technical Product Manager and System Designer with 2+ years leading an engineering R&D team (4–7 engineers). Shipped 2 production platforms from 0 to 1: **archmap** (adopted for 4 products / 25 microservice repos at T-Bank, reducing C4 architecture delivery from 3 days to 15 mins) and **OmniSearch Engine** (on-premise multimodal RAG video search adopted by Gazprom Vostok Neft). Specialized in Platform Product Management, System Design (C4 / ADR / OpenAPI), and AI-native architecture (LLM pipelines, Knowledge Graphs, MCP). Seeking a Master's degree in Computer Science / Software Engineering to conduct applied systems research.

---

## LEADERSHIP & EXPERIENCE

### Team v3.9 — Applied R&D Lab | Founder, Team Lead & System Designer
*Tomsk, Russia | Sep 2024 — Present (2 years) | Team: 4–7 engineers*

#### 1. Archon — AI-Native Source of Truth & Architecture Platform (Diploma Project)
*Lead System Architect & Product Owner | Kotlin, Python, Temporal, PostgreSQL + Apache AGE, Qdrant, React/LikeC4*
* **Core Product Vision:** Solved architectural drift by designing an automated Knowledge Graph platform that synchronizes C4 architecture with codebases and feeds verified context to AI engineering agents via MCP.
* **Architecture & Delivery:** Decomposed 17 logical modules into 3 polyglot services orchestrated by Temporal Workflows; authored 7 Architecture Decision Records (ADRs) closing 100% of technical blockers before implementation.
* **Deterministic + LLM Pipeline:** Designed a hybrid Code-to-Architecture extraction pipeline: deterministic AST parsing (Tree-sitter) + 2-phase LLM extraction with a strict "Proof-of-Truth" rule (discarding any edge without line-level source code proof), slashing LLM token consumption by 90%.
* **Scalable Graph Storage:** Benchmarked multi-tenant Graph-per-Tenant isolation on PostgreSQL 16 + Apache AGE across 50 schemas: Impact Analysis traversal <15ms at depth 4 (NFR <100ms).

#### 2. OmniSearch Engine — On-Premise Multimodal Video RAG System
*Product Owner & System Designer | Kotlin Ktor, Go (FFmpeg/GoCV), Python (Whisper/CLIP), Qdrant, MinIO S3*
* **System Design:** Architected microservices separating Control Plane (Kotlin Ktor) and Compute Plane (Go worker pool, Python ML nodes). Designed OpenAPI 3.0 contracts and asynchronous media processing finite-state machine.
* **Production Deployment:** Delivered on-premise semantic search over video archives (audio transcription via Whisper + visual frame embeddings via CLIP). Deployed at **Gazprom Vostok Neft** for industrial safety compliance.

---

### T-Bank | System Analyst (Junior+, Full-Cycle System Design)
*Moscow, Russia (Remote) | Apr 2026 — Aug 2026 (5 months)*

* **archmap Platform (Founder & PO):** Initiated and launched an automated C4 architecture diagram generator from scratch. Combined AST extraction, LLMs, and LikeC4 with CI/CD integration. Reduced architecture documentation turnaround from 1–3 days to 15 minutes; approved by management and scaled to 4 products (~25 repositories).
* **Cross-System Integrations:** Designed end-to-end specifications for co-branding features across 3 external systems with backward-compatible REST APIs; eliminated delivery blockers at the specification phase.
* **Operational Optimization:** Refactored on-call runbooks across 145 incidents, reducing response time by 40%.

---

## SKILLS & COMPETENCIES
* **Product & Architecture:** System Design, C4 Model, LikeC4, PlantUML, OpenAPI/REST, ADR/RFC, BPMN, Use Cases, NFR, Impact Analysis.
* **Distributed Systems & AI:** Microservices, Event-Driven Architecture, Temporal, Knowledge Graphs (Apache AGE), Vector Databases (Qdrant), RAG, Model Context Protocol (MCP).
* **Technologies:** Kotlin, Go, Python, PostgreSQL, Redis, Docker, Git.
* **Leadership:** Team Leadership (4–7 engineers), Agile/Scrum, Delivery Management, Stakeholder Communication.
