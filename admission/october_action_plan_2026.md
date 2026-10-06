# Операционный план действий: Октябрь 2026

> **Владелец:** Денис Штэпа  
> **Статус:** Активно (6–15 октября 2026)  
> **Главный фокус:** Письма профессорам первой волны (Китай), бронь IELTS в Чэнду, документы ТПУ.

---

## 1. Срочные шаги на эту неделю (Чек-лист)

- [ ] **Шаг 1:** Сгенерировать `Denis_Shtepa_CV.pdf` из [`cv_en.html`](file:///Users/shteppinson/mylife/maga/admission/cv_en.html) — CV уже переведен в research-вариант, осталось только `Cmd+P → Save as PDF`.
- [ ] **Шаг 2:** Отправить письмо профессору **Zheng Haitao** (Tsinghua SIGS) — *утром в будний день (04:00–06:00 по Томску / 08:00–10:00 по Китаю)*.
- [ ] **Шаг 3:** Отправить письма профессорам **Xuanzhe Liu** (PKU) и **Lu Chen** (SJTU) — **не в один день с шагом 2**, интервал 2 дня между письмами.
- [ ] **Шаг 4:** Зарегистрировать аккаунт на **[ielts.neea.cn/en/](https://ielts.neea.cn/en/)** и забронировать слот в Чэнду на **4–5 декабря 2026**.
- [ ] **Шаг 5:** Заказать в деканате ТПУ выписку оценок за 3 курса с расчетом GPA и печатью.
- [ ] **Шаг 6:** Предупредить научрука в ТПУ и ментора/лида в Т-Банке о двух рекомендательных письмах.

---

## 2. Как сделать CV в PDF за 10 секунд

1. Открой файл [`admission/cv_en.html`](file:///Users/shteppinson/mylife/maga/admission/cv_en.html) в браузере (Google Chrome или Safari).
2. Нажми сочетание клавиш **`Cmd + P`** (Печать).
3. В диалоговом окне:
   * **Принтер / Назначение:** *Сохранить как PDF (Save as PDF)*.
   * **Размер бумаги:** *A4*.
   * **Поля (Margins):** *По умолчанию (Default)* или *Минимальные*.
   * **Параметры:** снять галочку с *«Колонтитулы (Headers and footers)»*.
4. Сохрани файл как **`Denis_Shtepa_CV.pdf`** в папку `admission/`.

> Что уже исправлено в CV (06.10.2026): заголовок → `Research-Oriented System Designer & Team Lead — AI-Native Architecture (KG / MCP / RAG)`, summary → `Research-oriented...`, GPA → `3.93/5.0 — Top 10%, ~3.5/4.0`, английский → `IELTS 7.5 expected Dec 2026`, T-Bank → `Apr 2026 — Aug 2026 (Internship, Full-Cycle System Design)`, GitHub — один линк.

---

## 3. Письма профессорам (Волна 1: Китай CSC Type B)

> **Тактика отправки:** День 1 — Zheng (Tsinghua), День 3 — Liu (PKU), День 5 — Chen (SJTU). Не залпом — чтобы успеть подправить шаблон если первый ответит с замечанием. Отправка только с Gmail, plain text, PDF <1MB.

### 3.1. Письмо №1: Zheng Haitao — Tsinghua SIGS (Приоритет №1)

* **Кому (To):** `zheng.haitao@sz.tsinghua.edu.cn`
* **Тема (Subject):** `Prospective Master's Student Fall 2027 — Knowledge Graph Grounding for AI Agents (Archon)`
* **Вложение (Attachment):** `Denis_Shtepa_CV.pdf`
* **Тайминг:** Будний день, 08:00–10:00 утра по Пекину (04:00–06:00 утра по Томску).

```text
Dear Professor Zheng,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia) and Team Lead of our R&D lab. I am writing to ask whether you would consider supervising a master's student for Fall 2027, as I plan to apply to the Data Science and Information Technology program at Tsinghua SIGS (CSC scholarship).

My diploma project, Archon, is an AI-native Source of Truth platform that keeps architectural knowledge synchronized with code and delivers verified context to AI agents via MCP. Its core is a multi-tenant Knowledge Graph on PostgreSQL 16 + Apache AGE (50 isolated tenant schemas, impact-analysis traversal <15ms at depth 4) populated by a hybrid pipeline: deterministic AST parsing (Tree-sitter) plus two-phase LLM extraction with a "Proof-of-Truth" rule — every graph edge must carry evidence_files with file paths and line numbers, otherwise it is discarded. This cut LLM token consumption by 90% while keeping extraction verifiable.

I have read your work on knowledge graph completion and RLHF-V (CVPR 2024), and I see a direct continuation of my interests: my Proof-of-Truth rule is essentially a grounding constraint on LLM output, and scaling it from 50 to 500+ tenants raises exactly the completion-and-consistency questions your group studies. Separately, I shipped archmap, an LLM-based C4 diagram generator adopted for 4 products (~25 repos) at T-Bank, and OmniSearch, a multimodal RAG video-search system (Whisper/CLIP/Qdrant) deployed by Gazprom Neft.

My CV is attached. I would be grateful for a brief reply on whether my profile fits your lab's plans for Fall 2027 — and whether you would be open to a short call.

Thank you for your time.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

---

### 3.2. Письмо №2: Xuanzhe Liu — Peking University (PKU SEI)

* **Кому (To):** `liuxuanzhe@pku.edu.cn`
* **Тема (Subject):** `Prospective Master's Student Fall 2027 — MCP Agent Context on Top of LLM Serving (Archon)`
* **Вложение:** `Denis_Shtepa_CV.pdf`

```text
Dear Professor Liu,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia), Team Lead of our R&D lab. I plan to apply to the MSc Software Engineering program at PKU for Fall 2027 (CSC scholarship) and would be honored to work in your group.

My diploma project, Archon, is an AI-native Source of Truth platform for enterprise architecture. Its core is a multi-tenant Knowledge Graph (PostgreSQL + Apache AGE) fed by a hybrid pipeline — deterministic AST parsing plus two-phase LLM extraction where a File Selector agent reads only file trees (90% token savings) and every extracted edge must present evidence_files, or it is discarded. The graph is then served to engineering AI agents through MCP: agents ask "what breaks if I change this API" and get traversal-backed answers (<15ms at depth 4) instead of hallucinating from stale docs.

Your work is the natural next layer under this system: RAGCache (TOCS 2026) and Pythia address exactly the serving economics of RAG-heavy, agent-native workloads that Archon pushes onto the infrastructure, and BAMAS (AAAI 2026) formalizes the multi-agent budget allocation I currently handle with ad-hoc heuristics. I would love to research how agent-context platforms like Archon should co-design with the LLM serving stack — e.g., what a "context-serving tier" between vector stores and application agents should look like.

Previously I shipped archmap (LLM-based C4 generation, 4 products/~25 repos at T-Bank) and OmniSearch (multimodal RAG: Whisper/CLIP/Qdrant, Control/Compute plane split).

My CV is attached. Would my profile fit your lab for Fall 2027? I would gladly schedule a call at your convenience.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

---

### 3.3. Письмо №3: Lu Chen — Shanghai Jiao Tong University (SJTU School of CS)

> ⚠️ **Критично:** SJTU требует *Acceptance Letter* от профессора **до** подачи заявки!

* **Кому (To):** `chenlusteve@sjtu.edu.cn`
* **Тема (Subject):** `Prospective Master's Student Fall 2027 — Knowledge-Grounded Dialogues (Archon)`
* **Вложение:** `Denis_Shtepa_CV.pdf`

```text
Dear Professor Chen,

I am Denis Shtepa, a final-year BSc Software Engineering student at Tomsk Polytechnic University (Russia) and Team Lead of our R&D lab. I am preparing my application for the Master in Computer Science and Technology program at SJTU (CSC Type B, agency 10248) and am seeking your supervision for Fall 2027.

My diploma project, Archon, is an AI-native Source of Truth platform for architecture knowledge. It extracts a multi-tenant Knowledge Graph from codebases (AST + LLM with a line-level Proof-of-Truth constraint) and serves structured subgraphs to AI agents via MCP. Agents query it in natural language to evaluate breaking changes, resolving queries via graph traversals (<15ms at depth 4) rather than unstructured vector search.

I have followed your work at X-LANCE on robust dialogue state tracking and knowledge-grounded generation. Archon's core challenge — keeping agent interactions strictly grounded in verified enterprise facts without hallucinating unproven architectural links — directly mirrors your group's research into grounded conversation and domain-specific knowledge integration. Additionally, I led OmniSearch (multimodal RAG video search for Gazprom Neft) and archmap (automated C4 diagram platform at T-Bank, scaled to 25 repos).

Since SJTU School of CS requires prospective applicants to secure provisional supervision, could you let me know if my profile aligns with your group's priorities for Fall 2027? My CV is attached.

Thank you very much for your consideration.

Best regards,
Denis Shtepa
Email: ischademadda@gmail.com | GitHub: github.com/ischademadda | CV attached
```

---

## 4. Бронь IELTS on Computer в Чэнду (3–8 декабря)

1. **Портал:** [ielts.neea.cn/en/](https://ielts.neea.cn/en/) (English version).
2. **Тип документа:** *Passport (Загранпаспорт РФ)*.
3. **Город тестирования:** *Chengdu (Sichuan)*.
4. **Тест-центр:** *British Council Chengdu Computer-delivered Test Centre (Times Plaza)* или *Sichuan University*.
5. **Целевые даты:** **4 декабря (пятница) или 5 декабря (суббота) 2026**.
6. **Стоимость:** 2 170 RMB (оплата через QR-код Alipay / карта друга или зарубежная карта).

---

## 5. Бюрократия ТПУ (Справки и рекомендации)

### Выписка оценок:
* Заказать в деканате ИШИТР ТПУ: **Академическая справка (выписка оценок за все 3 курса с расчетом GPA и гербовой печатью)**.
* После получения — отдать в бюро переводов в Томске на **нотариальный перевод на английский язык**.

### Рекомендатели (Скрипты сообщений):

* **Научному руководителю в ТПУ:**
  > *«Здравствуйте, [Имя Отчество]! Я планирую подавать документы на стипендию правительства Китая (CSC) в магистратуру Цинхуа и Пекинского университета (дедлайн середина декабря). Мне потребуется академическое рекомендательное письмо на английском языке с акцентом на наш дипломный проект Archon и исследовательскую работу. Я сам подготовлю полный драфт текста и форму рекомендации в ноябре, от вас потребуется только проверить и подписать. Будете ли вы готовы меня порекомендовать?»*

* **Тимлиду / Ментору в Т-Банке:**
  > *«Привет, [Имя]! Я подаюсь в магистратуру в Азию (Цинхуа / NTHU) на осень 2027. Для заявки на грант нужны две рекомендации, в том числе с места работы. Можно ли попросить у тебя рекомендательное письмо как от работодателя? Акцент сделаем на системный анализ, самостоятельный запуск платформы archmap на 25 репозиториев и продуктовое лидерство. Текст на английском я полностью напишу сам в ноябре, от тебя нужно будет только согласование и подпись.»*
