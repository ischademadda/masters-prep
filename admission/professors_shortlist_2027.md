# Шортлист профессоров — осень 2027 (Тайвань / Китай)

> **Обновлено:** 09.11.2026. Данные о профессорах и публикациях проверены 10–11.09.2026 (официальные страницы кафедр, DBLP). Статус писем ведётся в `README.md`, раздел 4. Тексты писем: `letters_2027.md`.
> **Не хватает (подобрать):** 🇹🇼 NYCU CS, 🇹🇼 NCKU CSIE, средние вузы Китая (🇨🇳 UESTC, 🇨🇳 SCU, 🇨🇳 HIT Shenzhen) по KG / RAG / LLM для SE.

---

## 1. Стратегия писем

| Куда | Нужны ли письма? | Формат |
|---|---|---|
| **Китай (CSC Type B — 1 вуз; SGS для Шанхая)** | ✅ **Критично**: ответ профессора решает, куда уходит единственная заявка CSC | Письмо + CV + короткий research pitch; просить о встрече/ответе, в идеале — supporting letter к заявке |
| **Тайвань (🇹🇼 NTU / 🇹🇼 NYCU / 🇹🇼 NTHU / 🇹🇼 NCKU)** | ⚠️ Желательно, не обязательно: приём по документам (знакомая поступила в 🇹🇼 NTU и 🇹🇼 NTHU без писем) | Короткое письмо, 150–200 слов: 1–2 профессорам на вуз |

**Правило:** писать 2 письма за один раз нельзя в один вуз — сначала приоритетный, через 1-2 недели без ответа — второй.

**Скелет письма (октябрь 2026):**
1. Кто я: 4th-year SE @ TPU, GPA 3.93/5.0, Team Lead R&D lab (team v3.9), стажировка T-Bank (System Analyst, Junior+).
2. Что сделал: Archon (KG + LLM extraction + MCP), OmniSearch (multimodal RAG), archmap (C4-генерация, ~40 репозиториев, ~15 мин на репозиторий).
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
- **Хук для письма:** OmniSearch — multimodal RAG над видеоархивами (Whisper + CLIP + Qdrant), сценарий промышленной безопасности (обмен опытом с Gazprom Vostok Neft, без внедрения). Плюс его интерес к AI security ↔ Archon's Proof-of-Truth как защита от LLM-галлюцинаций.
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

## 3a. 🇨🇳 Китай — SJTU School of Computer Science (деньги: SGS, не CSC)

> По официальному гиду 2026 acceptance letter до подачи обязателен для **PhD**, для магистратуры не подтверждено ⚠️ (вопрос: gs.admission@sjtu.edu.cn). Согласие профессора всё равно сильно помогает, в том числе для SGS.

### ⭐ Lu Chen (陈璐) — ПРИОРИТЕТ (равен волне 2)
- **Title:** Associate Professor, X-LANCE Lab
- **Email:** chenlusz@sjtu.edu.cn (верифицирован: chen.lu/en/)
- **Направление:** LLMs, agentic systems, AI for Science, RAG
- **Публикации (проверено):** NeuSym-RAG — hybrid neural-symbolic retrieval (ACL 2025); "Heads up! LLMs, Reducing Tool Hallucination via Reliability Alignment" (ICML 2025); task-specific data selection (NeurIPS 2025)
- **Хук для письма:** Прямое пересечение: статья про tool hallucination reduction — это Proof-of-Truth в постановке лабы; NeuSym-RAG (нейро-символный гибрид) — это Archon (AST-детерминизм + LLM-семантика) в retrieval-форме. OmniSearch — мультимодальный RAG-кейс для лабы.

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

## 3b. 🇨🇳 Китай — ZJU College of Computer Science (CSC Type B, ~31.12 ⚠️)

> Form for Provisional Acceptance of International Student by 🇨🇳 ZJU Supervisor — даёт **priority** (не строго обязательно). Контакт в сентябре-октябре.

