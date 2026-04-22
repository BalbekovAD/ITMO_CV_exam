# 14. Архитектура генеративно-состязательных сетей, их виды. Проблемы GAN и способы улучшения сходимости

## Краткий ответ

GAN, Generative Adversarial Network, состоит из двух сетей: генератора `G`, который преобразует шум или условие в изображение, и дискриминатора `D`, который отличает реальные изображения от сгенерированных. Они обучаются как игра с нулевой суммой: генератор пытается обмануть дискриминатор, а дискриминатор - распознать подделку. GAN применяются для синтеза изображений, image-to-image translation, super-resolution, inpainting, стилизации, редактирования лиц, генерации данных и доменной адаптации.

## Основные понятия

- **Generator**: модель `G(z)` или `G(z, c)`, генерирующая изображение.
- **Discriminator**: бинарный классификатор `D(x)`, оценивающий реалистичность.
- **Latent vector**: входной шум `z`, обычно из `N(0, I)`.
- **Conditional GAN**: генерация с условием `c`: класс, текст, сегментационная карта, изображение.
- **DCGAN**: сверточная GAN-архитектура с convolution/deconvolution слоями.
- **Mode collapse**: генератор покрывает только часть распределения данных.
- **Training instability**: неустойчивое обучение из-за динамики игры `G` и `D`.

## Алгоритмы, архитектуры и формулы

Классическая minimax-цель GAN:

$$
\min_G \max_D V(D, G) =
\mathbb{E}_{x \sim p_{data}}[\log D(x)] +
\mathbb{E}_{z \sim p(z)}[\log(1 - D(G(z)))]
$$

На практике для генератора часто используют non-saturating loss:

$$
\begin{aligned}
L_G &= -\mathbb{E}_z[\log D(G(z))], \\
L_D &= -\mathbb{E}_x[\log D(x)] - \mathbb{E}_z[\log(1 - D(G(z)))].
\end{aligned}
$$

Условная GAN:

$$
\begin{aligned}
G &: (z, c) \to x, \\
D &: (x, c) \to \text{вероятность реальности}.
\end{aligned}
$$

Условие можно подавать конкатенацией, conditional batch normalization, class embedding, projection discriminator или через входное изображение/маску.

DCGAN закрепил практические правила: сверточные слои вместо fully connected, batch normalization, ReLU в генераторе, LeakyReLU в дискриминаторе, transposed convolution или upsampling в генераторе.

## Проблемы GAN и улучшение сходимости

Главные проблемы:

- **Mode collapse**: разные `z` дают похожие изображения.
- **Vanishing gradients**: если `D` слишком силен, `G` получает слабый градиент.
- **Oscillation**: `G` и `D` не сходятся к устойчивому состоянию.
- **Sensitivity to hyperparameters**: важны learning rate, batch size, регуляризация, архитектура.
- **Evaluation difficulty**: loss GAN плохо коррелирует с визуальным качеством.

Способы улучшения:

- **WGAN**: заменить JS divergence на Wasserstein distance:

$$
\begin{aligned}
\max_D\ &\mathbb{E}[D(\text{real})] - \mathbb{E}[D(\text{fake})], \\
\min_G\ &-\mathbb{E}[D(\text{fake})].
\end{aligned}
$$

В WGAN-GP добавляют gradient penalty:

$$
\lambda \mathbb{E}\left[(\lVert \nabla_{\hat{x}} D(\hat{x}) \rVert_2 - 1)^2\right]
$$

- **Spectral normalization**: ограничивает Lipschitz constant дискриминатора.
- **Feature matching**: генератор подгоняет статистики признаков, а не только ответ `D`.
- **Minibatch discrimination**: помогает бороться с mode collapse.
- **Label smoothing/noise**: снижает переобучение дискриминатора.
- **TTUR**: разные learning rates для `G` и `D`.
- **Progressive growing**: обучение от низкого разрешения к высокому.
- **Self-attention**: улучшает глобальную согласованность.
- **ADA/augmentation**: аугментации при малом датасете, чтобы дискриминатор не переобучался.

## Виды GAN и задачи

- **Conditional GAN**: класс-условная генерация, text/image/segmentation-conditioned generation.
- **DCGAN**: базовая сверточная GAN.
- **Pix2Pix**: paired image-to-image translation.
- **CycleGAN**: unpaired translation с cycle consistency.
- **SRGAN/ESRGAN**: super-resolution.
- **StyleGAN**: высококачественная генерация лиц и изображений с управляемым latent space.
- **BigGAN**: class-conditional high-fidelity generation.

## Сравнения, плюсы и минусы

GAN дают резкие и визуально убедительные изображения, но сложны в обучении и могут плохо покрывать распределение. VAE стабильнее, но часто размывает. Diffusion обычно устойчивее и качественнее, но медленнее на инференсе. Авторегрессионные модели дают явное likelihood-моделирование, но генерация пиксель-за-пикселем или токен-за-токеном может быть медленной.

## Связь с практикой и материалами курса

Тема соответствует `03_generation_VAE_GAN.pdf`, `Викторов_Методы_улучшения_сходимости_GAN.pdf`, ноутбукам `03_01_Autoencoders,_DCGAN.ipynb` и `03_02_GANs.ipynb`. В практике обычно реализуют DCGAN, наблюдают баланс `G/D`, mode collapse и влияние архитектурных решений.

## Типичные ошибки

- Интерпретировать loss GAN как обычную монотонную метрику качества.
- Путать дискриминатор обычной GAN и critic в WGAN: critic не обязан выдавать вероятность.
- Делать дискриминатор слишком сильным или слишком слабым.
- Забывать, что conditional GAN должна передавать условие и в `G`, и в `D`.
- Путать transposed convolution с математической обратной сверткой.
- Оценивать GAN только по нескольким красивым примерам без diversity metrics.

## Источники

- Материалы курса: `Презентации/03_generation_VAE_GAN.pdf`, `Презентации/Викторов_Методы_улучшения_сходимости_GAN.pdf`, ноутбук `03_02_GANs.ipynb`.
- Goodfellow et al., Generative Adversarial Nets.
- Radford et al., Unsupervised Representation Learning with Deep Convolutional GANs.
- Arjovsky et al., Wasserstein GAN.
- Gulrajani et al., Improved Training of Wasserstein GANs.
- Miyato et al., Spectral Normalization for GANs.
