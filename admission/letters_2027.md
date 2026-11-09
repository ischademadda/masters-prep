# Письма профессорам 2027

> **Обновлено:** 09.11.2026. Статус писем ведётся в `README.md`, раздел 4. Профессора и публикации: `professors_shortlist_2027.md`.
> **Правило честности:** Archon: спроектирована архитектура (7 ADR), начат базовый каркас, метрик нет. OmniSearch: R&D-прототип, не задеплоен. archmap: ~40 репозиториев, ~15 минут на репозиторий (как в CV). Не писать «deployed», «production», «<15ms», «90% tokens», «1–3 дня».
> **Отправка:** Gmail ischademadda@gmail.com, plain text, CV в PDF меньше 1 МБ. Будни, утро по местному времени вуза (Пекин 08:00–10:00 = Томск 04:00–06:00, ставить отложенную отправку).
> **Тема письма (общая):** `Prospective Master's Student Fall 2027 — AI-native Architecture (Archon: KG + LLM + MCP)`

---

## 1. Отправленные письма (тексты нужны для follow-up)

> Zheng: 20.10 (исправление 27.10). Liu, Lu Chen: 28.10 ✅. Gu: 28.10, Xin Xia, Wen Zhang, Jerry Chou: 29.10 — по плану, отправку подтвердить.
> ⚠️ Письмо Zheng ушло со старыми цифрами archmap («4 products, ~25 repos»). В follow-up и следующих письмах использовать цифры из CV.

### 1.1 Zheng Haitao — 🇨🇳 Tsinghua SIGS (zheng.haitao@sz.tsinghua.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — Knowledge Graph Grounding for AI Agents (Archon)

```
Dear Professor Zheng,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia) and Team Lead of our R&D lab. I am writing to ask whether you would consider supervising a master's student for Fall 2027, as I plan to apply to the Data Science and Information Technology program at Tsinghua SIGS (CSC scholarship).

My diploma project, Archon, is an AI-native Source of Truth platform designed to keep architectural knowledge synchronized with code and deliver verified context to AI agents via MCP. We have completed the architecture (7 ADRs) and are now building the base skeleton. Its core is a multi-tenant Knowledge Graph on PostgreSQL 16 + Apache AGE (graph-per-tenant isolation) populated by a hybrid pipeline: deterministic AST parsing (Tree-sitter) plus two-phase LLM extraction with a "Proof-of-Truth" rule — every graph edge must carry evidence_files with file paths and line numbers, otherwise it is discarded. Whether this rule keeps extraction both verifiable and cheap is exactly what I want to measure.

I have read your work on knowledge graph completion (TKDE) and RLHF-V (CVPR 2024), and I see a direct continuation of my interests: my Proof-of-Truth rule is essentially a grounding constraint on LLM output, and scaling it to hundreds of tenants raises exactly the completion-and-consistency questions your group studies. Separately, I built archmap, an LLM-based C4 diagram generator adopted for 4 products (~25 repos) at T-Bank, and designed OmniSearch, a multimodal RAG video-search system (Whisper/CLIP/Qdrant) for industrial safety monitoring.

My CV and a one-page research summary are attached. I would be grateful for a brief reply on whether my profile fits your lab's plans for Fall 2027 — and whether you would be open to a short call.

Thank you for your time.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

*Хук: KG completion ↔ AGE-граф + RLHF-V ↔ grounding LLM-вывода. 190 слов — норм.*

---

### 1.2 Xuanzhe Liu — 🇨🇳 PKU SEI (liuxuanzhe@pku.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — MCP Agent Context on Top of LLM Serving (Archon)

```
Dear Professor Liu,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), Team Lead of our R&D lab. I plan to apply to the MSc Software Engineering program at PKU for Fall 2027 (CSC scholarship) and would be honored to work in your group.

