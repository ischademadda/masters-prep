# Драфты писем профессорам — Fall 2027 (волны 1-2 + SJTU/ZJU)

> **Дата:** 11.09.2026
> **Автор:** Денис Штэпа (отправка с ischademadda@gmail.com)
> **Правила отправки:** по одному письму на вуз — КРОМЕ SJTU/ZJU: там два письма одновременно оправданы (acceptance letter нужен до подачи ~15.12, время дорого; пиши сначала Lu Chen + Gu параллельно — разные лаборатории X-LANCE/LLMSE). Будни, утро по местному времени вуза. Приложения: CV (1 стр., PDF) + ссылка на GitHub Archon.
> **Данные профессоров и публикации:** `professors_shortlist_2027.md`.
> **Тема письма (общая):** `Prospective Master's Student Fall 2027 — AI-native Architecture (Archon: KG + LLM + MCP)`

---

## Волна 1 (СЕЙЧАС — критично для CSC Type B, дедлайн mid-Dec)

### 1.1 Zheng Haitao — Tsinghua SIGS (zheng.haitao@sz.tsinghua.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — Knowledge Graph Grounding for AI Agents (Archon)

```
Dear Professor Zheng,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia) and Team Lead of our R&D lab. I am writing to ask whether you would consider supervising a master's student for Fall 2027, as I plan to apply to the Data Science and Information Technology program at Tsinghua SIGS (CSC scholarship).

My diploma project, Archon, is an AI-native Source of Truth platform that keeps architectural knowledge synchronized with code and delivers verified context to AI agents via MCP. Its core is a multi-tenant Knowledge Graph on PostgreSQL 16 + Apache AGE (50 isolated tenant schemas, impact-analysis traversal <15ms at depth 4) populated by a hybrid pipeline: deterministic AST parsing (Tree-sitter) plus two-phase LLM extraction with a "Proof-of-Truth" rule — every graph edge must carry evidence_files with file paths and line numbers, otherwise it is discarded. This cut LLM token consumption by 90% while keeping extraction verifiable.

I have read your work on knowledge graph completion (TKDE) and RLHF-V (CVPR 2024), and I see a direct continuation of my interests: my Proof-of-Truth rule is essentially a grounding constraint on LLM output, and scaling it from 50 to 500+ tenants raises exactly the completion-and-consistency questions your group studies. Separately, I shipped archmap, an LLM-based C4 diagram generator adopted for 4 products (~25 repos) at T-Bank, and OmniSearch, a multimodal RAG video-search system (Whisper/CLIP/Qdrant) deployed by Gazprom Neft.

My CV and a one-page research summary are attached. I would be grateful for a brief reply on whether my profile fits your lab's plans for Fall 2027 — and whether you would be open to a short call.

Thank you for your time.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: KG completion ↔ AGE-граф + RLHF-V ↔ grounding LLM-вывода. 190 слов — норм.*

---

### 1.2 Xuanzhe Liu — PKU SEI (liuxuanzhe@pku.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — MCP Agent Context on Top of LLM Serving (Archon)

```
Dear Professor Liu,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), Team Lead of our R&D lab. I plan to apply to the MSc Software Engineering program at PKU for Fall 2027 (CSC scholarship) and would be honored to work in your group.

My diploma project, Archon, is an AI-native Source of Truth platform for enterprise architecture. Its core is a multi-tenant Knowledge Graph (PostgreSQL + Apache AGE) fed by a hybrid pipeline — deterministic AST parsing plus two-phase LLM extraction where a File Selector agent reads only file trees (90% token savings) and every extracted edge must present evidence_files, or it is discarded. The graph is then served to engineering AI agents through MCP: agents ask "what breaks if I change this API" and get traversal-backed answers (<15ms at depth 4) instead of hallucinating from stale Confluence pages.

Your work is the natural next layer under this system: RAGCache (TOCS 2026) and Pythia address exactly the serving economics of RAG-heavy, agent-native workloads that Archon pushes onto the infrastructure, and BAMAS (AAAI 2026) formalizes the multi-agent budget allocation I currently handle with ad-hoc heuristics. I would love to research how agent-context platforms like Archon should co-design with the LLM serving stack — e.g., what a "context-serving tier" between vector stores and application agents should look like.

