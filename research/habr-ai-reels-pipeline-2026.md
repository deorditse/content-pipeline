# Habr research: AI Reels content pipeline, 2026

Дата: 2026-10-11

## Использованные Habr-источники

- https://habr.com/ru/companies/study_ai/articles/1074682/ — топ-10 генераторов видео 2026.
- https://habr.com/ru/companies/study_ai/articles/1023800/ — сравнение Veo 3.1, Kling 3.0, Runway, HappyHorse.
- https://habr.com/ru/companies/era2/articles/1042364/ — топ-7 генераторов видео 2026.
- https://habr.com/ru/companies/era2/articles/1034794/ — ElevenLabs и аналоги для клонирования/озвучки.
- https://habr.com/ru/companies/study_ai/articles/1037322/ — русская TTS-озвучка и агрегаторы.
- https://habr.com/ru/companies/bothub/articles/1081544/ — OpenAI TTS, ElevenLabs Voice и модели озвучки в агрегаторе.
- https://habr.com/ru/companies/tsnis/articles/1056844/ — гайд по генерации изображений и рейтинг моделей.
- https://habr.com/ru/companies/tsnis/articles/1060980/ — генерация текста/картинок/видео/музыки в одном месте.
- https://habr.com/ru/companies/studyai/articles/1085264/ — тесты генераторов изображений.

## Вывод для MVP

Для коротких Reels лучше строить не один «магический» генератор, а модульный конвейер:

1. сценарий и сцены;
2. ключевые изображения/референсы для каждой сцены;
3. image-to-video / text-to-video по сценам;
4. отдельная TTS-озвучка;
5. сборка, субтитры, музыка, нормализация звука.

Так проще менять провайдеров, контролировать стоимость и пересобирать только проблемные сцены.

## TTS / озвучка

Предварительный топ по статьям Хабра:

- ElevenLabs — основной кандидат для качества, естественных интонаций, русского TTS, дубляжа и voice cloning.
- Voice.era2.ai / локальные или региональные обёртки ElevenLabs — вариант, если важны доступность из РФ и простая оплата.
- Для MVP нужен абстрактный `VoiceProvider`, чтобы можно было менять ElevenLabs на альтернативы без переписывания пайплайна.

Практические правила:

- Готовить текст специально под произношение: короткие фразы, без длинных скобок, явно прописывать числа и сокращения.
- Хранить voice preset, stability/style/speaker settings и версию модели рядом с артефактом.
- Генерировать субтитры отдельно и держать таймкоды.

## Image generation / картинки под сцены

Предварительный топ по статьям Хабра:

- GPT Image 2 / ChatGPT Images — точное следование промпту, диалоговое редактирование, хорош для итераций и сложных инструкций.
- Nano Banana Pro / Google image models — сильны для кириллицы, сохранения идентичности персонажей и 4K/сложных задач.
- FLUX 2 / FLUX Pro/Max — сильный фотореализм, открытая экосистема, удобен для локального/серийного production при наличии инфраструктуры.
- Midjourney — художественная атмосфера, стиль, красивые key visuals.
- Recraft / Ideogram — дизайн, текст, постеры, типографика.
- Adobe Firefly — кандидат для корпоративных сценариев с высокими требованиями к лицензированию.

Практические правила:

- Для Reels лучше генерировать consistent keyframes: персонаж, стиль, палитра, камера, свет, seed/reference.
- Промпт сцены хранить структурно: subject → action → environment → style → lighting → camera/tech params → negative constraints.
- Разделять `concept image`, `keyframe`, `thumbnail`, `overlay/text frame`.

## Video generation

Предварительный топ по статьям Хабра:

- Google Veo 3.1 — кинематографичный флагман; часть обзоров отмечает генерацию видео со звуком/синхронной речью.
- Kling 3.0 — сильный баланс цены/качества, image-to-video, motion control, детализация текстур; хороший кандидат для Reels-сцен.
- Runway Gen-4 / Aleph — не только генерация, но и видеоредактирование: замена объектов, свет, стиль, reference workflows.
- Luma Ray / Ray Flash — быстрое прототипирование, хорошая мимика/движение в отдельных тестах.
- Seedance / PixVerse / Hailuo / Wan — кандидаты для динамики, соцсетевых эффектов, серийного контента и людей/эмоций.

Практические правила:

- Для MVP делать scene-based generation: 3–6 секунд на сцену, потом сборка.
- Сначала генерировать keyframe, затем image-to-video — это обычно стабильнее для персонажей и стилистики.
- Всегда сохранять provider, model, prompt, seed/reference, duration, aspect ratio, cost и статус качества.
- Для вертикальных роликов держать 9:16 как default, но сохранять safe zones под UI Reels/TikTok/Shorts.

## Рекомендованный MVP stack провайдеров

- TTS: ElevenLabs-compatible adapter первым, fallback через альтернативный TTS adapter.
- Images: GPT Image / Nano Banana / FLUX adapter интерфейсы; начать с того, к чему есть доступ/API.
- Video: Kling/Runway/Luma adapters; начать с image-to-video.
- Assembly: FFmpeg как обязательная низкоуровневая сборка; Python wrapper позже.

## API-следствие

Backend должен оперировать не «одним роликом», а сущностями:

- `Brief`
- `Script`
- `Scene`
- `Asset` (`image`, `video`, `audio`, `subtitle`)
- `GenerationJob`
- `ProviderRun`
- `Render`

Это позволит подменять модели и перегенерировать отдельные сцены.
