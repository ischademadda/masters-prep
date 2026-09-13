# Шортлист профессоров для писем — Fall 2027 (CN / TW / KR)

> **Дата:** 10.09.2026 (обновлено 11.09.2026)
> **Контекст:** Денис Штэпа, ТПУ, диплом 2027, подача осень 2027 (CSC Type B, MOE Taiwan, GKS Korea).
> **Цель писем:** ~~октябрь 2026~~ **СРОЧНО — сентябрь 2026.** Tsinghua CSC-дедлайн mid-Dec 2026 (First-Round, официальный reminder от 07.09.2026), PKU окно ~20.10-23.12. Письма профессорам должны уйти за 4-6 недель до подачи → волны 1-2 отправлять в ближайшие 1-2 недели. Тема писем: **Archon + RAG** (см. `asia_masters_2027_shortlist_and_cv.md`).
> **Все email'ы и данные проверены вручную** на официальных страницах кафедр + публикации сверены с DBLP (2024-2026).

---

## 1. Стратегия писем

| Куда | Нужны ли письма? | Формат |
|---|---|---|
| **Китай (CSC Type B, Tsinghua/PKU)** | ✅ **Критично** — приглашение/поддержка профессора резко повышает шансы в university track | Письмо + CV + короткий research pitch; просить о встрече/ответе, в идеале — supporting letter к заявке |
| **Корея (GKS University Track, KAIST/SNU)** | ⚠️ Полезно, не обязательно — GKS не требует, но рекомендация профессора в personal statement усиливает | Короткое письмо, спросить про lab positions / RA funding |
| **Тайвань (MOE, NTU/NTHU)** | ⚠️ Опционально — admission по документам, но контакт с директором программы (NTHU IMS) — плюс | Короткое письмо директорам программ + интересным профессорам |

**Правило:** писать 2 письма за один раз нельзя в один вуз — сначала приоритетный, через 1-2 недели без ответа — второй.

**Скелет письма (октябрь 2026):**
1. Кто я: 4th-year SE @ TPU, GPA 3.93→4.0+, Team Lead R&D lab, стажировка T-Bank (System Analyst).
2. Что сделал: Archon (KG + LLM extraction + MCP), OmniSearch (multimodal RAG), archmap (C4-генерация, 4 продукта/25 репо).
3. Почему ВАМ: указать 1-2 ЕГО статьи 2024-2026 (из таблиц ниже) и связать со своим проектом.
4. Что прошу: рассмотреть меня как магистранта Fall 2027 в вашей лаборатории / короткий zoom / supporting letter.
5. Приложения: CV (1 стр.), ссылка на GitHub Archon.

---

## 2. 🇨🇳 Китай — Tsinghua SIGS (Data Science & IT, CSC Type B)

### ⭐ Zheng Haitao (郑海涛) — ПРИОРИТЕТ #1
- **Title:** Associate Professor, PhD supervisor (Институт компьютерных наук, SIGS)
- **Email:** zheng.haitao@sz.tsinghua.edu.cn
- **Кабинет:** Room 1613, Information Building; тел +86 (0755) 2603-6076
- **Направление:** Knowledge Engineering, KG completion, parameter-efficient fine-tuning, RLHF
- **Публикации (проверено):** KG completion (TKDE 2020), OpenPrompt (ACL 2022), RLHF-V (CVPR 2024), parameter-efficient fine-tuning (Nature Machine Intelligence 2023), ShuffleNet V2
- **Хук для письма:** Archon = Knowledge Graph на PostgreSQL 16 + Apache AGE с LLM-extraction и Proof-of-Truth. Его KG completion + моё evidence-grounded извлечение — прямое пересечение.