Previously I shipped archmap (LLM-based C4 generation, 4 products/~25 repos at T-Bank) and OmniSearch (multimodal RAG: Whisper/CLIP/Qdrant, Control/Compute plane split).

My CV is attached. Would my profile fit your lab for Fall 2027? I would gladly schedule a call at your convenience.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: его RAGCache/Pythia/BAMAS = системный слой ПОД Archon → «co-design platform + serving». Самый сильный research-мачч.*

---

## Волна 2 (конец сентября)

### 2.1 Shin Yoo — KAIST SoC (shin.yoo@kaist.ac.kr)

**Subject:** Prospective MS Student Fall 2027 — Verifiable LLM Extraction for SE (Proof-of-Truth)

```
Dear Professor Yoo,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), planning to apply to KAIST's School of Computing for Fall 2027 (via GKS and the regular track). May I ask whether you would consider supervising a master's student?

Your COSMosFL work on LLM fault localization (ICSE 2025) and autonomous testing agents speaks directly to a problem I have been engineering around: making LLM output about code verifiable. In my diploma project Archon — an AI-native Source of Truth platform — the Knowledge Graph (PostgreSQL + Apache AGE) is populated by hybrid extraction (deterministic AST + two-phase LLM), and every edge must carry evidence_files with file paths and line numbers or it is rejected ("Proof-of-Truth"). This reduced token waste by 90% and, more importantly, made hallucinated dependencies structurally impossible in the graph. I see your research agenda — LLMs for SE with verifiable grounding — as the scientific frame my engineering rule deserves: I want to evaluate it as a testing/verification mechanism, not just a data-quality heuristic.

I also lead a 4-7 person lab (two shipped platforms: archmap, an LLM C4-generator adopted at T-Bank for ~25 repos, and OmniSearch, a multimodal RAG system), so RA contributions in your lab would come with real delivery experience.

Would my profile fit your lab's Fall 2027 plans? My CV is attached; I am happy to share the Archon technical report on request.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: Proof-of-Truth как верификация LLM-вывода — его повестка. ⚠️ KAIST-гайд рекомендует найти advisor до подачи — это письмо важнее остальных из волны 2.*

---

### 2.2 Jerry Chou — NTHU, директор IMPISA/IMS (jchou@cs.nthu.edu.tw)

**Subject:** Prospective MS Student Fall 2027 — IMPISA (multi-tenant platform, resource management)

```
Dear Professor Chou,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia). I plan to apply to the International Master Program in Information Systems and Applications for Fall 2027 (via TaiwanICDF and MOE scholarships) and would be glad to join your lab.

Your work on distributed systems and resource management resonates with both systems I have built. Archon, my diploma project, is an AI-native Source of Truth platform whose storage layer is a multi-tenant graph database: 50 isolated tenant schemas on PostgreSQL 16 + Apache AGE, with impact-analysis traversal <15ms at depth 4 — a resource-isolation problem first, an AI problem second. OmniSearch, our multimodal RAG video-search system, splits Control Plane (Kotlin) from Compute Plane (Go/Python workers for Whisper/CLIP over FFmpeg pipelines), with Qdrant as the vector tier — essentially a scheduling and resource-management exercise across heterogeneous workers.

As IMPISA's director, you see better than anyone how information systems and applications converge; I would bring the practitioner's side of that convergence (two production platforms, team lead of a 4-7 person lab, product-owner of archmap — an LLM-based C4 generator adopted for ~25 repositories at T-Bank).

Would my profile fit your lab for Fall 2027? My CV is attached. I am also applying to the IMBA program, but IMPISA is my research home if granted the opportunity.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: он распределёнщик + директор программы — письмо и про research, и про admission. 160-200 слов, США-стиль.*

---

### 2.3 Hwang Junseok — SNU TEMEP (junhwang@snu.ac.kr)

