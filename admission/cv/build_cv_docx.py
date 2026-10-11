#!/usr/bin/env python3
"""Build cv_sa.docx from the CV content — Google Docs-compatible styles."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ACCENT = RGBColor(0x17, 0x45, 0x6E)
INK = RGBColor(0x1C, 0x24, 0x30)
SOFT = RGBColor(0x4A, 0x55, 0x68)

doc = Document()

# --- page setup: A4, sane margins ---
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
sec.top_margin = sec.bottom_margin = Cm(1.4)
sec.left_margin = sec.right_margin = Cm(1.5)

# --- base style ---
normal = doc.styles['Normal']
normal.font.name = 'Arial'
normal.font.size = Pt(10)
normal.font.color.rgb = INK
normal.paragraph_format.space_after = Pt(2)
normal.paragraph_format.space_before = Pt(0)
# also set east-asian/cyrillic font hint so Word/Google keep Arial for Cyrillic
rpr = normal.element.get_or_add_rPr()
rfonts = rpr.get_or_add_rFonts()
rfonts.set(qn('w:ascii'), 'Arial')
rfonts.set(qn('w:hAnsi'), 'Arial')
rfonts.set(qn('w:cs'), 'Arial')


def para(text='', size=10, bold=False, color=INK, before=0, after=2, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    if align:
        p.alignment = align
    if text:
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.bold = bold
        r.font.color.rgb = color
    return p


def rich(p, parts, size=10):
    """parts: list of (text, bold) tuples appended to paragraph p."""
    for t, b in parts:
        r = p.add_run(t)
        r.font.size = Pt(size)
        r.bold = b
        r.font.color.rgb = INK if b else SOFT
    return p


def heading(text, before=10):
    p = para(text.upper(), size=10.5, bold=True, color=ACCENT, before=before, after=3)
    # bottom border under section heading
    ppr = p._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '2')
    bottom.set(qn('w:color'), 'D8DEE6')
    pbdr.append(bottom)
    ppr.append(pbdr)
    return p


def bullet(parts, size=10):
    if isinstance(parts, str):
        parts = [(parts, False)]
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.5)
    rich(p, parts, size=size)
    return p


# ================= HEADER =================
p = para('Денис Штэпа', size=22, bold=True, after=1)
p = para('Системный аналитик · Junior+ (грейд подтверждён внутренней оценкой Т-Банка)',
         size=11.5, bold=True, color=ACCENT, after=4)

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
rich(p, [('+7 (996) 350-77-95', True), ('  ·  ', False), ('ischademadda@gmail.com', False),
         ('  ·  ', False), ('Telegram: @ischademadda', False)], size=9.5)
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
rich(p, [('github.com/ischademadda  ·  github.com/teamv39', False)], size=9.5)
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
rich(p, [('Томск', True), (' — удалённо / гибрид / командировки; гражданство: Россия', False)], size=9.5)

# ================= DESIRED =================
heading('Желаемая должность и зарплата', before=8)
bullet([('Должность: ', True), ('системный аналитик (смежные: бизнес-аналитик, аналитик AI/LLM-продуктов)', False)])
bullet([('Зарплата: ', True), ('от 140 000 ₽ на руки, обсуждаема', False)])
bullet([('Тип занятости: ', True), ('полная занятость', False)])
bullet([('Формат: ', True), ('гибрид, удалённо', False)])

# ================= PROFILE =================
heading('Профиль')
para('Системный аналитик с подтверждённым грейдом Junior+ и суммарным опытом 2,5 года: два года веду R&D-лабораторию '
     'как основатель и системный аналитик, параллельно — корпоративные роли в Т-Банке и Газпром нефти. '
     'Специализация — System Design и полный цикл запуска продукта: архитектура (C4), API-контракты (REST/OpenAPI), '
     'модели данных, межсистемные интеграции, документация (ТЗ, RFC, ADR, Use Cases, Sequence Diagram). '
     'Отдельный фокус — AI-системы: LLM-пайплайны, RAG, Knowledge Graph, MCP-интеграции для AI-агентов. '
     'Ключевые системы внедрены у корпоративных заказчиков (Газпром Восток Нефть, Т-Банк), код проектов публичен на GitHub.',
     size=10, after=4)

# ================= SKILLS =================
heading('Ключевые навыки')
para('Системный анализ · Сбор и анализ требований · Разработка ТЗ · Use Cases · AS IS / TO BE · NFR · '
     'System Design (C4, LikeC4, PlantUML) · Sequence Diagram · Проектирование API (REST, OpenAPI, JSON API) · '
     'Межсистемные интеграции · Микросервисы · Событийная архитектура · Temporal · SQL / PostgreSQL · '
     'Графовые БД (Apache AGE) · Векторные БД (Qdrant) · Redis · RAG · LLM-пайплайны · AI-агенты · Knowledge Graph · '
     'Confluence · Jira · Git · Agile · Декомпозиция задач · Работа со стейкхолдерами · Постановка задач разработчикам',
     size=9.5, after=4)

# ================= EXPERIENCE =================
heading('Опыт работы — 2 года 7 месяцев (суммарно; роли частично параллельные)')

# --- Team v3.9 ---
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(4)
p.paragraph_format.space_after = Pt(0)
rich(p, [('R&D-лаборатория Team v3.9', True), ('   Сентябрь 2024 — настоящее время (2 года)', False)], size=11)
p = para('Роль: основатель, тимлид (4–7 инженеров), системный аналитик · Томск · github.com/teamv39',
         size=9.5, color=SOFT, after=2)
para('Студенческая R&D-команда, которую я собрал и возглавил: проектируем и внедряем системы для корпоративных '
     'заказчиков. Моя зона — системный анализ и System Design всех продуктов команды, от бизнес-требований '
     'до архитектуры и приёмки. Корпоративные роли (Т-Банк, Газпром нефть) вёл параллельно — совмещение '
     'согласовано с работодателями.', size=10, after=4)

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(1)
rich(p, [('Archon — платформа AI-native Source of Truth для корпоративной архитектуры', True),
         (' (август 2026 — н.в., выпускной проект)', False)], size=10.5)
para('Ведущий системный архитектор: платформа непрерывно синхронизирует архитектурную документацию с кодом '
     'и отдаёт проверенный контекст инженерам и AI-агентам разработки.', size=10, color=SOFT, after=2)
bullet('Спроектировал «фабрику знаний» из 17 логических модулей (портал, PR-бот, MCP-сервер, Knowledge Graph, '
       'детектор дрейфа), автор 7 ADR — все развилки закрыты до старта кодинга.')
bullet('Гибридный пайплайн Code-to-Architecture: детерминированный AST-анализ + двухфазный LLM-контур '
       'с Proof-of-Truth (каждая связь в графе подтверждена ссылками на файлы/строки) — исключены недоказанные '
       'связи, −90% LLM-токенов.')
bullet('Мультитенантный Knowledge Graph на PostgreSQL 16 + Apache AGE: верифицировал 50 изолированных '
       'графов-тенантов, обход на глубину 4 за <15 мс при NFR <100 мс.')
bullet('Физическая топология: 3 полиглотных сервиса (Kotlin/Python/React) под оркестрацией Temporal Workflows; '
       'privacy-by-default (код клиентов только в RAM).')
bullet('Управление: трекер на 37 задач, процесс Docs-as-Code (AGENTS.md), команда из 4 инженеров.')

p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(5)
p.paragraph_format.space_after = Pt(1)
rich(p, [('OmniSearch Engine — мультимодальная RAG-система для видеоархивов', True),
         (' (январь — июнь 2026) · github.com/teamv39/OmniSearch-Engine', False)], size=10.5)
para('Product Owner и системный аналитик: on-premise движок семантического видео-поиска, внедрён '
     'у корпоративного заказчика.', size=10, color=SOFT, after=2)
bullet('Спроектировал микросервисную архитектуру: Control Plane (Kotlin Ktor) + Compute Plane '
       '(Go: FFmpeg/GoCV, Python: Whisper/CLIP), OpenAPI 3.0-контракты, асинхронный пайплайн с конечным '
       'автоматом статусов обработки видео.')
bullet('Хранение: PostgreSQL, Qdrant, S3/MinIO; presigned URL для безопасного стриминга, CI/CD на GitHub Actions.')
bullet('Результат: внедрён в задачу автоматизации отслеживания соблюдения ТБ на объектах Газпром Восток Нефть; '
       'в раскатке на высоконагруженные бизнес-решения.')

p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(5)
p.paragraph_format.space_after = Pt(1)
rich(p, [('WikiLive — система совместной wiki-разработки для MTS Tech', True), (' (в разработке)', False)], size=10.5)
para('Системный аналитик, спроектировал всю систему:', size=10, color=SOFT, after=2)
bullet('Frontend (React + Tiptap) под Design Kit; Backend Gateway (Java Spring): бизнес-логика, авторизация, '
       'PostgreSQL, безопасное проксирование к MWS API.')
bullet('Sync Engine (Go): WebSockets, роутинг бинарных дельт, горизонтальное масштабирование через Redis Pub/Sub.')
bullet('AI Node (Python FastAPI): шлюз к MWS GPT, RAG-пайплайн, Qdrant.')

# --- T-Bank ---
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(8)
p.paragraph_format.space_after = Pt(0)
rich(p, [('Т-Банк', True), ('   Апрель 2026 — август 2026 (5 месяцев)', False)], size=11)
p = para('Должность: системный аналитик (по итогам оценки — грейд Junior+) · Москва, удалённо',
         size=9.5, color=SOFT, after=2)
para('Системный аналитик полного цикла с фокусом на System Design: сквозные решения на стыке нескольких команд, '
     'от сбора требований у бизнеса до постановки на разработку и сопровождения релиза в проде. Документация '
     'уровня RFC, ADR, ТЗ, Use Cases, Sequence Diagram; проработка рисков и корнер-кейсов на этапе проектирования; '
     'координация кросс-функциональных команд (Backend, Frontend, ML, QA, Design).', size=10, after=3)
bullet([('archmap', True), (' — автор и владелец продукта: из запроса лида направления «построить архитектурную '
       'карту» самостоятельно инициировал и вывел продукт — автогенерация архитектурной документации (LikeC4) '
       'прямо из кода. Спроектировал двухфазный LLM-парсер (File Selector → Extractor) + детерминированный '
       'генератор (Python, CI/CD), оркестрация в n8n, запуск через бота в один клик. Отрисовка C4-диаграммы: '
       'с 1–3 дней до 10–15 минут, онбординг в архитектуру: с недель до часов. Одобрен руководством, '
       'масштабируется на 4 продукта (~25 репозиториев).', False)])
bullet([('Кобрендинг в Т-ОРД', True), (' — спроектировал сквозную фичу от БД до фронта с интеграцией трёх внешних '
       'систем с разными контрактами и обратной совместимостью API. Все корнер-кейсы закрыты в ТЗ — разработка '
       'без единого блокера, фича в проде, обеспечивает соблюдение закона о маркировке рекламы.', False)])
bullet([('BotControl', True), (' — полный цикл аналитики и сравнительный анализ вариантов, обосновал быстрый MVP '
       'вместо дорогой интеграции. Решение в проде, конверсия отклика в бота — 50%.', False)])
bullet([('Процессы', True), (' — переработал ранбуки дежурств (анализ ~145 обращений, время ответа −40%), '
       'создал шаблон сервисной документации, переиспользуемый двумя командами (онбординг с 3 дней до 1).', False)])

# --- Gazprom ---
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(8)
p.paragraph_format.space_after = Pt(0)
rich(p, [('Газпром нефть, ПАО', True), ('   Июнь 2026 — июль 2026 (2 месяца, параллельно с R&D)', False)], size=11)
p = para('Должность: бизнес-аналитик · удалённо, проектная работа', size=9.5, color=SOFT, after=2)
bullet('Работал над задачей «Автоматизация отслеживания соблюдения ТБ на объектах»: стейкхолдеры '
       'Газпром Восток Нефть заинтересовались OmniSearch Engine и предложили расширить функционал под свои задачи.')
bullet('Собрал бизнес-требования с ключевых стейкхолдеров, выделил границы продукта, составил план доработки '
       'и roadmap для каждого участника команды.')
bullet('Задокументировал и согласовал требования с заказчиком, разработал функциональные требования с учётом '
       'пользовательских и бизнес-требований, проанализировал оптимальность существующих бизнес-процессов.')

# --- TPU curator ---
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(8)
p.paragraph_format.space_after = Pt(0)
rich(p, [('НИ ТПУ — платформа «Витрина проектов» ИШИТР+', True),
         ('   Сентябрь 2025 — июнь 2026 (10 месяцев)', False)], size=11)
p = para('Должность: куратор студенческих проектов · Томск', size=9.5, color=SOFT, after=2)
bullet('Кураторство студенческих проектных команд: помогал выстраивать процесс разработки и ведения проектов, '
       'подготавливал индивидуальные учебные планы, консультировал по учебным и внеучебным вопросам.')

# ================= PERSONAL PROJECTS =================
heading('Личные проекты')
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
rich(p, [('CRDT-Engine — распределённый движок совместного редактирования', True)], size=11)
p = para('github.com/ischademadda/CRDT-Engine · Go, Redis Pub/Sub, WebSockets', size=9.5, color=SOFT, after=2)
bullet('Спроектировал и реализовал real-time движок совместного редактирования с Strong Eventual Consistency '
       'без центральных блокировок: Fugue (Sequence CRDT), LWW-Register, векторные часы.')
bullet('Горизонтальное масштабирование (Hub/Broker-Worker): синк нод через Redis Pub/Sub, пул воркеров '
       'с шардированием по document_id.')
bullet('Clean-архитектура, полный комплект C4-диаграмм и ADR, e2e-тест на двух нодах с проверкой идентичности '
       'состояния при параллельном вводе.')

# ================= EDUCATION / LANGUAGES =================
heading('Образование и языки')
bullet([('2023 — 2027', True), (' — НИ Томский политехнический университет, ИШИТР, «Программная инженерия», '
       'бакалавриат (4 курс).', False)])
bullet([('Курсы: ', True), ('интенсив по системному анализу (Т-Банк, 2026); бизнес-аналитика (ТПУ, 2025).', False)])
bullet([('Русский', True), (' — родной; ', False), ('английский', True),
       (' — C1 (свободно работаю с документацией и технической перепиской).', False)])

# ================= ABOUT =================
heading('Обо мне')
para('Системный аналитик, который не ждёт детальной постановки: сам разбираюсь в контексте и довожу решение '
     'до прода. Дважды вёл продукт от идеи до внедрения у корпоративного заказчика: OmniSearch (Газпром '
     'Восток Нефть) и archmap (Т-Банк). Умею говорить и с бизнесом, и с разработкой: собираю требования '
     'у стейкхолдеров, декомпозирую задачи и веду кросс-функциональные команды (Backend, Frontend, ML, QA).',
     size=10, after=3)
para('Ищу команду со сложными задачами System Design: распределённые системы, межсистемные интеграции, '
     'AI-архитектура.', size=10)

doc.save('/Users/shteppinson/mylife/maga/admission/cv_sa.docx')
print('saved cv_sa.docx')