### Xia Shutao (夏树涛)
- **Title:** Professor, Director of Institute of Computer Science and Technology, SIGS
- **Email:** xiast@sz.tsinghua.edu.cn
- **Кабинет:** Room 1609; тел 0755-26036081
- **Направление:** ML, multimodal RAG / ChatGPT / AIGC / retrieval augmentation, video retrieval, AI security (NeurIPS/ICML/ICLR/CVPR)
- **Хук для письма:** OmniSearch — multimodal RAG над видеоархивами (Whisper + CLIP + Qdrant), industrial deployment (Gazprom Vostok Neft). Плюс его интерес к AI security ↔ Archon's Proof-of-Truth как защита от LLM-галлюцинаций.
- **Нюанс:** как директор института — занят, но это сигнал "сильная лаборатория". Письмо короче и конкретнее.

---

## 3. 🇨🇳 Китай — PKU SEI (MSc Software Engineering, CSC Type B)

### ⭐ Xuanzhe Liu (刘譞哲) — ПРИОРИТЕТ #2 (самый сильный research-мачч по LLM-системам)
- **Title:** Professor, Software Engineering Institute
- **Email:** liuxuanzhe@pku.edu.cn
- **Направление:** LLM serving, RAG systems, agents, distributed systems (301 публикация)
- **Публикации (проверено DBLP):** RAGCache (ACM TOCS 2026), Pythia — agent-native LLM serving (2026), BAMAS — budget-aware multi-agent systems (AAAI 2026), FastServe (NSDI 2026), MegaScale-MoE (EuroSys 2026)
- **Хук для письма:** Archon доставляет контекст агентам через MCP + RAG — его RAGCache/Pythia/BAMAS это буквально системный слой под моим приложением. Готов делать research на стыке его LLM-serving и моего knowledge-grounding.

### Ge Li (李戈)
- **Title:** Professor, SEI
- **Email:** lig@pku.edu.cn
- **Направление:** AI for SE, code generation
- **Публикации (проверено):** CodeGeeX (KDD 2023) — LLM для кода
- **Хук для письма:** archmap — LLM-генерация C4-диаграмм из кода (File Selector + Extractor, n8n). Его CodeGeeX-направление = генерация кода, моя ветка = генерация архитектуры из кода.

### Запасные (не писать первыми, но держать в CV/Study Plan):
- **Zhi Jin** (zhijin@pku.edu.cn) — knowledge-driven SE (близко к Archon, но ядро его группы = Zhihai Wang и др.)
- **Tao Xie** (taoxie@pku.edu.cn) — IEEE/AAAI Fellow, testing
- **Gang Huang** (hg@pku.edu.cn), **Dan Hao**, **Yingfei Xiong** — software analysis

---

## 3a. 🇨🇳 Китай — SJTU School of Computer Science (⚠️ добавлено 11.09.2026 — CSP Type B, дедлайн 1-го раунда ~15.12.2026)

> **КРИТИЧНО:** SJTU School of CS требует **acceptance letter от супервизора ДО подачи** — контакт с профессорами начинать сразу, вместе с волной 2. Процесс: письмом спросить готовность супервизировать → при согласии просить acceptance letter для приложения к заявке (pre-admission letter от школы недоступен до аппрува заявки, но письмо профессора — да; см. me.sjtu.edu.cn/YanJS/GAdmission/3718.html и brochure 2026).

### ⭐ Lu Chen (陈璐) — ПРИОРИТЕТ (равен волне 2)
- **Title:** Associate Professor, X-LANCE Lab
- **Email:** chenlusz@sjtu.edu.cn (верифицирован: chen.lu/en/)
- **Направление:** LLMs, agentic systems, AI for Science, RAG
- **Публикации (проверено):** NeuSym-RAG — hybrid neural-symbolic retrieval (ACL 2025); "Heads up! LLMs, Reducing Tool Hallucination via Reliability Alignment" (ICML 2025); task-specific data selection (NeurIPS 2025)
- **Хук для письма:** Прямое пересечение: её tool hallucination reduction — это Proof-of-Truth в её постановке; NeuSym-RAG (нейро-символный гибрид) — это Archon (AST-детерминизм + LLM-семантика) в retrieval-форме. OmniSearch — её мультимодальный RAG-кейс.