**Subject:** Prospective MS Student Fall 2027 — AI Tool Diffusion in Practice (TEMEP)

```
Dear Professor Hwang,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), applying to TEMEP for Fall 2027 (GKS scholarship). Your research on AI technology diffusion and knowledge management caught my attention because I have lived a small, measurable case of it.

At T-Bank (Russia's leading tech bank), AI coding agents had already reached every developer — but the organization's knowledge layer had not: architectural docs went stale in two weeks, and agents hallucinated APIs from them. I built archmap, an LLM-based C4 diagram generator, as a bottom-up answer: from a single lead's request it scaled to 4 products / ~25 repositories, cutting diagram delivery from 1-3 days to 15 minutes and onboarding from weeks to hours. Adoption was organic — engineers pulled it in, management approved it after the fact. That is technology diffusion in miniature: the gap between tool availability (100%) and organizational absorption (~10% when I started), and the product intervention that closed it.

Your work gives this practitioner's story a scientific frame — diffusion of AI tools, knowledge management, and the economics of adoption — which is exactly the training I lack and seek at TEMEP. My ambition is Platform / Technology Product Management, and my evidence so far is shipping: leading a 4-7 person R&D lab (Archon, an AI-native knowledge-graph platform; OmniSearch, a multimodal RAG system).

Would my profile fit your lab for Fall 2027? My CV is attached.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: его research = научная рамка для кейса archmap. Тон: меньше кода, больше product/diffusion/economics — под TEMEP.*

---

## Волна 2 (продолжение) — SJTU/ZJU (⚠️ добавлено 11.09.2026)

> **SJTU: acceptance letter от супервизора нужен ДО подачи (~15.12).** Поэтому в этих письмах аск сильнее — прямо спрашивать готовность супервизировать и просить acceptance letter. **ZJU:** Form for Provisional Acceptance даёт priority — аск мягче. Писать одновременно с KAIST/NTHU-письмами волны 2.

### 2.4 Lu Chen — SJTU, X-LANCE Lab (chenlusz@sjtu.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — Reducing Tool Hallucination via Grounded KG (Archon)

```
Dear Professor Lu,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), planning to apply to the Computer Science and Technology master program at SJTU's School of Computer Science for Fall 2027 (CSC scholarship). May I ask whether you would consider supervising a master's student — and if so, whether you could provide a supervisor's acceptance letter to accompany my application?

Your work speaks directly to the problem my diploma project solves. Archon is an AI-native Source of Truth platform: a multi-tenant Knowledge Graph (PostgreSQL 16 + Apache AGE, 50 tenants, impact-analysis traversal <15ms at depth 4) populated by a hybrid pipeline — deterministic AST parsing plus two-phase LLM extraction under a "Proof-of-Truth" rule: every graph edge must present evidence_files with file paths and line numbers, or it is discarded. Engineering agents consume this graph through MCP instead of hallucinating from stale docs. Your "Heads up!" paper (ICML 2025) frames the same failure mode — tool hallucination — from the alignment side, and NeuSym-RAG (ACL 2025) is the retrieval-side twin of my hybrid: neural extraction, symbolic verification. I would love to study how these two halves compose into a principled anti-hallucination architecture.

I also shipped archmap (LLM-based C4 generation, 4 products/~25 repos at T-Bank) and OmniSearch (multimodal RAG: Whisper/CLIP/Qdrant with a Control/Compute plane split).

My CV is attached. Would my profile fit X-LANCE for Fall 2027, and would you be open to providing the acceptance letter?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: её tool hallucination + NeuSym-RAG = две половины Archon (alignment + retrieval-side). Аск: acceptance letter явно.*

---

### 2.5 Xiaodong Gu — SJTU, LLMSE Lab (xiaodong.gu@sjtu.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — Repository-Level Verified Context (Archon)