My diploma project, Archon, is an AI-native Source of Truth platform for enterprise architecture, now in early implementation (architecture complete, base skeleton in progress). Its core is a multi-tenant Knowledge Graph (PostgreSQL + Apache AGE) fed by a hybrid pipeline — deterministic AST parsing plus two-phase LLM extraction where a File Selector agent reads only file trees to keep token costs low, and every extracted edge must present evidence_files, or it is discarded. The graph will be served to engineering AI agents through MCP: agents ask "what breaks if I change this API" and get traversal-backed answers (our NFR: <100ms at depth 4) instead of hallucinating from stale Confluence pages.

Your work is the natural next layer under this system: RAGCache (TOCS 2026) and Pythia address exactly the serving economics of RAG-heavy, agent-native workloads that Archon will push onto the infrastructure, and BAMAS (AAAI 2026) formalizes the multi-agent budget allocation our design currently handles with ad-hoc heuristics. I would love to research how agent-context platforms like Archon should co-design with the LLM serving stack — e.g., what a "context-serving tier" between vector stores and application agents should look like.

Previously I built archmap at T-Bank (LLM-based C4 generation; it covered about 40 repositories by the time I left, at roughly 15 minutes per repository) and OmniSearch (a multimodal RAG prototype: Whisper/CLIP/Qdrant, Control/Compute plane split).

My CV is attached. Would my profile fit your lab for Fall 2027? I would gladly schedule a call at your convenience.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

*Хук: его RAGCache/Pythia/BAMAS = системный слой ПОД Archon → «co-design platform + serving». Самый сильный research-мачч.*

---

### 1.3 Jerry Chou — 🇹🇼 NTHU, директор IMPISA/IMS (jchou@cs.nthu.edu.tw)

**Subject:** Prospective MS Student Fall 2027 — IMPISA (multi-tenant platform, resource management)

```
Dear Professor Chou,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia). I plan to apply to the International Master Program in Information Systems and Applications for Fall 2027 (via TaiwanICDF and MOE scholarships) and would be glad to join your lab.

Your work on distributed systems and resource management resonates with both systems I have worked on. Archon, my diploma project, is an AI-native Source of Truth platform whose storage layer is designed as a multi-tenant graph database: one isolated schema per tenant on PostgreSQL 16 + Apache AGE, with an NFR of <100ms impact-analysis traversal at depth 4 — a resource-isolation problem first, an AI problem second. OmniSearch, a multimodal RAG video-search system we designed, splits Control Plane (Kotlin) from Compute Plane (Go/Python workers for Whisper/CLIP over FFmpeg pipelines), with Qdrant as the vector tier — essentially a scheduling and resource-management exercise across heterogeneous workers.

As IMPISA's director, you see better than anyone how information systems and applications converge; I would bring the practitioner's side of that convergence (team lead of a 4-7 person lab, and the author of archmap — an LLM-based C4 generator that covered about 40 repositories at T-Bank, at roughly 15 minutes per repository).

Would my profile fit your lab for Fall 2027? My CV is attached. I am also applying to the IMBA program, but IMPISA is my research home if granted the opportunity.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

*Хук: он распределёнщик + директор программы — письмо и про research, и про admission. 160-200 слов, США-стиль.*

---

### 1.4 Lu Chen — 🇨🇳 SJTU, X-LANCE Lab (chenlusz@sjtu.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — Reducing Tool Hallucination via Grounded KG (Archon)

```
Dear Professor Chen,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), planning to apply to the Computer Science and Technology master program at SJTU's School of Computer Science for Fall 2027 (CSC scholarship). May I ask whether you would consider supervising a master's student — and if so, whether you could provide a supervisor's acceptance letter to accompany my application?