### ⭐ Xiaodong Gu (顾小东) — ПРИОРИТЕТ (равен волне 2)
- **Title:** Associate Professor, co-director LLMSE Lab
- **Email:** xiaodong.gu@sjtu.edu.cn (верифицирован: guxd.github.io)
- **Направление:** LLMs for code, repository-level generation, intelligent SE
- **Публикации (проверено):** repository-level code generation via context inlining (FSE 2026); machine vs human programmer patterns (ICSE 2025); domain-specific code generation (TOSEM 2025, ESI Highly Cited)
- **Хук для письма:** Его repository-level context inlining — буквально задача Archon: как собрать verified context из целого репо для LLM. archmap — его домен (генерация из кода), Archon — эволюция его FSE-работы.

### Beijun Shen (沈备军) — средний приоритет (после Gu, если тишина)
- **Title:** Associate Professor, co-director LLMSE Lab
- **Email:** bjshen@sjtu.edu.cn (верифицирован: base.sjtu.edu.cn/~bjshen)
- **Направление:** SE, LLM-based software technologies, code interpretation
- **Публикации (проверено):** code LLM interpretation (FSE/ICSE 2026), anti-adversarial prompt desensitizing (AAAI 2026), malicious code generation (TSE 2025)
- **Хук для письма:** Код-LLM интерпретация + repository mining ↔ AST+Tree-sitter extraction. Очень сеньорный (SWEBOK co-editor, 200+ публикаций) — может делегировать в LLMSE.

---

## 3b. 🇨🇳 Китай — ZJU College of Computer Science (⚠️ добавлено 11.09.2026 — CSC Type B, дедлайн ~31.12.2026)

> Form for Provisional Acceptance of International Student by ZJU Supervisor — даёт **priority** (не строго обязательно). Контакт в сентябре-октябре.

### ⭐ Xin Xia (夏鑫) — ПРИОРИТЕТ (волна 2-3)
- **Title:** Qiushi Distinguished Professor; ex-Huawei Chief Expert (2021-2025); ACM Distinguished Member; ACM SIGSOFT Early Career Award 2022
- **Email:** xxia@zju.edu.cn (верифицирован: xin-xia.github.io)
- **Направление:** AI4SE / SE4AI, program comprehension, empirical SE
- **Публикации:** 360+ публикаций, 160+ CCF-A
- **Хук для письма:** Идеальный мачч под Platform PM трек: его Huawei-бэкграунд = индустриальный масштаб; Archon с его NFR-метриками (<15ms, 50 tenants) — production-система, а не игрушка. Он набирает команду после перехода из Huawei — момент удачный.

### ⭐ Wen Zhang (张文) — ПРИОРИТЕТ (волна 2-3)
- **Title:** Assistant Professor, ZJUKG Lab
- **Email:** zhang.wen@zju.edu.cn (верифицирован: person.zju.edu.cn/en/wenzhang)
- **Направление:** Knowledge graphs, representation learning, multi-modal learning, neural reasoning
- **Публикации:** 5,794 цитирований; KG completion, multi-modal KG
- **Хук для письма:** Multi-modal KG ↔ OmniSearch (мультимодальный RAG) + Archon (graph traversal, KG). Assistant Professor — самый отвечающий уровень (мало писем, активно набирает).

### Huajun Chen (陈华钧) — средний приоритет (звёздный, но перегруженный)
- **Title:** Full Professor, директор ZJUKG Lab (крупнейшая KG-лаба Китая)
- **Email:** huajunsir@zju.edu.cn (верифицирован: person.zju.edu.cn/en/huajun)
- **Направление:** Knowledge graphs + LLM, AI for Science; OpenBG (business KG для Alibaba)
- **Хук для письма:** KG+LLM integration — ядро Archon. Но Full Prof + директор = высокая конкуренция и мало bandwidth; писать после Xia/Zhang или параллельно с коротким письмом.

---

## 4. 🇰🇷 Корея — KAIST (School of Computing / GSai, GKS)

