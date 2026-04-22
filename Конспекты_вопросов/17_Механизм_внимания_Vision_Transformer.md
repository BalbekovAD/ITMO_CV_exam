# 17. Механизм внимания, Vision Transformer

## Краткий ответ

Механизм внимания позволяет модели взвешенно учитывать разные элементы входа при построении представления. В self-attention каждый токен сравнивается со всеми токенами и собирает информацию из них с весами, зависящими от сходства query и key. Vision Transformer, ViT, применяет Transformer к изображению: разбивает изображение на патчи, превращает патчи в токены, добавляет positional embeddings и обрабатывает последовательность Transformer encoder-блоками.

## Основные понятия

- **Token**: элемент последовательности. В ViT токен соответствует patch embedding.
- **Query, Key, Value**: три линейные проекции входных токенов.
- **Self-attention**: внимание внутри одной последовательности.
- **Multi-head attention**: несколько независимых attention heads, изучающих разные отношения.
- **Positional embedding**: добавляет информацию о положении, потому что attention сам по себе перестановочно-инвариантен.
- **CLS token**: специальный токен для классификации в ViT.
- **Patch embedding**: линейное отображение плоского patch в вектор признаков.

## Формулы внимания

Scaled dot-product attention:

$$
\operatorname{Attention}(Q, K, V) =
\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Где $Q = XW_Q$, $K = XW_K$, $V = XW_V$. Деление на $\sqrt{d_k}$ стабилизирует softmax при больших размерностях.

Multi-head attention:

$$
\begin{aligned}
\operatorname{head}_i &= \operatorname{Attention}(QW_i^Q, KW_i^K, VW_i^V), \\
MHA &= \operatorname{Concat}(\operatorname{head}_1, \ldots, \operatorname{head}_h)W_O.
\end{aligned}
$$

Transformer encoder block обычно содержит:

$$
\begin{aligned}
X &= X + MSA(\operatorname{LayerNorm}(X)), \\
X &= X + MLP(\operatorname{LayerNorm}(X)).
\end{aligned}
$$

То есть residual connections, layer normalization, multi-head self-attention и feed-forward MLP.

## Vision Transformer

ViT pipeline:

1. Изображение `H x W x C` делится на патчи `P x P`.
2. Каждый patch разворачивается и проецируется в embedding размерности `D`.
3. Добавляется `CLS` token и positional embeddings.
4. Последовательность проходит через Transformer encoder.
5. Представление `CLS` используется для классификации.

Число токенов:

$$
N = \frac{HW}{P^2}
$$

Сложность self-attention по числу токенов квадратичная:

$$
O(N^2D)
$$

Поэтому маленький patch повышает точность локализации, но резко увеличивает стоимость.

## Архитектурные варианты

- **ViT**: чистый Transformer на патчах, хорошо работает при большом pretraining.
- **DeiT**: data-efficient training и distillation token.
- **Swin Transformer**: локальное window attention и shifted windows; иерархическая структура ближе к CNN.
- **MAE**: masked autoencoder pretraining, восстановление скрытых патчей.
- **DETR-подходы**: attention для объектного детектирования через object queries.

## Сравнения, плюсы и минусы

CNN имеют сильные inductive biases: локальность, weight sharing, translation equivariance. Поэтому они эффективны на малых датасетах. ViT слабее зашит под изображения, но лучше масштабируется на больших данных и умеет моделировать дальние зависимости с ранних слоев.

Плюсы ViT: глобальный контекст, масштабируемость, универсальность для мультимодальных моделей. Минусы: требовательность к данным и вычислениям, квадратичная сложность attention, необходимость positional encoding.

## Связь с практикой и материалами курса

Тема соответствует ноутбуку `04_01_Attn,_ViT.ipynb` и генеративным блокам, где attention используется в autoregressive, diffusion и text-to-image моделях. В CV attention встречается не только в классификации, но и в DETR, CLIP, Stable Diffusion U-Net, VLM и segmentation models.

## Типичные ошибки

- Думать, что attention сам знает порядок токенов: без positional embeddings порядок теряется.
- Путать attention weights с полноценным объяснением решения модели.
- Считать ViT всегда лучше CNN: на малых данных CNN часто выигрывают.
- Забывать квадратичную сложность self-attention по числу токенов.
- Называть patch embedding сверткой только концептуально: реализация может быть линейным слоем или Conv2d с kernel/stride равными patch size.

## Источники

- Материалы курса: `jupiter notebooks/04_01_Attn,_ViT.ipynb`, `Презентации/04_autoregr_diff.pdf`.
- Vaswani et al., Attention Is All You Need.
- Dosovitskiy et al., An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale.
- Touvron et al., Training data-efficient image transformers and distillation through attention.
- Liu et al., Swin Transformer.
