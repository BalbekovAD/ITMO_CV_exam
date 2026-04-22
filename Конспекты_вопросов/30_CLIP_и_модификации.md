# 30. CLIP и модификации

## Краткий ответ

CLIP - это модель контрастивного обучения, которая выравнивает изображения и тексты в общем эмбеддинг-пространстве. Она обучается на парах изображение-текст: эмбеддинг изображения должен быть близок к эмбеддингу правильного текста и далек от других текстов в батче. CLIP используется для zero-shot классификации, поиска, оценки text-image alignment, управления генерацией, фильтрации данных и multimodal reasoning. Модификации включают OpenCLIP, ALIGN, LiT, SigLIP, CLIPSeg, StyleCLIP, RegionCLIP и адаптации для детекции, сегментации и VLM.

## Основные понятия

- Contrastive learning: обучение через сближение положительных пар и отталкивание отрицательных.
- Image encoder: CNN или Vision Transformer.
- Text encoder: Transformer для текста.
- Joint embedding space: общее пространство признаков.
- Zero-shot classification: классификация без обучения на целевом датасете через текстовые шаблоны.
- Prompt engineering: подбор текстовых формулировок классов.
- Prompt ensembling: усреднение нескольких текстовых шаблонов.
- Image-text retrieval: поиск изображений по тексту и текста по изображению.

## Алгоритмы, архитектуры и формулы

CLIP кодирует батч из `N` пар:

$$
\begin{aligned}
I_i &\to \operatorname{image\_encoder} \to v_i, \\
T_i &\to \operatorname{text\_encoder} \to u_i.
\end{aligned}
$$

Затем нормирует эмбеддинги и считает матрицу похожести:

$$
s_{ij} = \exp(\tau)\cos(v_i, u_j)
$$

Функция потерь - симметричная cross-entropy:

$$
L = \frac{1}{2}CE(\operatorname{image\_to\_text\_logits}, \operatorname{labels}) +
\frac{1}{2}CE(\operatorname{text\_to\_image\_logits}, \operatorname{labels})
$$

где правильная пара находится на диагонали матрицы похожести.

Zero-shot classification:

1. Для каждого класса создается текст, например `a photo of a {class}`.
2. Тексты кодируются text encoder.
3. Изображение кодируется image encoder.
4. Класс выбирается по максимальному cosine similarity.

$$
\operatorname{class} = \arg\max_k \cos(\operatorname{image\_embedding}, \operatorname{text\_embedding}_k)
$$

Модификации и родственные модели:

- OpenCLIP: открытая реализация и модели, обученные на больших открытых датасетах.
- ALIGN: похожая контрастивная image-text модель от Google.
- LiT: фиксирует сильный image encoder и дообучает text tower.
- SigLIP: заменяет softmax contrastive loss на sigmoid loss по парам, что лучше масштабируется.
- CLIPSeg: использует CLIP для сегментации по текстовому запросу.
- StyleCLIP: использует CLIP loss для управления латентным пространством StyleGAN.
- RegionCLIP/Detic: адаптация CLIP-подобных признаков к регионам и open-vocabulary detection.

## Сравнения, плюсы и минусы

CLIP по сравнению с обычным supervised classifier:

- Плюсы: zero-shot перенос, работа с естественным языком, универсальные эмбеддинги.
- Минусы: хуже специализированной модели на узкой задаче при наличии качественной разметки.

CLIP как метрика:

- Плюсы: быстро оценивает соответствие текста и изображения.
- Минусы: не гарантирует правильный счет объектов, пространственные отношения и мелкие детали.

CLIP для генерации:

- Плюсы: дает дифференцируемый сигнал от текста к изображению.
- Минусы: может приводить к adversarial-like решениям, когда картинка "нравится" CLIP, но выглядит плохо человеку.

## Связь с практикой и материалами курса

Тема связана с `Соотвествие изображений и текста.pdf`, `SSL и CL.pdf`, `05_text2img.pdf`, вопросами про StyleCLIP и условную генерацию. CLIP является мостом между компьютерным зрением и языком: через него строятся retrieval, zero-shot классификация, оценка соответствия промпту и управление генеративными моделями.

## Типичные ошибки

- Считать CLIP генеративной моделью. Сам CLIP ничего не генерирует, он кодирует и сравнивает.
- Использовать один промпт для zero-shot классификации без проверки шаблонов.
- Считать высокий CLIPScore доказательством полного соответствия промпту.
- Игнорировать bias обучающих данных.
- Путать CLIP и BLIP/LLaVA: CLIP не является диалоговой VLM.

## Источники

- Radford et al. Learning Transferable Visual Models From Natural Language Supervision, 2021.
- Jia et al. Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision, 2021.
- Zhai et al. Sigmoid Loss for Language Image Pre-Training, 2023.
- Материалы курса: `Соотвествие изображений и текста.pdf`, `SSL и CL.pdf`, `05_text2img.pdf`.