### ⭐ Shin Yoo (유신) — ПРИОРИТЕТ #3
- **Title:** Endowed Chair Professor, School of Computing
- **Email:** shin.yoo@kaist.ac.kr
- **Направление:** Software testing + LLM for SE, autonomous testing agents
- **Публикации (проверено DBLP):** COSMosFL — LLM fault localization (LLM4Code@ICSE 2025), LLM agents for package install (SANER 2025), autonomous testing agents (ASE 2023)
- **Хук для письма:** Archon's Proof-of-Truth (каждое ребро графа требует evidence_files с путями и строками, иначе отбрасывается) — это верифицируемость LLM-вывода в SE-задачах, ровно его повестка.

### In-Young Ko (고인영)
- **Title:** Professor, School of Computing (division: Software Design? — КOIST AI+SE group)
- **Email:** iko@kaist.ac.kr
- **Направление:** AI + SE, ML service composition, edge-cloud ML
- **Публикации (проверено DBLP):** OrchestML — automated ML service compositions (APSEC 2025), adaptive ML edge-cloud (JWE 2026), code-embedding fault localization (ICST 2026)
- **Хук для письма:** archmap — оркестрация LLM-пайплайна в n8n + его OrchestML = service orchestration для ML. Плюс мой OmniSearch Control/Compute Plane split.

### Запасной: **Ho-Jin Choi** (hojinc@kaist.ac.kr) — AI+SE, LLM benchmarks, MultiVerse (ICCV 2025)

---

## 5. 🇰🇷 Корея — SNU TEMEP (MS Technology Management, Economics and Policy, GKS)

### Hwang Junseok (황준석)
- **Title:** Professor, TEMEP; DIGITALOGY Lab
- **Email:** junhwang@snu.ac.kr
- **Тел:** +82-2-880-8679; Bldg 37, Room 312
- **Направление:** AI technology diffusion, knowledge management, smart cities, digital policy
- **Публикации (проверено):** AI technology diffusion (Scientometrics 2025), knowledge management (TFSC), smart cities
- **Хук для письма:** Мой путь = Platform PM: archmap как продукт (4 продукта/25 репо, метрики времени 1-3 дня → 10-15 мин). Его research о диффузии AI-технологий в индустрии — это научная рамка для моего продуктового кейса. Тон письма: меньше код, больше product/market/diffusion.

---

## 6. 🇹🇼 Тайвань — NTHU (IMPISA/IMS + IMBA — обновлено 11.09.2026)

> ⚠️ **Обновление 11.09.2026:** замена NTU GMBA — **NTHU IMBA** (College of Technology Management): 100% English, 2 года, work experience **optional** («preferable», в гайдлайне Fall 2026 сертификат опыта — в разделе Optional). Подача ~15.12.2026 — 25.02.2027, IELTS 6.0, без экзаменов/интервью. **Institute of Service Science отпал: магистратура ISS для иностранцев закрыта** (только PhD — гайдлайны NTHU Fall 2026/Spring 2027), в ICDF не входит. NTHU-слоты теперь: IMBA (regular + ICDF-версия) + IMPISA (SE-профиль, тоже ICDF-партнёр).

### ⭐ Jerry Chou (周 from 資應所) — ПРИОРИТЕТ #4 (он директор программы IMS!)
- **Title:** Distinguished Professor (特聘教授), Director of Institute of Information Systems and Applications (資應所所長)
- **Email:** jchou@cs.nthu.edu.tw
- **Направление:** Distributed systems, cloud computing, resource management
- **Хук для письма:** Archon = multi-tenant платформа (Graph-per-Tenant, 50 изолированных схем PostgreSQL), OmniSearch = Control Plane / Compute Plane. Он распределёнщик + он ДОСТУП программы — короткое письмо "почему IMS, почему ваша лаборатория" сильно для admission.

### Chin-Yu Huang (黃金儒? no — 黃 from 資安)
- **Title:** Professor, Director of Institute of Information Security (資安所所長)
- **Email:** cyhuang@cs.nthu.edu.tw
- **Тел:** 03-5742972
- **Направление:** Software engineering, software reliability, software testing
- **Хук для письма:** Archon's reconciliation + evidence_files — это reliability-механика для LLM-извлечения. Software testing angle: как тестировать LLM-пайплайн детерминированно.

