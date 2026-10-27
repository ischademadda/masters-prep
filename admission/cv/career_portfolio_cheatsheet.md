# 🎯 Шпаргалка: Карьерное портфолио, метрики и STAR-кейсы

> **Владелец:** Денис Штэпа  
> **Назначение:** Единый источник проверенных цифр, метрик и архитектурных решений для **Study Plans, Motivation Letters, Cold Emails профессорам, интервью и резюме**.  
> **Ключевые профили:**
> - Platform / Technical PM & System Designer (AI-Native Architecture, Knowledge Graphs, MCP)
> - Platform Engineer / DevOps Lead (GitLab CI/CD, Kubernetes, Docker, Nginx, Temporal, Git Flow)
>
> **Файлы резюме:**
> - **DevOps / Platform (RU):** [cv_devops_ru.html](file:///Users/shteppinson/mylife/maga/admission/cv/cv_devops_ru.html) (готов к печати в 1 страницу A4), [cv_devops_ru.md](file:///Users/shteppinson/mylife/maga/admission/cv/cv_devops_ru.md), PDF: [Denis_Shtepa_DevOps_CV.pdf](file:///Users/shteppinson/mylife/maga/admission/cv/Denis_Shtepa_DevOps_CV.pdf)
> - **Technical PM / System Design (RU):** [cv_technical_pm_ru.md](file:///Users/shteppinson/mylife/maga/admission/cv/cv_technical_pm_ru.md)
> - **Masters / Academic (EN):** [cv_en.html](file:///Users/shteppinson/mylife/maga/admission/cv/cv_en.html), [cv_en.md](file:///Users/shteppinson/mylife/maga/admission/cv/cv_en.md), PDF: [Denis_Shtepa_CV.pdf](file:///Users/shteppinson/mylife/maga/admission/cv/Denis_Shtepa_CV.pdf)

---

## 1. 📊 Матрица оцифрованных результатов (Impact Cheat Sheet)

| Проект / Место | Роль | Метрика / Результат | Ключевой стек |
|---|---|---|---|
| **archmap**<br>*(Т-Банк)* | Founder & Product Owner | • Доставка C4-диаграмм: **с 1–3 дней до 15 минут** (−98% времени).<br>• Онбординг инженеров в архитектуру: **с недель до часов**.<br>• Масштабирование: **4 продукта / ~25 микросервисных репозиториев**.<br>• Оркестрация: n8n + бот в один клик. | Python, LikeC4, AST Tree-sitter, LLM (File Selector → Extractor), n8n, CI/CD |
| **Archon**<br>*(Диплом, R&D Lab — в разработке: архитектура + базовый каркас)* | Lead System Architect & Product Owner | • Архитектурная декомпозиция: **17 логических модулей → 3 полиглотных сервиса** (Temporal Workflows, ADR-0007).<br>• Проектирование: **7 ADR зафиксировали ключевые архитектурные развилки до реализации ядра**.<br>• Knowledge Graph: изоляция Graph-per-Tenant на PostgreSQL + Apache AGE, NFR на обход графа: глубина 4 за **<100 мс** (предстоит проверить бенчмарком).<br>• **Правило Proof-of-Truth**: каждая связь графа обязана иметь подтверждение в коде, иначе отсекается.<br>• Процессы: **37 задач в GitHub Projects**, Docs-as-Code (AGENTS.md). | Kotlin, Python, Temporal, PostgreSQL 16 + Apache AGE, Qdrant, LikeC4, MCP |
| **OmniSearch Engine**<br>*(R&D, Газпромнефть-Восток)* | Product Owner & System Architect | • Разделение Control Plane (Kotlin Ktor) и Compute Plane (Go / Python).<br>• Спроектирован конечный автомат (FSM) статусов видео и on-premise стек (MinIO S3 + Qdrant).<br>• Проектирование под сценарии промышленного видеомониторинга; обмен опытом со специалистами Газпромнефть-Восток. | Kotlin Ktor, Go (GoCV/FFmpeg), Python (Whisper/CLIP), Qdrant, MinIO S3 |
| **Кобрендинг Т-ОРД**<br>*(Т-Банк)* | System Analyst (Junior+) | • Интеграция **3 внешних систем с разными REST-контрактами**.<br>• Спецификации согласованы с учетом обратной совместимости API: **фича в проде без интеграционных блокеров**. | REST API, OpenAPI, PostgreSQL, JSON API, Reverse Compatibility |
| **Операционные процессы**<br>*(Т-Банк)* | System Analyst | • Анализ **~145 инцидентов дежурств** → рефакторинг ранбуков → **время ответа (MTTR) −40%**.<br>• Шаблон сервисной документации для 2 команд: онбординг сокращён с 3 дней до 1 дня.<br>• BotControl: сравнительный анализ вариантов → быстрый MVP с конверсией отклика 50%. | Confluence, Jira, Runbooks, Service Blueprints |
| **CRDT-Engine**<br>*(Solo Open-Source)* | System Designer | • Real-time коллаборативный движок со Strong Eventual Consistency.<br>• Sequence CRDT (Fugue) + LWW-Register + векторные часы.<br>• Горизонтальное масштабирование через Redis Pub/Sub и шардирование по `document_id`. | Go, WebSockets, Redis Pub/Sub, Clean Architecture |
| **Корпоративная Wiki**<br>*(МТС True Tech Hack)* | DevOps / Infra Engineer | • Спроектирован и развернут мультисервисный деплой (Java Spring Boot, Go, Python ML, Postgres) за 5 дней хакатона.<br>• Настроен GitHub Actions CI/CD и Nginx маршрутизация.<br>• Интеграция с MWS Tables API. | Docker, Docker Compose, GitHub Actions, Nginx, Java Spring, Go, Python, MWS |

---

## 2. 🎙️ Готовые STAR-кейсы для эссе и интервью

### Кейс 1: Выбор физической топологии процессов и декомпозиция (ADR-0007)
* **Situation:** Архитектурный домен Archon включал 17 логических модулей (AST-парсер, Knowledge Graph, LLM-экстрактор, reconciler, portal и др.). Система изначально проектировалась как распределенная, но требовалось определить модель физического развертывания под ресурсы небольшой команды (4 инженера).
* **Task:** Найти баланс между модульностью и эксплуатационными накладными расходами, избежав оверхеда на поддержку 17 отдельных контейнеров в Kubernetes и сохранив полиглотность стека (JVM, Python, Node).
* **Action:** Формализовал развилку в ADR-0007: сгруппировал логические модули в 3 физических сервиса (Portal на React, Core Engine на Kotlin, AI Node на Python) с оркестрацией распределенных сценариев через Temporal Polyglot Workflows.
* **Result:** Ещё до написания ядра у команды есть план деплоя, посильный для 4 человек: 3 сервиса вместо 17, без сетевого оверхеда, с сохранением разделения ответственности модулей и возможностью отдельно масштабировать ML-нагрузку.

### Кейс 2: Борьба с галлюцинациями LLM и оптимизация токеномики (Proof-of-Truth)
* **Situation:** LLM при извлечении архитектурных связей из кода склонна додумывать несуществующие зависимости. Для графа, которому должны доверять инженеры и AI-агенты, это неприемлемо; кроме того, отправлять в модель весь репозиторий дорого.
* **Task:** Заложить в архитектуру достоверность графа знаний и разумный расход токенов ещё на этапе проектирования.
* **Action:** Я спроектировал двухфазный пайплайн: детерминированный статический анализ через AST Tree-sitter + строгий протокол **Proof-of-Truth**. Каждое ребро графа обязано содержать точные `evidence_files` (путь к файлу и номера строк). Любая связь без подтверждения отбрасывается валидатором.
* **Result:** Правило зафиксировано в архитектуре и контракте извлечения до начала реализации. Реальный эффект (precision/recall связей, расход токенов) предстоит измерить на реализации; это же — готовый исследовательский вопрос для магистратуры.

### Кейс 3: Продуктовая инициатива из неструктурированного запроса (archmap)
* **Situation:** Руководитель направления в Т-Банке упомянул проблему: архитектурные схемы в Confluence устаревают быстрее, чем их успевают обновлять, а разработчики тратят до 3 дней на ручную отрисовку C4.
* **Task:** Превратить абстрактную боль в работающий автоматизированный продукт.
* **Action:** Я не стал ждать ТЗ сверху. Самостоятельно инициировал продукт archmap: написал RFC, спроектировал двухфазный пайплайн (File Selector → Extractor) на Python, интегрировал генерацию LikeC4 в CI/CD и вывел запуск через Telegram-бота в один клик.
* **Result:** Время генерации архитектурной схемы упало с 1–3 дней до 15 минут. Руководство одобрило масштабирование решения на 4 продукта (~25 микросервисных репозиториев).

---

## 3. 🎯 Формулировки позиционирования под гранты

### Для Китая (CSC Type B — Tsinghua SIGS, PKU, SJTU):
> *"Research-oriented System Designer & Team Lead focused on AI-native Developer Platforms. Background in deterministic-LLM hybrid pipelines (Tree-sitter + Knowledge Graphs on Apache AGE) and Context Engineering via Model Context Protocol (MCP). Built archmap at T-Bank (adopted across 25 microservice repos); now designing Archon, a verifiable code-to-architecture Knowledge Graph platform (diploma project)."*

### Для Тайваня (ICDF / MOE — NTHU IMBA / IMPISA):
> *"Technical Product Manager & R&D Team Lead (team v39) with a proven track record of shipping developer tools from 0 to 1. Proven impact in reducing architectural delivery cycle times by 98% (archmap), leading cross-functional engineering teams, and aligning business requirements with scalable distributed architectures."*