Your work speaks directly to the problem my diploma project addresses. Archon is an AI-native Source of Truth platform, now in early implementation (architecture complete, base skeleton in progress): a multi-tenant Knowledge Graph (PostgreSQL 16 + Apache AGE) populated by a hybrid pipeline — deterministic AST parsing plus two-phase LLM extraction under a "Proof-of-Truth" rule: every graph edge must present evidence_files with file paths and line numbers, or it is discarded. Engineering agents will consume this graph through MCP instead of hallucinating from stale docs. Your "Heads up!" paper (ICML 2025) frames the same failure mode — tool hallucination — from the alignment side, and NeuSym-RAG (ACL 2025) is the retrieval-side twin of my hybrid: neural extraction, symbolic verification. I would love to study how these two halves compose into a principled anti-hallucination architecture.

I also built archmap at T-Bank (LLM-based C4 generation, about 40 repositories at roughly 15 minutes each) and OmniSearch (a multimodal RAG prototype: Whisper/CLIP/Qdrant with a Control/Compute plane split).

My CV is attached. Would my profile fit X-LANCE for Fall 2027, and would you be open to providing the acceptance letter?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

*Хук: статья про tool hallucination + NeuSym-RAG = две половины Archon (alignment + retrieval-side). Аск: acceptance letter явно.*

---

### 1.5 Xiaodong Gu — 🇨🇳 SJTU, LLMSE Lab (xiaodong.gu@sjtu.edu.cn)

**Subject:** Prospective Master's Student Fall 2027 — Repository-Level Verified Context (Archon)

```
Dear Professor Gu,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), applying to SJTU's Computer Science and Technology master program for Fall 2027 (CSC scholarship). May I ask whether you would consider supervising a master's student — and whether you could provide a supervisor's acceptance letter for my application?

Your repository-level code generation work (context inlining, FSE 2026) formalizes exactly the problem my diploma project attacks from the platform side. Archon (architecture complete, implementation starting) is designed to build a Knowledge Graph of an entire codebase (PostgreSQL + Apache AGE, multi-tenant) via hybrid extraction: a File Selector agent reads only file trees to cut token costs, an Extractor agent proposes edges, and a "Proof-of-Truth" rule requires evidence_files for every edge or rejects it. Your paper asks how to inline the right context into the prompt; Archon asks how to maintain that context as a durable, queryable, multi-tenant asset that agents consume via MCP. I believe these are the same research question at two lifecycle stages, and I would like to pursue the joint one under your supervision.

My supporting evidence: archmap, an LLM-based C4 diagram generator I built at T-Bank (about 40 repositories, roughly 15 minutes each), and OmniSearch, a multimodal RAG video-search prototype we built (Whisper/CLIP/Qdrant).

CV attached. Does my profile fit LLMSE for Fall 2027 — and would you be open to providing the acceptance letter?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

*Хук: его FSE-2026 context inlining ↔ Archon = «тот же вопрос на двух стадиях lifecycle». Аск: acceptance letter.*

---

### 1.6 Xin Xia — 🇨🇳 ZJU, AI4SE (xin.xia@zju.edu.cn)

**Subject:** Prospective MS Student Fall 2027 — AI4SE: Verifiable LLM Extraction for Architecture (Archon)

```
Dear Professor Xia,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), planning to apply to ZJU's Computer Science master program for Fall 2027 (CSC scholarship). Your AI4SE agenda — and the industry perspective you bring from Huawei — is precisely where I want to do my master's, and I would be glad to join your group. If my profile fits, may I also request the ZJU supervisor's Form for Provisional Acceptance to strengthen my application?

My diploma project, Archon, is an AI-native platform for architecture knowledge, now moving from design to implementation: a multi-tenant Knowledge Graph (PostgreSQL 16 + Apache AGE, graph-per-tenant isolation), populated by hybrid extraction (deterministic AST + two-phase LLM with a "Proof-of-Truth" evidence rule) and served to engineering agents via MCP. I lead the 4-7 person team building it: we decomposed 17 modules into 3 services (7 ADRs, 37-task delivery board) and are now implementing the base skeleton. Earlier I built archmap — an LLM-based C4 documentation generator that covered about 40 repositories at T-Bank (roughly 15 minutes each) — and OmniSearch, a multimodal RAG prototype (Whisper/CLIP/Qdrant).