### Yi-Shin Chen (陳宜欣)
- **Title:** Professor
- **Email:** yishin@cs.nthu.edu.tw
- **Направление:** Web intelligence, data mining, big data
- **Хук для письма:** OmniSearch — data mining + поиск по большим мультимодальным архивам.

---

## 7. 🇹🇼 Тайвань — NTU (~~Global MBA~~ отпал 11.09.2026 — требует 2 года опыта)

> ⚠️ NTU GMBA отпал: официально требует Proof of Work Experience (2 года). Колледж Management NTU для свежего выпускника без китайского — тупик (BA/MBA и International Business — китайскоязычные, EMBA — 10 лет опыта, EiMBA — executive-трек; проверено 11.09.2026). Запасной вариант NTU: **SPE Leadership & Management** (all-English, но «tailored for experienced professionals» — до подачи уточнить письмом ntuspe@ntu.edu.tw, обязательность опыта в formal eligibility не указана). Письма в NTU CSIE теряют приоритет — тайваньский фокус теперь NTHU (IMBA + IMPISA). Профили ниже оставлены как запас.

### ⭐ Yun-Nung Chen (陳縈? no — 陳蘊? Vivian Chen) — лучший technical-мачч в NTU
- **Title:** Professor, CSIE (Machine Intelligence, Understanding, and Interaction Lab; Office 418)
- **Email:** yvchen@csie.ntu.edu.tw
- **Сайт:** https://www.csie.ntu.edu.tw/~yvchen/
- **Направление:** NLP, dialogue systems, LLM, RAG
- **Публикации (проверено DBLP):** "LLMs are Biased Evaluators But Not Biased for Fact-Centric Retrieval Augmented Generation" (ACL Findings 2025); "Creativity in LLM-based Multi-Agent Systems: A Survey" (EMNLP 2025); "LLM Inference Enhanced by External Knowledge: A Survey" (2025); "ICICLE: Expanding Retrieval with In-Context Documents" (2026); "TraceSafe: LLM Guardrails on Multi-Step Tool-Calling Trajectories" (2026); PairDistill — dense retrieval (EMNLP 2024)
- **Хук для письма:** Archon = RAG + tool-calling (MCP) для инженерных агентов. TraceSafe (guardrails на multi-step tool-calling) и fact-centric RAG — буквально мои проблемы: как заземлить агентов на Source of Truth.

### Wen-Huang Cheng (鄭文皇) — под GMBA Tech&Innovation
- **Title:** Professor & CSIE Chair (!), Office 420
- **Email:** wenhuang@csie.ntu.edu.tw
- **Направление:** AI, multimedia, CV, ML, **digital transformation, fintech**
- **Публикации (проверено):** SeCo — semantic-guided multimodal (ACM TOMM 2026)
- **Хук для письма:** двойной: (а) OmniSearch = multimodal AI; (б) digital transformation — язык GMBA. Как chair он делегирует — письмо короткое, с ask "к кому в GMBA/Service Science обратиться".

### Shou-De Lin (林守德)
- **Title:** Professor, CSIE (Machine Discovery and Social Network Mining Lab; Office 333)
- **Email:** sdlin@csie.ntu.edu.tw
- **Направление:** ML, knowledge discovery, data mining, NLP
- **Публикации (проверено DBLP):** LiveCLKTBench — cross-lingual knowledge transfer в multilingual LLMs (ACL 2026); PromptEmbedder — dual-LLM soft prompting (2026); uncertainty metrics for LLM target-aware search (EMNLP Findings 2025)
- **Хук для письма:** эмбеддинги + uncertainty — OmniSearch (Qdrant) и оценки уверенности LLM-extraction в Archon.

