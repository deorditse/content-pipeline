# Content Pipeline map

Быстрый навигатор по проектам репозитория `content-pipeline`.

## Репозиторий

- Назначение: продуктовый конвейер для коротких вертикальных роликов: идея/бриф → сценарий → сцены → изображения/ключевые кадры → видео → озвучка/субтитры → сборка итогового MP4.
- Entry: `README.md`.
- Общая документация: `docs/README.md`.
- Общие архитектурные правила: `docs/adr/rules.md`.
- Общие инструкции для агентов: `docs/adr/agent.md`.

## Проекты

| Проект | Путь | За что отвечает | Entry | Документация |
|---|---|---|---|---|
| Content Pipeline root | `.` | Общий продуктовый scope, карта репозитория, cross-project specs/ADR, research/reports. | `README.md` | `docs/README.md` |
| Backend | `backend/` | API, OpenAPI-контракты, orchestration/jobs, интеграции с TTS/image/video providers, render-сборка. | `backend/README.md` | `backend/docs/README.md` |
| Frontend | `frontend/` | UI управления конвейером: бриф, сцены, prompt editor, очередь генераций, preview, экспорт. | `frontend/README.md` | `frontend/docs/README.md` |

## Поддерживающие директории

| Директория | Назначение |
|---|---|
| `research/` | Исследования моделей, сервисов и решений для контент-пайплайна. |
| `reports/` | Сгенерированные отчёты/экспорты по исследованиям и прототипам. |

## Документационный стандарт

В каждом проекте:

- `docs/specs/todo/<task>/spec.md` — активная OpenSpec-спецификация.
- `docs/specs/done/<task>/spec.md` — принятая/завершённая спецификация.
- `docs/adr/` — архитектурные решения и правила.
- `docs/adr/rules.md` — архитектурные правила проекта; сейчас файл создан пустым.
- `docs/adr/agent.md` — инструкции для агентов; сейчас файл создан пустым.
