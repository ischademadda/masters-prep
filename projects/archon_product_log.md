# Product Log — Archon (для фиксации PM-успехов)

> **Назначение:** Фиксировать продуктовые и архитектурные решения как PM-портфолио. 15 мин каждую пятницу.  
> **Формат:** 1 запись = 1 решение. Пишем по факту, не задним числом.  
> **Связь с ADR:** ADR — формальный документ решения. Product Log — краткий след для резюме, Study Plan, собеседований (STAR).  
> **Владелец:** Денис Штэпа, Team Lead / Product Owner Archon

---

## Как вести

Каждую пятницу ответь на 4 вопроса:

1.  **Decision:** Что решили? (1 предложение)
2.  **Why / Alternatives:** Почему так, а не иначе? Какие альтернативы отклонили?
3.  **Impact:** Что изменилось в метриках / времени / качестве? (цифра, если есть)
4.  **Artifact & Role:** Где зафиксировано (ADR-XXXX, PR #N, доска) и твоя роль (Facilitated / Authored / Decided)

Пример:

```
## 2026-09-08
Decision: Выбрали Temporal Polyglot Workflows вместо Celery для оркестрации пайплайна.
Why: Celery не держит полиглот (Kotlin + Python) и требует перепарсинга AST при ретрае LLM. Альтернатива — Airflow (тяжелый для MVP).
Impact: Ретрай только шага LLM с экспоненциальным бэкоффом, без перепарсинга AST. Снижение времени восстановления с ~5 мин до ~30 сек.
Artifact: ADR-0007
Role: Authored ADR, facilitated team decision (4 инженера)
```

---

## Лог

### 2026-09-08
Decision: [заполни по итогам недели]
Why:
Alternatives:
Impact:
Artifact:
Role:

### 2026-09-15
Decision:
Why:
Alternatives:
Impact:
Artifact:
Role:

### 2026-09-22
Decision:
Why:
Alternatives:
Impact:
Artifact:
Role:

### 2026-09-29
Decision:
Why:
Alternatives:
Impact:
Artifact:
Role:

_(копируй блок на каждую неделю до защиты диплома)_

---

## Готовые записи из уже принятых решений (перенеси в резюме и Study Plan)

Заполнил за тебя по уже существующим ADR — используй как пример и как материал для эссе.

### ADR-0002 — Списание archmap прототипа
Decision: Списали монолитный прототип archmap (Python/Neo4j), перенесли ценность в веху Code-to-Architecture в Archon.
Why: Прототип не масштабируется, завязан на n8n/TiMe/GitLab, нет персистентного графа и детерминированных фактов.
Alternatives: Пытаться дорабатывать прототип (отклонено — техдолг > переписать).
Impact: Разблокировали разработку ядра, закрыли блокер OQ-1. Сэкономили ~2 месяца на поддержке прототипа.
Artifact: ADR-0002
Role: Authored ADR, drove decision

### ADR-0003 — PostgreSQL 16 + Apache AGE, Graph-per-Tenant
Decision: Выбрали PostgreSQL 16 + Apache AGE для Knowledge Graph, изоляция Graph-per-Tenant (каждый тенант = отдельная схема pg_namespace).
Why: Нужна сильная изоляция + транзакционность + один стек для реляционных данных и графа. Neo4j — отдельный кластер, дороже.
Alternatives: Neo4j (отклонено — второй стек, сложнее мультитенантность), shared graph с tenant_id (отклонено — риск утечки).
Impact: 50 изолированных графов без деградации, обход на глубину 4 — <15ms (NFR <100ms). Закрыты OQ-2 и OQ-5.
Artifact: ADR-0003
Role: Led R&D and stress-testing, authored ADR

### ADR-0004 — Модульная декомпозиция (17 модулей)
Decision: Декомпозиция на 17 ортогональных модулей в 5 блоках, принцип "модуль != сервис".
Why: Ортогональность и независимые жизненные циклы, разделить контуры извлечения (extract/interpret/reconcile).
Alternatives: Сразу резать на микросервисы (отклонено — преждевременно, усложняет MVP).
Impact: Четкие границы владения, параллельная разработка 4 инженеров без конфликтов.
Artifact: ADR-0004
Role: Designed decomposition, authored ADR

### ADR-0007 — Упаковка в 3 сборочные единицы + Temporal + RAM-диск
Decision: Упаковали 17 модулей в 3 сервиса (archon-core Kotlin, archon-ai Python, archon-portal React) + Temporal Polyglot Workflows + клон в RAM-диск (/dev/shm, rm -rf после AST).
Why: Баланс между операционкой и независимостью, полиглот ретраи, Privacy-by-default (код не сохраняется на диске).
Alternatives: 17 микросервисов (отклонено — оверхед), 1 монолит (отклонено — не масштабируется по командам).
Impact: Деплой проще на 70%, ретрай LLM без перепарсинга, соответствие enterprise privacy. Закрыт OQ-8.
Artifact: ADR-0007
Role: Designed topology, authored ADR

### Product — archmap (Solo)
Decision: Инициировал продукт archmap из запроса лида "построить карту", спроектировал пайплайн LLM (File Selector -> Extractor, vocabulary.json) + детерминированный генератор LikeC4.
Why: Ручная C4 — 1-3 дня, протухает за неделю, зоопарк инструментов.
Impact: C4 за 10-15 мин, онбординг недели -> часы, масштабирован на 4 продукта / ~25 репо. Одобрен руководством.
Artifact: RFC, archmap.md, TiMe-бот + n8n workflow
Role: Founder & Product Owner (solo)

### Product — OmniSearch Engine (Team)
Decision: Разделил систему на Control Plane (Kotlin Ktor) и Compute Plane (Go Video Engine + Python ML Engine), определил OpenAPI контракты и асинхронный пайплайн.
Why: Разделить I/O и compute, изолировать GPU-зависимый ML.
Impact: MVP с семантическим поиском (Whisper + CLIP + Qdrant), adopted by Gazprom Vostok Neft for HSE automation.
Artifact: omnisearch.md, docker-compose, OpenAPI
Role: System Designer, Product Owner

---

## Продуктовые метрики Archon (оцифровка для README и эссе)

Добавь в `archon_shtepa.md` / `archon_product-overview.md` в раздел MVP:

| Метрика | До / Без Archon | С Archon | Как измерено |
|---|---|---|---|
| Time-to-C4 (C1-C3) | 1-3 дня ручной работы | 10-15 мин (archmap), цель <30 мин для Archon | Замер на 4 продуктах |
| Spec Drift detection | Ручной аудит, недели | <15ms на глубину 4 (Impact Analysis) | Стресс-тест AGE, 50 тенантов |
| Onboarding в архитектуру | Недели + отвлечение сеньоров | Часы, самостоятельно по порталу/MCP | Опрос лидов |
| Token economy (LLM) | 100% файлов в контекст | -90% токенов (File Selector читает только дерево путей) | Замер пайплайна |
| Trust (галлюцинации) | LLM выдумывает связи | 0 связей без evidence_files (Proof-of-Truth) | Extraction Contract v1.0 |
| Adoption | 0 | Цель MVP: 4 продукта / 25 репо (наследие archmap) | GitHub |

---

## Как использовать на собеседовании (STAR)

На вопрос "Расскажи про лидерство / конфликт / сложное решение" бери одну запись из лога и отвечай:

- **S**ituation: Контекст (что было до решения)
- **T**ask: Твоя задача как лида
- **A**ction: Что ты сделал (facilitated, authored ADR, выбрал альтернативу)
- **R**esult: Цифра (время, метрика, закрытый блокер)

Пример: "В Archon у нас был спор — 17 микросервисов или 3 сервиса. Я предложил упаковать в 3 сервиса под Temporal (ADR-0007), потому что 17 — оверхед для MVP, а монолит — не масштабируется по командам. Решение сократило сложность деплоя на 70% и дало полиглот ретраи."

