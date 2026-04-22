# 31. Vision Language Models: LLaVA и другие

## Краткий ответ

Vision Language Models (VLM) - это модели, которые совместно обрабатывают изображения и текст, отвечают на вопросы по картинкам, описывают сцены, рассуждают о визуальном содержимом и могут выполнять инструкции. В отличие от CLIP, который в основном сравнивает изображение и текст, VLM обычно подключает визуальный энкодер к большой языковой модели. LLaVA - типичный пример: CLIP ViT кодирует изображение, projection layer переводит визуальные признаки в пространство LLM, а языковая модель генерирует ответ.

## Основные понятия

- Multimodal model: модель, работающая с несколькими модальностями.
- Visual encoder: извлекает признаки изображения.
- LLM: языковая модель, генерирующая текстовый ответ.
- Projector/adapter: слой, согласующий размерности visual tokens и language embeddings.
- Visual instruction tuning: дообучение на диалогах и инструкциях с изображениями.
- VQA: visual question answering.
- Image captioning: генерация описания изображения.
- OCR-aware VLM: модель, способная читать текст на изображении.
- Grounding: связывание ответа с конкретными областями изображения.

## Алгоритмы, архитектуры и формулы

Общая схема VLM:

```text
image -> visual encoder -> visual tokens
visual tokens -> projector -> LLM embedding space
text prompt + visual tokens -> LLM -> answer
```

LLaVA строится в две основные стадии:

1. Feature alignment pretraining.
   - Visual encoder и LLM соединяются projector-слоем.
   - Модель учится превращать визуальные признаки в формат, понятный LLM.

2. Visual instruction tuning.
   - Модель дообучается на инструкциях вида "что изображено?", "сравни объекты", "объясни ситуацию".
   - Ответ генерируется авторегрессионно как обычный текст.

Типичный loss:

$$
L = -\sum_t \log p(y_t \mid y_{<t}, \operatorname{image}, \operatorname{prompt})
$$

То есть обучение идет как language modeling с дополнительным визуальным контекстом.

Другие семейства моделей:

- Flamingo: использует cross-attention между LLM и визуальными признаками, умеет few-shot multimodal learning.
- BLIP/BLIP-2: bootstrapping language-image pretraining; BLIP-2 использует Q-Former между visual encoder и LLM.
- MiniGPT-4: соединяет visual encoder с LLM через проекцию, похожая идея на LLaVA.
- Kosmos, PaLI, Gemini-подобные и GPT-4V-подобные системы: масштабные мультимодальные модели.
- GroundingDINO + SAM pipelines: не всегда VLM в узком смысле, но часто используются для grounded visual tasks.

Важные задачи:

- captioning;
- VQA;
- document understanding;
- chart understanding;
- visual reasoning;
- referring expression comprehension;
- open-vocabulary detection/segmentation через связку с grounding models;
- multimodal agents.

## Сравнения, плюсы и минусы

CLIP:

- Плюсы: сильные эмбеддинги, retrieval, zero-shot classification.
- Минусы: не генерирует развернутые ответы.

LLaVA-подобные VLM:

- Плюсы: диалог, инструкции, объяснения, гибкость LLM.
- Минусы: возможны hallucinations, ошибки счета, слабая локализация без специальных модулей; модель может отвечать правдоподобно даже при недостаточном визуальном свидетельстве.

BLIP-2:

- Плюсы: эффективное соединение замороженных vision и language моделей через Q-Former.
- Минусы: архитектура сложнее, качество зависит от согласования модальностей.

Grounded VLM:

- Плюсы: может указывать области, bounding boxes, маски.
- Минусы: требует специальной разметки или внешних детекторов/сегментаторов.

## Связь с практикой и материалами курса

Тема связана с `img_report_VLM_Козьма.pdf`, `Соотвествие изображений и текста.pdf`, `SSL и CL.pdf` и вопросом про CLIP. Логическая цепочка курса: сначала учимся извлекать визуальные признаки, затем связываем изображения и текст через CLIP, затем строим модели, которые используют зрение как контекст для языкового рассуждения.

## Типичные ошибки

- Называть CLIP полноценной VLM в смысле диалоговой модели. CLIP - vision-language encoder, но не instruction-following assistant.
- Доверять VLM без проверки: модели могут уверенно выдумывать детали.
- Принимать текстовый ответ за доказательство grounding: без boxes/masks/attention-проверок модель могла не привязать утверждение к нужной области.
- Игнорировать разрешение изображения: мелкий текст и мелкие объекты могут быть потеряны.
- Считать, что VLM всегда умеет точную локализацию. Для grounding часто нужны отдельные механизмы.
- Не различать captioning, VQA, OCR и reasoning: это разные способности.

## Источники

- Alayrac et al. Flamingo: a Visual Language Model for Few-Shot Learning, 2022.
- Li et al. BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models, 2023.
- Liu et al. Visual Instruction Tuning, 2023.
- Материалы курса: `img_report_VLM_Козьма.pdf`, `Соотвествие изображений и текста.pdf`, `SSL и CL.pdf`.
