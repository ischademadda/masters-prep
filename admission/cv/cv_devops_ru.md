# Денис Штэпа — Platform Engineer / DevOps Lead

**Контакты:**
- **Город:** Томск, Россия (готов к удаленной работе / гибриду)
- **Телефон:** +7 (996) 350-77-95
- **Email:** [ischademadda@gmail.com](mailto:ischademadda@gmail.com)
- **Telegram:** [@ischademadda](https://t.me/ischademadda)
- **GitHub:** [ischademadda](https://github.com/ischademadda) / [teamv39](https://github.com/teamv39)
- **Образование:** Томский политехнический университет (ТПУ), Инженерная школа информационных технологий и робототехники (ИШИТР), бакалавриат «Программная инженерия» (2023–2027), GPA: 3.93/5.0 (~3.5/4.0, топ-10% курса)
- **Языки:** Русский (родной), Английский (C1, свободный технический / подготовка к IELTS 7.5+)

---

## О себе / Профессиональный профиль

**Platform Engineer / DevOps Lead** с 2+ годами опыта проектирования надежной инфраструктуры, построения сквозных CI/CD конвейеров и контейнеризации гетерогенных сервисов в R&D лаборатории и enterprise-контурах.

- **Глубокая экспертиза в GitLab CI/CD:** разработка переиспользуемых CI-шаблонов (`include:remote`), multi-project пайплайны, артефакты, развертывание на GitLab Pages, триггеры и авто-мерж MR через API и вебхуки.
- **GitHub Actions & автоматизация сборок:** матричные сборки, `docker buildx bake` с многоуровневым кешированием в GitHub Actions Cache, релизные пайплайны.
- **Контейнеризация и оркестрация:** Docker, multi-stage Dockerfile, Docker Compose (разбиение dev/prod), Kubernetes (стратегии деплоя, Ingress Controller, эфемерные sandboxes в RAM через `emptyDir` / `/dev/shm`), Temporal.io Cluster.
- **Инфраструктура, сети и Reverse Proxy:** Nginx (API Gateway, балансировка, rate-limiting, SSL/TLS, стриминг видео), Cloudflare, Linux (Bash, тюнинг производительности).
- **Инженерные стандарты:** построение Git Flow, контроль Conventional Commits, Docs-as-Code (ADR, C4 модель в LikeC4).

Реальный опыт запуска решений в **Т-Банке** (платформа archmap — CI/CD пайплайны на 4 продукта / 25 репозиториев), проектирования on-premise инфраструктуры (OmniSearch, обмен опытом со специалистами **Газпромнефть-Восток**) и хакатона **МТС True Tech Hack**.

---

## Опыт работы

### team v39 — Applied R&D Lab
**Роль:** DevOps Lead & Platform Engineer (руководство инфраструктурным направлением команды из 4–7 инженеров)  
**Период:** Сентябрь 2024 — настоящее время | Томск, Россия

#### 1. Archon — AI-Native Enterprise Architecture Platform (диплом, в разработке)
*Стек: Kubernetes, Temporal, Docker, GitHub Actions, Nginx Ingress, PostgreSQL (Apache AGE), Qdrant, Linux*  
*Роль: Tech Lead & Platform Architect*
- **Инженерные процессы команды (Tech Lead):** Руковожу инженерной командой (4–7 разработчиков); выстраиваю процессы разработки: строгий Git Flow, Conventional Commits, версионирование решений Docs-as-Code (ADR) и GitHub Actions CI/CD (линтеры, автотесты, сборка multi-stage Docker-образов).
- **Проектирование стратегий деплоя (K8s & Ingress):** Спроектировал стратегию физического развертывания и топологию сервисов в Kubernetes (ADR-0007: декомпозиция 17 модулей в 3 полиглотных сервиса и кластер Temporal); заложил модель маршрутизации через Nginx Ingress с TLS-терминацией.
- **Архитектура песочниц (RAM-диски):** Спроектировал стратегию изоляции сред (Sandboxes) для безопасного AST/LLM анализа кода на базе RAM-дисков (`emptyDir: { medium: "Memory" }` / `/dev/shm`), чтобы исключить дисковые I/O боттлнеки и гарантировать атомарную очистку при сбоях.
- **Модель оркестрации воркфлоу:** Спроектировал модель отказоустойчивой оркестрации долгих фоновых графовых пайплайнов на базе Temporal.io (retry policies, таймауты, саги компенсации сбоев).

#### 2. OmniSearch Engine — On-Premise Multimodal Video RAG Platform
*Стек: Docker, Docker Compose, Docker Buildx, GitHub Actions, Nginx Gateway, MinIO S3, Qdrant, Bash*
- **Мультисервисная контейнеризация:** Спроектировал легковесные production-ready multi-stage Dockerfile для 4 разнородных микросервисов (Kotlin/JVM, Go worker pool, Python ML/PyTorch, React SPA), изолировав зависимости и сократив размеры образов.
- **Окружения и оптимизация сборок:** Разделил конфигурации сред (`docker-compose.yml`, `docker-compose.dev.yml`, `docker-compose.prod.yml`). Внедрил сборку через `docker buildx bake` с кешированием слоев в GitHub Actions Cache, ускорив время прогона CI в 2.5 раза.
- **API Gateway & Networking:** Сконфигурировал Nginx Reverse Proxy Gateway (`gateway.conf`) с rate-limiting, CORS-заголовками, поддержкой чанкового видео-стриминга и едиными health-check эндпоинтами для оркестрации сервисов.
- **On-Premise архитектура & обмен опытом:** Спроектировал автономную on-premise топологию с распределенным хранилищем MinIO S3 и векторной БД Qdrant под требования промышленного видеомониторинга; защита решений и обмен инженерным опытом с экспертами **Газпромнефть-Восток**.

#### 3. Корпоративная Wiki-система — МТС True Tech Hack 2026
*Стек: Docker, Docker Compose, GitHub Actions, Nginx, Java Spring Boot, Go, Python, PostgreSQL, MWS*  
*Роль: DevOps / Infrastructure Engineer*
- **Мультисервисный деплой за 5 дней:** В сжатые сроки хакатона спроектировал и развернул контейнеризированную среду Docker Compose для связки из 3 микросервисов (Java Spring Boot, Go модуль, Python ML/RAG) и PostgreSQL.
- **CI/CD & Инфраструктура:** Настроил GitHub Actions (автоматическая сборка Docker-образов, линтеры, автотесты при PR), внутреннюю маршрутизацию через Nginx и интеграцию с облачными сервисами MWS (MTS Web Services).
- **Git Flow в команде:** Внедрил командный Git Flow для ускоренной синхронизации бэкендеров и ML-инженеров, обеспечив непрерывную интеграцию и успешную защиту прототипа на хакатоне.

---

### Т-Банк (T-Bank)
**Роль:** DevOps / CI/CD Engineer & System Analyst (проект archmap)  
**Период:** Апрель 2026 — Август 2026 | Москва, Россия (Удаленно)

- **Архитектура GitLab CI/CD для archmap:** Спроектировал и реализовал с нуля распределенный CI/CD конвейер генерации архитектурных карт LikeC4. Разработал централизованный переиспользуемый CI-шаблон `build-likec4.gitlab-ci.yml`, подключаемый через `include:remote` во все зависимые микросервисные репозитории компании.
- **Multi-Project Pipelines & GitLab Pages:** Настроил межпроектную оркестрацию: автоматический экспорт артефактов (`bundle.json`), сборку статических веб-бандлов и публикацию на **GitLab Pages** с гибким разграничением прав доступа через GitLab PAT.
- **Автоматизация MR и интеграция с n8n:** Выстроил сквозную триггерную модель CI-джобов (`generate-c4`, `build-likec4`, `pages`) и автоматический merge Merge Request через GitLab API и вебхуки в n8n. Сократил time-to-market доставки архитектурной документации с 1–3 дней до 15 минут, масштабировав решение на 4 продукта (~25 микросервисов).
- **Операционная надежность & Incident Runbooks:** Систематизировал и автоматизировал онкол-ранбуки по 145 боевым инцидентам, сократив время локализации и восстановления систем (MTTR) на 40%.

---

## Навыки и стек технологий

| Категория | Технологии и инструменты |
|---|---|
| **CI/CD & Автоматизация** | GitLab CI/CD (Shared Templates, Multi-project pipelines, Artifacts, Pages, GitLab API, Webhooks), GitHub Actions (Workflows, Matrix builds, Cache, Secrets), n8n, semantic-release |
| **Контейнеризация & Оркестрация** | Docker, Docker Compose, Docker Buildx (bake, multi-stage), Kubernetes (стратегии деплоя, Ingress, Pod Topology, Ephemeral Volumes, `emptyDir` RAM-диски), Temporal.io Cluster |
| **Инфраструктура & Сети** | Nginx (Reverse Proxy, API Gateway, Load Balancing, Rate-limiting, SSL/TLS), Cloudflare, Linux / Bash, System Design, Git Flow, Conventional Commits, Docs-as-Code (ADR, LikeC4) |
| **Хранилища, Базы данных & Cloud** | PostgreSQL, Redis, MinIO S3, Qdrant Vector DB, Apache AGE, MWS (MTS Web Services) |
| **Языки и тулинг** | Bash, Python, Go, Kotlin, Java, YAML, JSON, Git, curl, jq, Make, Tree-sitter |
| **Иностранные языки** | Английский (C1 — свободное чтение документации, техническая переписка, подготовка к IELTS 7.5), Китайский (HSK 1-2, в процессе) |