### Cheng-Fu Chou (周成福)
- **Title:** Professor, CSIE (Office 517)
- **Email:** ccf@csie.ntu.edu.tw
- **Направление:** Distributed ML systems, multimedia systems, performance evaluation
- **Хук для письма:** OmniSearch — распределённый ML-пайплайн (Kotlin Control / Go+Python Compute), performance evaluation — мой NFR-подход (<15ms traversal, 90% token saving).

### Jonathan Lee (李哲? no — Lee)
- **Title:** Professor, CSIE (Software Engineering Lab; Office 513)
- **Email:** jlee@csie.ntu.edu.tw
- **Направление:** Software engineering, service-oriented computing
- **Нюанс:** публикации давние (goal-driven RE, 2002-2010) — активность ниже; тематический мачч с service-oriented computing. Низкий приоритет письма.

---

## 8. Сводная таблица приоритетов (октябрь 2026)

| # | Профессор | Вуз/страна | Программа | Email | Мотив письма |
|---|---|---|---|---|---|
| 1 | **Zheng Haitao** | Tsinghua SIGS 🇨🇳 | Data Science & IT (CSC B) | zheng.haitao@sz.tsinghua.edu.cn | KG + LLM extraction ↔ Archon |
| 2 | **Xuanzhe Liu** | PKU SEI 🇨🇳 | MSc SE (CSC B) | liuxuanzhe@pku.edu.cn | RAG serving + agents ↔ Archon MCP |
| 3 | **Shin Yoo** | KAIST 🇰🇷 | MS Computing (GKS) | shin.yoo@kaist.ac.kr | LLM for SE ↔ Proof-of-Truth |
| 4 | **Jerry Chou** | NTHU 🇹🇼 | IMPISA/IMS (MOE/ICDF) — директор программы | jchou@cs.nthu.edu.tw | Distributed systems ↔ Archon/OmniSearch infra |
| 5 | Xia Shutao | Tsinghua SIGS 🇨🇳 | Data Science & IT (CSC B) | xiast@sz.tsinghua.edu.cn | Multimodal RAG ↔ OmniSearch |
| 6 | Ge Li | PKU SEI 🇨🇳 | MSc SE (CSC B) | lig@pku.edu.cn | Code generation ↔ archmap |
| 7 | In-Young Ko | KAIST 🇰🇷 | MS Computing (GKS) | iko@kaist.ac.kr | Orchestration ↔ archmap n8n |
| 8 | Hwang Junseok | SNU TEMEP 🇰🇷 | MS TEMEP (GKS) | junhwang@snu.ac.kr | AI diffusion ↔ Platform PM |
| 9 | Chin-Yu Huang | NTHU 🇹🇼 | IMPISA/IMS (MOE/ICDF) | cyhuang@cs.nthu.edu.tw | SE reliability ↔ Archon |
| 10 | **Lu Chen** | SJTU 🇨🇳 | CS (CSC B) — acceptance letter нужен до подачи | chenlusz@sjtu.edu.cn | Tool hallucination + hybrid RAG ↔ Proof-of-Truth |
| 11 | **Xiaodong Gu** | SJTU 🇨🇳 | CS, LLMSE (CSC B) — acceptance letter до подачи | xiaodong.gu@sjtu.edu.cn | Repo-level context ↔ Archon extraction |
| 12 | **Xin Xia** | ZJU 🇨🇳 | CS (CSC B) — Provisional Acceptance = priority | xxia@zju.edu.cn | AI4SE + Huawei ex-Chief Expert ↔ Platform PM |
| 13 | **Wen Zhang** | ZJU 🇨🇳 | CS, ZJUKG (CSC B) | zhang.wen@zju.edu.cn | Multi-modal KG ↔ OmniSearch + Archon |
| 14 | Yun-Nung Chen | NTU CSIE 🇹🇼 | ~~GMBA~~ (низкий приоритет после отпадения GMBA) | yvchen@csie.ntu.edu.tw | RAG + tool-calling ↔ Archon |
| 15 | Wen-Huang Cheng | NTU CSIE 🇹🇼 | ~~GMBA Tech&Innov~~ (низкий приоритет) | wenhuang@csie.ntu.edu.tw | Multimodal AI + digital transformation |
| 16 | Shou-De Lin | NTU CSIE 🇹🇼 | ~~NTU SPE L&M~~ (низкий приоритет) | sdlin@csie.ntu.edu.tw | Embeddings + uncertainty |
| 17 | Beijun Shen | SJTU 🇨🇳 | CS, LLMSE (CSC B) — запасной после Gu | bjshen@sjtu.edu.cn | Code interpretation ↔ AST extraction |
| 18 | Huajun Chen | ZJU 🇨🇳 | CS, ZJUKG (CSC B) — после Xia/Zhang | huajunsir@zju.edu.cn | KG+LLM integration ↔ Archon |