Your empirical-AI4SE lens is what these systems lack: my engineering rules (Proof-of-Truth, evidence gating) deserve rigorous evaluation — extraction precision/recall on large open-source codebases, hallucination metrics, and the economics of context delivery. That is the research I propose for a master's under your supervision, on the path from system builder to Platform / Technology Product Manager.

My CV is attached. Would my profile fit your group for Fall 2027?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

*Хук: его empirical AI4SE = способ честно измерить Proof-of-Truth + его Huawei-масштаб; твой трек PM ↔ его индустриальность. Аск: Provisional Acceptance (мягче 🇨🇳 SJTU — priority, не обязательство).*

---

### 1.7 Wen Zhang — 🇨🇳 ZJU, ZJUKG Lab (zhang.wen@zju.edu.cn)

**Subject:** Prospective MS Student Fall 2027 — Multi-Tenant & Multimodal Knowledge Graphs (Archon/OmniSearch)

```
Dear Professor Zhang,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), applying to ZJU's Computer Science master program for Fall 2027 (CSC scholarship). Your work on knowledge graphs, representation learning, and multi-modal learning covers both systems I have worked on — and I would be glad to pursue a master's in your lab. If my profile fits, may I request the supervisor's Form for Provisional Acceptance to accompany my application?

My diploma project, Archon, is an AI-native Source of Truth platform whose core is a multi-tenant Knowledge Graph (one isolated schema per tenant on PostgreSQL 16 + Apache AGE; architecture complete, implementation starting) — an engineering approach to the question of how graph representations scale under tenancy, which your representation-learning work frames from the learning side. Its extraction pipeline (deterministic AST + two-phase LLM with a "Proof-of-Truth" evidence rule) is designed to keep the graph trustworthy; agents will consume it via MCP.

The second is OmniSearch, a multimodal RAG video-search system we designed (Whisper + CLIP + Qdrant) with a Control/Compute plane split — a multimodal retrieval question close to your multi-modal KG research.

Your ZJUKG lab is the strongest KG environment I could join; my contribution would be a builder's: a 4-7 person team led for two years and an LLM-to-C4 generator (archmap) that covered about 40 repositories at T-Bank.

CV attached. Would my profile fit your group for Fall 2027?

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

*Хук: multi-modal KG ↔ OmniSearch + representation learning ↔ graph traversal. Assistant Prof — отвечающий уровень. Аск: Provisional Acceptance.*

---

## 2. Запасные письма 🇨🇳 SJTU/ZJU (если молчат 10–14 дней)

**Beijun Shen (bjshen@sjtu.edu.cn):** тот же аск acceptance letter, хук — code LLM interpretation + repository mining ↔ AST/Tree-sitter extraction; сослаться на его FSE/ICSE 2026 работы. Отправлять только если Lu Chen И Gu молчат.

**Huajun Chen (huajunsir@zju.edu.cn):** короткое письмо (он директор ZJUKG, перегружен), хук — OpenBG business KG ↔ Archon как enterprise KG; спросить также, кого из коллег порекомендует. Отправлять если Xia и Zhang молчат.

---

## 3. Чек-лист перед отправкой

- [ ] Подставить ссылку на актуальный CV (Google Drive/Dropbox, PDF) — проверить, что открывается из инкогнито
- [ ] GitHub Archon: README на английском с честным статусом (что спроектировано / что реализовано), свежий коммит — профессор может открыть в тот же день
- [ ] Отправка: вт-чт, утро по местному времени вуза (🇨🇳 Tsinghua/PKU — утро по Пекину = 4-6 утра Томска → отправить вечером накануне с отложенной отправкой)
- [ ] Отправлять с ischademadda@gmail.com; подпись с полным именем + GitHub
- [ ] Если ответа нет 10-14 дней — одно вежливое follow-up (2-3 предложения), потом переход ко второму профессору вуза
- [ ] Ответы сортировать: (а) «пишите официально / supporting letter» → просить короткое письмо к заявке CSC; (б) «нет мест» → вежливо спросить, кого из коллег порекомендует; (в) молчание после follow-up → волна 3

## 4. Follow-up (через 10–14 дней тишины, один раз)

```
Subject: Re: <тема первого письма>