### ⭐ Xin Xia (夏鑫) — ПРИОРИТЕТ (волна 2-3)
- **Title:** Qiushi Distinguished Professor; ex-Huawei Chief Expert (2021-2025); ACM Distinguished Member; ACM SIGSOFT Early Career Award 2022
- **Email:** xin.xia@zju.edu.cn (верифицирован: xin-xia.github.io)
- **Направление:** AI4SE / SE4AI, program comprehension, empirical SE
- **Публикации:** 360+ публикаций, 160+ CCF-A
- **Хук для письма:** Идеальный мачч под Platform PM трек: его Huawei-бэкграунд = индустриальный масштаб; Archon — серьёзно спроектированная система (7 ADR, NFR), а его empirical-подход — способ честно её измерить. Он набирает команду после перехода из Huawei — момент удачный.

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

## 4. 🇹🇼 Тайвань — NTHU (CS / IMPISA, IMBA запасной)

> 🇹🇼 NTHU: основной трек CS / IMPISA, IMBA (менеджмент) запасной. Подача ожидается с середины декабря до конца февраля/марта ⚠️. Institute of Service Science закрыт для иностранцев-магистрантов.

### ⭐ Jerry Chou — директор программы IMS
- **Title:** Distinguished Professor (特聘教授), Director of Institute of Information Systems and Applications (資應所所長)
- **Email:** jchou@cs.nthu.edu.tw
- **Направление:** Distributed systems, cloud computing, resource management
- **Хук для письма:** Archon = multi-tenant платформа (Graph-per-Tenant, 50 изолированных схем PostgreSQL), OmniSearch = Control Plane / Compute Plane. Он распределёнщик + он ДОСТУП программы — короткое письмо "почему IMS, почему ваша лаборатория" сильно для admission.

### Chin-Yu Huang
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

## 5. 🇹🇼 Тайвань — NTU CSIE

> **09.11.2026: 🇹🇼 NTU снова приоритет** (Тайвань стал основным слоем). GMBA отпал (нужно 2 года опыта), подаём на **CSIE**: 2-й раунд 01.12.2026–19.01.2027. Первой писать Yun-Nung Chen.

### ⭐ Yun-Nung Chen (Vivian Chen) — лучший мэтч в 🇹🇼 NTU, писать первой
- **Title:** Professor, CSIE (Machine Intelligence, Understanding, and Interaction Lab; Office 418)
- **Email:** yvchen@csie.ntu.edu.tw
- **Сайт:** https://www.csie.ntu.edu.tw/~yvchen/
- **Направление:** NLP, dialogue systems, LLM, RAG
- **Публикации (проверено DBLP):** "LLMs are Biased Evaluators But Not Biased for Fact-Centric Retrieval Augmented Generation" (ACL Findings 2025); "Creativity in LLM-based Multi-Agent Systems: A Survey" (EMNLP 2025); "LLM Inference Enhanced by External Knowledge: A Survey" (2025); "ICICLE: Expanding Retrieval with In-Context Documents" (2026); "TraceSafe: LLM Guardrails on Multi-Step Tool-Calling Trajectories" (2026); PairDistill — dense retrieval (EMNLP 2024)
- **Хук для письма:** Archon = RAG + tool-calling (MCP) для инженерных агентов. TraceSafe (guardrails на multi-step tool-calling) и fact-centric RAG — буквально мои проблемы: как заземлить агентов на Source of Truth.

### Wen-Huang Cheng (鄭文皇)
- **Title:** Professor & CSIE Chair (!), Office 420
- **Email:** wenhuang@csie.ntu.edu.tw
- **Направление:** AI, multimedia, CV, ML, **digital transformation, fintech**
- **Публикации (проверено):** SeCo — semantic-guided multimodal (ACM TOMM 2026)
- **Хук для письма:** OmniSearch = multimodal AI. Как chair он делегирует: письмо короткое, с вопросом, к кому из коллег обратиться.

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
- **Хук для письма:** OmniSearch — распределённый ML-пайплайн (Kotlin Control / Go+Python Compute), performance evaluation — мой NFR-подход (целевые <100ms traversal, экономия токенов — предстоит измерить).

### Jonathan Lee
- **Title:** Professor, CSIE (Software Engineering Lab; Office 513)
- **Email:** jlee@csie.ntu.edu.tw
- **Направление:** Software engineering, service-oriented computing
- **Нюанс:** публикации давние (goal-driven RE, 2002-2010) — активность ниже; тематический мачч с service-oriented computing. Низкий приоритет письма.

---

## 6. Приоритет писем (09.11.2026)

