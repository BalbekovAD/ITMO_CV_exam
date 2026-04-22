# 20. Условная генерация изображений, распутывание вектора шума, обход латентного пространства GAN, CLIP и StyleCLIP

## Краткий ответ

Условная генерация создает изображение не только из случайного шума, но и с учетом условия: класса, текста, сегментации, изображения, позы или другого управляющего сигнала. В GAN это реализуется подачей условия в генератор и дискриминатор. Для управляемого редактирования важны свойства latent space: если направления в нем соответствуют осмысленным факторам, можно менять возраст, позу, стиль, освещение. CLIP связывает изображения и текст в общем embedding space, а StyleCLIP использует CLIP для текстового управления StyleGAN.

## Основные понятия

- **Conditional generation**: генерация $x = G(z, c)$ с условием $c$.
- **Disentanglement**: разделение факторов вариации, например поза отдельно от цвета и идентичности.
- **Latent traversal**: движение по latent space для изучения изменений изображения.
- **Latent direction**: вектор, изменение вдоль которого меняет конкретный атрибут.
- **GAN inversion**: поиск latent code для заданного реального изображения.
- **CLIP**: contrastive image-text model с общим пространством для изображений и текстов.
- **StyleCLIP**: методы редактирования StyleGAN через текстовые подсказки CLIP.

## Условная генерация в GAN

Базовая GAN генерирует:

$$
x = G(z)
$$

Conditional GAN:

$$
\begin{aligned}
x &= G(z, c), \\
D(x, c) &\to \text{real/fake}.
\end{aligned}
$$

Условие можно включать разными способами:

- конкатенация `z` и class embedding;
- conditional batch normalization;
- projection discriminator;
- spatial condition, например segmentation map или pose map;
- encoder condition для image-to-image задач.

Важно, чтобы дискриминатор тоже видел условие, иначе генератор может игнорировать `c` и просто делать реалистичные изображения.

## Распутывание и обход latent space

В хорошо организованном latent space линейные или почти линейные направления соответствуют семантическим изменениям:

$$
w_{\text{new}} = w + \alpha d_{\text{attribute}}
$$

Способы найти направления:

- supervised: обучить линейный классификатор атрибута в latent space, его нормаль задает направление;
- unsupervised: PCA/GANSpace, SeFa, анализ собственных направлений;
- optimization-based: подобрать направление, максимизирующее целевую функцию;
- CLIP-guided: направление определяется текстово-визуальным loss.

GAN inversion:

$$
w^* = \arg\min_w L_{\text{perceptual}}(G(w), x) + \lambda L_{\text{reg}}(w)
$$

После inversion можно редактировать реальное изображение через latent traversal. В StyleGAN часто используют пространства `W` и `W+`; `W+` дает больше точности реконструкции, но хуже сохраняет редактируемость.

## CLIP

CLIP обучается на парах изображение-текст с contrastive loss. Image encoder и text encoder проецируют входы в общее пространство; правильные пары должны иметь высокую cosine similarity, неправильные - низкую.

Упрощенно:

$$
\operatorname{sim}(I, T) = \cos(f_{\text{image}}(I), f_{\text{text}}(T))
$$

CLIP полезен как универсальный semantic scorer: можно оптимизировать изображение или latent code так, чтобы оно соответствовало тексту.

## StyleCLIP

StyleCLIP применяет CLIP к StyleGAN-редактированию. Основные варианты:

- latent optimization: для конкретного изображения оптимизировать latent code под текстовый prompt;
- mapper: обучить сеть, которая по latent code и тексту выдает сдвиг в latent space;
- global directions: заранее найти текстово заданные направления для быстрых редактирований.

CLIP loss может быть directional:

$$
\begin{aligned}
\Delta_T &= E_{\text{text}}(\operatorname{target}) - E_{\text{text}}(\operatorname{source}), \\
\Delta_I &= E_{\text{img}}(\operatorname{edited}) - E_{\text{img}}(\operatorname{original}), \\
L &= 1 - \cos(\Delta_I, \Delta_T).
\end{aligned}
$$

Так модель меняет именно нужный атрибут, а не просто делает изображение похожим на целевой текст.

## Сравнения, плюсы и минусы

Условная GAN эффективна и быстра, но может игнорировать условие или переобучаться на частые сочетания. Latent editing сохраняет идентичность лучше, чем генерация с нуля, но зависит от качества inversion и disentanglement. CLIP дает гибкое текстовое управление без разметки конкретных атрибутов, но его оценки не идеальны: возможны prompt sensitivity, слабая локализация и нежелательные изменения.

## Связь с практикой и материалами курса

Тема связана с `03_generation_VAE_GAN.pdf`, вопросом 16 про StyleGAN, а также с материалами про CLIP и соответствие изображения тексту: `Соотвествие изображений и текста.pdf`, `SSL и CL.pdf`. В практических задачах это основа для интерактивного редактирования изображений и text-guided generation.

## Типичные ошибки

- Подавать условие только в генератор и ожидать строгого следования условию.
- Считать любой latent direction независимым от остальных признаков: disentanglement редко идеален.
- Путать `Z`, `W` и `W+` в StyleGAN.
- Оптимизировать CLIP loss без регуляризации и получать артефакты.
- Считать CLIP полноценной метрикой фотореализма: он оценивает семантическое соответствие, а не качество пикселей.

## Источники

- Материалы курса: `Презентации/03_generation_VAE_GAN.pdf`, `Презентации/Соотвествие изображений и текста.pdf`, `Презентации/SSL и CL.pdf`.
- Radford et al., Learning Transferable Visual Models From Natural Language Supervision.
- Patashnik et al., StyleCLIP: Text-Driven Manipulation of StyleGAN Imagery.
- Härkönen et al., GANSpace.
- Shen et al., Interpreting the Latent Space of GANs for Semantic Face Editing.