Dear Professor <Last Name>,

I am following up on my email from <date> about joining your group as a master's student in Fall 2027. I understand you receive many messages, so a one-line reply on whether my profile could fit your lab would help me plan my <CSC / university> application, which closes in <month>.

Since my first email, <одна реальная новость: IELTS-результат / новый этап Archon / прочитанная статья профессора и один вопрос по ней>.

Thank you for your time.

Best regards,
Denis Shtepa
```

* Отвечать в тот же тред (Re:), не новым письмом. 80–120 слов.
* Новость только реальная. Если её нет, абзац убрать.
* После follow-up тишина 7–10 дней → писать следующему профессору этого вуза (раздел 2).

---

## 5. Рекомендатели: скрипты просьбы

**Научному руководителю ТПУ:**
> «Здравствуйте, [Имя Отчество]! Я подаюсь в магистратуру на осень 2027: Тайвань (🇹🇼 NTU, 🇹🇼 NYCU, 🇹🇼 NTHU) и Китай (стипендия CSC). Первые сроки в декабре–январе. Мне нужно академическое рекомендательное письмо на английском с акцентом на дипломный проект Archon и исследовательскую работу. Драфт я подготовлю сам, от вас нужно проверить и подписать. Порталы присылают ссылку рекомендателю на почту, это займёт 10–15 минут. Будете готовы меня порекомендовать?»

**Лиду / ментору в Т-Банке:**
> «Привет, [Имя]! Подаюсь в магистратуру в Азию (Тайвань / Китай) на осень 2027. Нужна рекомендация с места работы. Акцент на системный анализ и archmap: собрал сам, дошёл примерно до 40 репозиториев. Текст на английском напишу сам, от тебя согласование и подпись. Первые сроки в декабре. Сможешь?»

* Отправить обоим CV + 5–7 тезисов «что можно про меня сказать» с фактами (без «top X%»).
* Уточнить у 🇹🇼 NTU/NYCU: письмо загружает рекомендатель через ссылку или ты сам. От этого зависит, нужна ли подпись на бланке.

---

## 6. Заготовки ответов, если профессор заинтересовался

**«Can you send me your transcript / grades?»**
→ Транскрипт на английском (заказать в ТПУ заранее, см. docs_legalization) + честно: GPA 3.93/5.0, сильнейшие — системные/проектные курсы; оценки осеннего семестра 2026 войдут в транскрипт к январю.

**«Do you have funding needs?»**
→ «I am applying through the CSC Type B / Taiwan MOE / university scholarship, which covers tuition and stipend — I do not require lab funding, only your support in the university-track process.» (НЕ просить funding в первом письме.)

**«Send me a research proposal.»**
→ Одностраничная выжимка из `study_plans/study_plan_master_2027.md`, секция 5 (Year 1/Year 2) под его лабораторию.

**«I agree to supervise / here is the acceptance letter» (🇨🇳 SJTU) или «заполни Form for Provisional Acceptance» (🇨🇳 ZJU)**
→ Для 🇨🇳 SJTU: попросить письмо в PDF на бланке с фразой "I agree to supervise Mr. Denis Shtepa as a master's student in Fall 2027" + имя/подпись. Для 🇨🇳 ZJU: форма заполняется на портале 🇨🇳 ZJU — спросить у профессора, нужна ли от тебя какая-то часть.

**Следующие письма:** Yun-Nung Chen (🇹🇼 NTU CSIE, теперь приоритет), профессора 🇹🇼 NYCU / 🇹🇼 NCKU (подобрать), Xia Shutao (🇨🇳 Tsinghua), Ge Li (🇨🇳 PKU), Beijun Shen (если Gu молчит), Huajun Chen (если Xia/Zhang молчат).