```
Dear Professor Gu,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), applying to SJTU's Computer Science and Technology master program for Fall 2027 (CSC scholarship). May I ask whether you would consider supervising a master's student — and whether you could provide a supervisor's acceptance letter for my application?

Your repository-level code generation work (context inlining, FSE 2026) formalizes exactly the problem my diploma project attacks from the platform side. Archon builds a Knowledge Graph of an entire codebase (PostgreSQL + Apache AGE, 50 tenants) via hybrid extraction: a File Selector agent reads only file trees (90% token savings), an Extractor agent proposes edges, and a "Proof-of-Truth" rule requires evidence_files for every edge or rejects it. Your paper asks how to inline the right context into the prompt; Archon asks how to maintain that context as a durable, queryable, multi-tenant asset that agents consume via MCP. I believe these are the same research question at two lifecycle stages, and I would like to pursue the joint one under your supervision.

My supporting evidence: archmap, an LLM-based C4 diagram generator I initiated at T-Bank (adopted for 4 products/~25 repos, 1-3 days → 15 minutes), and OmniSearch, a multimodal RAG video-search system (Whisper/CLIP/Qdrant).

CV attached. Does my profile fit LLMSE for Fall 2027 — and would you be open to providing the acceptance letter?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: его FSE-2026 context inlining ↔ Archon = «тот же вопрос на двух стадиях lifecycle». Аск: acceptance letter.*

---

### 2.6 Xin Xia — ZJU, AI4SE (xxia@zju.edu.cn)

**Subject:** Prospective MS Student Fall 2027 — AI4SE with Production Platform Experience (Archon)

```
Dear Professor Xia,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), planning to apply to ZJU's Computer Science master program for Fall 2027 (CSC scholarship). Your AI4SE agenda — and the industry perspective you bring from Huawei — is precisely where I want to do my master's, and I would be glad to join your group. If my profile fits, may I also request the ZJU supervisor's Form for Provisional Acceptance to strengthen my application?

My diploma project, Archon, is a production-grade AI-native platform rather than a course artifact: a multi-tenant Knowledge Graph (PostgreSQL 16 + Apache AGE) with impact-analysis traversal <15ms at depth 4 across 50 isolated tenant schemas, populated by hybrid extraction (deterministic AST + two-phase LLM with a "Proof-of-Truth" evidence rule) and served to engineering agents via MCP. I lead the 4-7 person team that builds it: 17 modules decomposed into 3 services (7 ADRs, 37-task delivery board). Earlier I shipped archmap — an LLM-based C4 documentation generator adopted for ~25 repositories at T-Bank (1-3 days → 15 minutes) — and OmniSearch, a multimodal RAG system (Whisper/CLIP/Qdrant) deployed by Gazprom Neft.

Your empirical-AI4SE lens is what these systems lack: my engineering rules (Proof-of-Truth, evidence gating) deserve rigorous evaluation — extraction precision/recall on large open-source codebases, hallucination metrics, and the economics of context delivery. That is the research I propose for a master's under your supervision, on the path from system builder to Platform / Technology Product Manager.

My CV is attached. Would my profile fit your group for Fall 2027?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: production-платформа с NFR-метриками + его Huawei-масштаб; твой трек PM ↔ его индустриальность. Аск: Provisional Acceptance (мягче SJTU — priority, не обязательство).*

---

### 2.7 Wen Zhang — ZJU, ZJUKG Lab (zhang.wen@zju.edu.cn)

**Subject:** Prospective MS Student Fall 2027 — Multi-Tenant & Multimodal Knowledge Graphs (Archon/OmniSearch)