| Приоритет | Профессор | Вуз | Email | Хук |
|---|---|---|---|---|
| Отправлено | Zheng Haitao | 🇨🇳 Tsinghua SIGS | zheng.haitao@sz.tsinghua.edu.cn | KG + LLM extraction ↔ Archon |
| Отправлено | Xuanzhe Liu | 🇨🇳 PKU SEI | liuxuanzhe@pku.edu.cn | RAG serving + agents ↔ Archon MCP |
| Отправлено | Lu Chen | 🇨🇳 SJTU (деньги: SGS) | chenlusz@sjtu.edu.cn | Tool hallucination + hybrid RAG ↔ Proof-of-Truth |
| Отправлено ⚠️ | Xiaodong Gu | 🇨🇳 SJTU (SGS) | xiaodong.gu@sjtu.edu.cn | Repo-level context ↔ Archon extraction |
| Отправлено ⚠️ | Xin Xia | 🇨🇳 ZJU | xin.xia@zju.edu.cn | AI4SE |
| Отправлено ⚠️ | Wen Zhang | 🇨🇳 ZJU | zhang.wen@zju.edu.cn | Multi-modal KG ↔ OmniSearch + Archon |
| Отправлено ⚠️ | Jerry Chou | 🇹🇼 NTHU | jchou@cs.nthu.edu.tw | Distributed systems ↔ multi-tenant Archon |
| **1** | **Yun-Nung Chen** | **🇹🇼 NTU CSIE** | yvchen@csie.ntu.edu.tw | RAG + tool-calling (TraceSafe) ↔ Archon MCP |
| 2 | Shou-De Lin | 🇹🇼 NTU CSIE | sdlin@csie.ntu.edu.tw | Embeddings + uncertainty |
| 2 | Chin-Yu Huang | 🇹🇼 NTHU | cyhuang@cs.nthu.edu.tw | SE reliability ↔ Proof-of-Truth |
| 2 | — | 🇹🇼 NYCU CS, 🇹🇼 NCKU CSIE | подобрать | — |
| 3 | Xia Shutao | 🇨🇳 Tsinghua SIGS | xiast@sz.tsinghua.edu.cn | Multimodal RAG ↔ OmniSearch |
| 3 | Ge Li | 🇨🇳 PKU SEI | lig@pku.edu.cn | Code generation ↔ archmap |
| 3 | Beijun Shen | 🇨🇳 SJTU | bjshen@sjtu.edu.cn | После Gu, если тишина |
| 3 | Huajun Chen | 🇨🇳 ZJU | huajunsir@zju.edu.cn | После Xia/Zhang, если тишина |
| 3 | Cheng-Fu Chou, Wen-Huang Cheng, Yi-Shin Chen | 🇹🇼 NTU / 🇹🇼 NTHU | см. выше | Запас |

⚠️ = отправка 28–29.10 по плану, не подтверждена.

---

## 7. Чеклист к письму

- [ ] Прочитать 1-2 статьи профессора (из колонки «Публикации») — указать их в письме по названию
- [ ] GitHub Archon: README на английском + бейджи (stars, CI) — проверить перед письмом
- [ ] CV 1 страница EN: только цифры из `cv/cv_en.html` (archmap ~40 репо, ~15 мин/репо); Archon: честный статус
- [ ] Тема письма: `Prospective Master's Student Fall 2027 — AI-native Architecture (Archon: KG + RAG + MCP)` — или проще: `Prospective CSC applicant Fall 2027 — question about your lab`
- [ ] Не просить funding в первом письме. Просить ответ или разговор, деньги идут через CSC / SGS / MOE / стипендию вуза
- [ ] Отправлять вт: ср–чт утром по местному времени вуза

---

## 8. Источники (проверено 10.09.2026)

- 🇨🇳 Tsinghua SIGS: https://www.sigs.tsinghua.edu.cn (профили Zheng Haitao, Xia Shutao)
- 🇨🇳 PKU SEI: https://www.sei.pku.edu.cn (roster Faculty.htm, стр. 1-5)
- 🇹🇼 NTHU: dcs.site.nthu.edu.tw (professor pages)
- 🇹🇼 NTU CSIE: https://www.csie.ntu.edu.tw/en/member/Faculty
- DBLP (проверка публикаций 2024-2026): dblp.org
