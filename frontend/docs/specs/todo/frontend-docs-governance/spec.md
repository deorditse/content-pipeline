# Frontend: OpenSpec документации и ADR

## Цель
Завести документационный слой OpenSpec/ADR для frontend-проекта.

## Контекст
Frontend отвечает за будущий UI управления конвейером: бриф, сцены, prompt editor, очередь, preview и экспорт.

## Что делаем
- Создать `docs/adr/` для архитектурных правил frontend.
- Создать пустые `docs/adr/rules.md` и `docs/adr/agent.md`.
- Создать spec, фиксирующий документационную структуру frontend.

## Что НЕ делаем
- Не выбирать frontend-стек без отдельного ADR.
- Не добавлять UI-код сверх заглушки.
- Не описывать backend-контракты в frontend-правилах.

## Критерии приёмки
- В `frontend/docs/` есть README, specs и adr.
- `frontend/docs/adr/rules.md` и `frontend/docs/adr/agent.md` существуют и пока пустые.
- Spec frontend лежит в `frontend/docs/specs/todo/`.

## Открытые вопросы
- Какие архитектурные правила первыми занести в `rules.md`?
- Какие инструкции для агентов должны попасть в `agent.md` после выбора рабочих процессов?
