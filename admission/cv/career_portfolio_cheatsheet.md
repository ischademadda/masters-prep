# 🎯 Шпаргалка: Карьерное портфолио, метрики и STAR-кейсы

> **Владелец:** Денис Штэпа  
> **Назначение:** Единый источник проверенных цифр, метрик и архитектурных решений для **Study Plans, Motivation Letters, Cold Emails профессорам и интервью**.  
> **Ключевой профиль:** Platform / Technical PM & System Designer (AI-Native Architecture, Knowledge Graphs, MCP).

---

## 1. 📊 Матрица оцифрованных результатов (Impact Cheat Sheet)

| Проект / Место | Роль | Метрика / Результат | Ключевой стек |
|---|---|---|---|
| **archmap**<br>*(Т-Банк)* | Founder & Product Owner | • Доставка C4-диаграмм: **с 1–3 дней до 15 минут** (−98% времени).<br>• Онбординг инженеров в архитектуру: **с недель до часов**.<br>• Масштабирование: **4 продукта / ~25 микросервисных репозиториев**.<br>• Оркестрация: n8n + бот в один клик. | Python, LikeC4, AST Tree-sitter, LLM (File Selector → Extractor), n8n, CI/CD |
| **Archon**<br>*(Диплом, R&D Lab)* | Lead System Architect & Product Owner | • Архитектурная декомпозиция: **17 логических модулей → 3 полиглотных сервиса** (Temporal Workflows, ADR-0007).<br>• Проектирование: **7 ADR закрыли 100% развилок и техблокеров до кодинга**.<br>• Knowledge Graph: **50 изолированных тенантов**, обход графа на глубину 4 за **<15 мс** (NFR <100 мс).<br>• **Правило Proof-of-Truth**: отсев недоказанных связей, **−90% расхода LLM-токенов**.<br>• Процессы: **37 задач в GitHub Projects**, Docs-as-Code (AGENTS.md). | Kotlin, Python, Temporal, PostgreSQL 16 + Apache AGE, Qdrant, LikeC4, MCP |
| **OmniSearch Engine**<br>*(Газпром Восток Нефть)* | Product Owner & System Architect | • Разделение Control Plane (Kotlin Ktor) и Compute Plane (Go / Python).<br>• Спроектирован конечный автомат (FSM) статусов видео.<br>• Внедрён в прод: автоматизация мониторинга соблюдения ТБ на объектах заказчика. | Kotlin Ktor, Go (GoCV/FFmpeg), Python (Whisper/CLIP), Qdrant, MinIO S3 |
| **Кобрендинг Т-ОРД**<br>*(Т-Банк)* | System Analyst (Junior+) | • Интеграция **3 внешних систем с разными REST-контрактами**.<br>• 100% корнер-кейсов закрыты в ТЗ до разработки: **0 блокеров на этапе деливери**, фича в проде. | REST API, OpenAPI, PostgreSQL, JSON API, Reverse Compatibility |
| **Операционные процессы**<br>*(Т-Банк)* | System Analyst | • Анализ **~145 инцидентов дежурств** → рефакторинг ранбуков → **время ответа (MTTR) −40%**.<br>• Шаблон сервисной документации для 2 команд: онбординг сокращён с 3 дней до 1 дня.<br>• BotControl: сравнительный анализ вариантов → быстрый MVP с конверсией отклика 50%. | Confluence, Jira, Runbooks, Service Blueprints |
| **CRDT-Engine**<br>*(Solo Open-Source)* | System Designer | • Real-time коллаборативный движок со Strong Eventual Consistency.<br>• Sequence CRDT (Fugue) + LWW-Register + векторные часы.<br>• Горизонтальное масштабирование через Redis Pub/Sub и шардирование по `document_id`. | Go, WebSockets, Redis Pub/Sub, Clean Architecture |

---

## 2. 🎙️ Готовые STAR-кейсы для эссе и интервью

### Кейс 1: Конфликт архитектурной сложности (17 микросервисов vs 3 сервиса)
* **Situation:** В проекте Archon команда разработчиков (4 инженера) разделилась во мнениях: делать ли 17 независимых микросервисов или монолит. Спор затягивал разработку на недели.
* **Task:** Как Team Lead и System Architect, я должен был разрешить тупик, минимизировать накладные расходы на инфраструктуру и сохранить модульность.
* **Action:** Вместо голосования я формализовал развилку через ADR-0007: рассчитал operational overhead для 17 сервисов (сетевой latency, distributed tracing, k8s overhead) и спроектировал компромиссную физическую топологию из 3 полиглотных сервисов (Portal/BFF, Core Engine, AI/Analysis Node) под управлением Temporal Polyglot Workflows.
* **Result:** Команда единогласно приняла ADR. Эксплуатационная сложность снизилась на 70%, а логическая изоляция модулей осталась 100%.

### Кейс 2: Борьба с галлюцинациями LLM и оптимизация токеномики (Proof-of-Truth)
* **Situation:** При автоматическом извлечении архитектурных связей из кода LLM периодически галлюцинировала зависимостями между модулями, расходуя тысячи токенов на повторные генерации.
* **Task:** Обеспечить 100% достоверность строящегося графа знаний и сократить затраты на API.
* **Action:** Я разработал двухфазный пайплайн: детерминированный статический анализ через AST Tree-sitter + строгий протокол **Proof-of-Truth**. Каждое ребро графа обязано содержать точные `evidence_files` (путь к файлу и номера строк). Любая связь без подтверждения отбрасывается валидатором.
* **Result:** Полное устранение ложных связей в Knowledge Graph и сокращение расхода токенов на 90%.

### Кейс 3: Продуктовая инициатива из неструктурированного запроса (archmap)
* **Situation:** Руководитель направления в Т-Банке упомянул проблему: архитектурные схемы в Confluence устаревают быстрее, чем их успевают обновлять, а разработчики тратят до 3 дней на ручную отрисовку C4.
* **Task:** Превратить абстрактную боль в работающий автоматизированный продукт.
* **Action:** Я не стал ждать ТЗ сверху. Самостоятельно инициировал продукт archmap: написал RFC, спроектировал двухфазный пайплайн (File Selector → Extractor) на Python, интегрировал генерацию LikeC4 в CI/CD и вывел запуск через Telegram-бота в один клик.
* **Result:** Время генерации архитектурной схемы упало с 1–3 дней до 15 минут. Руководство одобрило масштабирование решения на 4 продукта (~25 микросервисных репозиториев).

---

## 3. 🎯 Формулировки позиционирования под гранты

### Для Китая (CSC Type B — Tsinghua SIGS, PKU, SJTU):
> *"Research-oriented System Designer & Team Lead focused on AI-native Developer Platforms. Background in deterministic-LLM hybrid pipelines (Tree-sitter + Knowledge Graphs on Apache AGE) and Context Engineering via Model Context Protocol (MCP). Shipped 2 production platforms (archmap adopted across 25 microservice repos at T-Bank; OmniSearch multimodal video RAG at Gazprom)."*

### Для Тайваня (ICDF / MOE — NTHU IMBA / IMPISA):
> *"Technical Product Manager & R&D Team Lead (team v39) with a proven track record of shipping developer tools from 0 to 1. Proven impact in reducing architectural delivery cycle times by 98% (archmap), leading cross-functional engineering teams, and aligning business requirements with scalable distributed architectures."*