```
Dear Professor Zhang,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), applying to ZJU's Computer Science master program for Fall 2027 (CSC scholarship). Your work on knowledge graphs, representation learning, and multi-modal learning covers both systems I have built — and I would be glad to pursue a master's in your lab. If my profile fits, may I request the supervisor's Form for Provisional Acceptance to accompany my application?

My diploma project, Archon, is an AI-native Source of Truth platform whose core is a multi-tenant Knowledge Graph: 50 isolated tenant schemas on PostgreSQL 16 + Apache AGE, with impact-analysis traversal <15ms at depth 4 — an engineering answer to the question of how graph representations scale under tenancy, which your representation-learning work frames from the learning side. Its extraction pipeline (deterministic AST + two-phase LLM with a "Proof-of-Truth" evidence rule) keeps the graph trustworthy; agents consume it via MCP.

The second system is OmniSearch, a multimodal RAG video-search platform (Whisper + CLIP + Qdrant) with a Control/Compute plane split — a multimodal retrieval question close to your multi-modal KG research.

Your ZJUKG lab is the strongest KG environment I could join; my contribution would be a builder's: two production systems, a 4-7 person team led for two years, and an LLM-to-C4 generator (archmap) adopted for ~25 repositories at T-Bank.

CV attached. Would my profile fit your group for Fall 2027?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/Team-v3-9-a | CV attached
```

*Хук: multi-modal KG ↔ OmniSearch + representation learning ↔ graph traversal. Assistant Prof — отвечающий уровень. Аск: Provisional Acceptance.*

---

### Запасные письма SJTU/ZJU (если молчат 10-14 дней)

**Beijun Shen (bjshen@sjtu.edu.cn):** тот же аск acceptance letter, хук — code LLM interpretation + repository mining ↔ AST/Tree-sitter extraction; сослаться на его FSE/ICSE 2026 работы. Отправлять только если Lu Chen И Gu молчат.

**Huajun Chen (huajunsir@zju.edu.cn):** короткое письмо (он директор ZJUKG, перегружен), хук — OpenBG business KG ↔ Archon как enterprise KG; спросить также, кого из коллег порекомендует. Отправлять если Xia и Zhang молчат.

---

## Чек-лист перед отправкой (каждое письмо)

- [ ] Подставить ссылку на актуальный CV (Google Drive/Dropbox, PDF) — проверить, что открывается из инкогнито
- [ ] GitHub Archon: README на английском, метрики в бейджах, свежий коммит — профессор может открыть в тот же день
- [ ] Отправка: вт-чт, утро по местному времени вуза (Tsinghua/PKU — утро по Пекину = 4-6 утра Томска → отправить вечером накануне с отложенной отправкой)
- [ ] Отправлять с ischademadda@gmail.com; подпись с полным именем + GitHub
- [ ] Если ответа нет 10-14 дней — одно вежливое follow-up (2-3 предложения), потом переход ко второму профессору вуза
- [ ] Ответы сортировать: (а) «пишите официально / supporting letter» → просить короткое письмо к заявке CSC/GKS; (б) «нет мест» → вежливо спросить, кого из коллег порекомендует; (в) молчание после follow-up → волна 3

## Что ответить профессору, если он заинтересуется (заготовки)

**«Can you send me your transcript / grades?»**
→ Транскрипт на английском (заказать в ТПУ заранее, см. docs_legalization) + честно: GPA 3.93/5.0, сильнейшие — системные/проектные курсы; оценки осеннего семестра 2026 войдут в транскрипт до подач GKS/KAIST и поднимут кумулятив до ~4.0.

**«Do you have funding needs?»**
→ «I am applying through CSC Type B / GKS / TaiwanICDF, which covers tuition and stipend — I do not require lab funding, only your support in the university-track process.» (НЕ просить funding в первом письме.)

**«Send me a research proposal.»**
→ Одностраничная выжимка из csc_study_plan_2027.md секция 5 (Year 1/Year 2) под его лабораторию.

**«I agree to supervise / here is the acceptance letter» (SJTU) или «заполни Form for Provisional Acceptance» (ZJU)**
→ Для SJTU: попросить письмо в PDF на бланке с фразой "I agree to supervise Mr. Denis Shtepa as a master's student in Fall 2027" + имя/подпись. Для ZJU: форма заполняется на портале ZJU — спросить у профессора, нужна ли от тебя какая-то часть.

**Волна 3 (октябрь):** Xia Shutao (Tsinghua), Ge Li (PKU), In-Young Ko (KAIST), Yun-Nung Chen (низкий приоритет), Beijun Shen (если Gu молчит), Huajun Chen (если Xia/Zhang молчат).