**План писем (⚠️ сдвинуто на сентябрь 2026 из-за дедлайнов вузов):**
- **Волна 1 (СЕЙЧАС, сентябрь 2026):** Zheng Haitao (Tsinghua), Xuanzhe Liu (PKU) — критично для CSC Type B, до подачи mid-Dec.
- **Волна 2 (конец сентября 2026):** Shin Yoo (KAIST), Jerry Chou (NTHU — директор IMPISA/IMS), Hwang Junseok (SNU) + **Lu Chen и Xiaodong Gu (SJTU — ⚠️ acceptance letter обязателен до подачи ~15.12!)** и **Xin Xia / Wen Zhang (ZJU — Provisional Acceptance = priority)**. KAIST-гайд прямо рекомендует найти advisor в SoC ДО подачи (RA-финансирование от его грантов) — Shin Yoo важнее, чем казалось.
- **Волна 3 (октябрь 2026 / если ответов нет — дублировать профессорам #5-7):** Xia Shutao, Ge Li, In-Young Ko, Yun-Nung Chen, Beijun Shen (если Gu молчит), Huajun Chen (если Xia/Zhang молчат).
- Тайвань-письма — shortest (MOE/ICDF не требуют), США-стиль: 150-200 слов. Для IMBA письмо профессору не критично (оценка по документам) — Jerry Chou важнее для IMPISA.
- **✅ Драфты всех писем волны 1-2 готовы (включая SJTU/ZJU):** `letters_drafts_2027.md` — Zheng Haitao, Xuanzhe Liu, Shin Yoo, Jerry Chou, Hwang Junseok, Lu Chen, Xiaodong Gu, Xin Xia, Wen Zhang + заготовки ответов на вопросы профессоров + аски acceptance letter (SJTU) / Provisional Acceptance (ZJU).

---

## 9. Чеклист к письму (для каждого)

- [ ] Прочитать 1-2 статьи профессора (из колонки «Публикации») — указать их в письме по названию
- [ ] GitHub Archon: README на английском + бейджи (stars, CI) — проверить перед письмом
- [ ] CV 1 страница EN: GPA 3.93/5.0, Archon/OmniSearch/archmap с метриками (<15ms, 50 tenants, 90% tokens, 4 products/25 repos)
- [ ] Тема письма: `Prospective Master's Student Fall 2027 — AI-native Architecture (Archon: KG + RAG + MCP)` — или проще: `Prospective CSC applicant Fall 2027 — question about your lab`
- [ ] Не просить "funding" в первом письме — просить о разговоре/ответе; funding = CSC/GKS/MOE в заявке
- [ ] Отправлять вт: ср–чт утром по местному времени вуза

---

## 10. Источники (проверено 10.09.2026)

- Tsinghua SIGS: https://www.sigs.tsinghua.edu.cn (профили Zheng Haitao, Xia Shutao)
- PKU SEI: https://www.sei.pku.edu.cn (roster Faculty.htm, стр. 1-5)
- KAIST Computing: faculty + 소프트웨어디자인 division (emails декодированы с "(at)")
- SNU TEMEP: temep.snu.ac.kr (Hwang Junseok profile)
- NTHU: dcs.site.nthu.edu.tw (professor pages)
- NTU CSIE: https://www.csie.ntu.edu.tw/en/member/Faculty
- DBLP (проверка публикаций 2024-2026): dblp.org
