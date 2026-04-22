# 16. Модель StyleGAN, ее архитектура, применение и эволюция

## Краткий ответ

StyleGAN - семейство GAN-моделей для высококачественной генерации изображений, особенно лиц. Главная идея - отделить входной latent vector от управления стилями на разных уровнях генератора. Вместо прямой подачи `z` в генератор используется mapping network, которая переводит `z` в промежуточное пространство `w`; затем `w` управляет слоями генератора через adaptive normalization или modulation. Это делает latent space более управляемым и позволяет менять грубую форму, черты и мелкие текстуры на разных масштабах.

## Основные понятия

- **Latent space Z**: исходное пространство шума.
- **Intermediate latent space W**: пространство после mapping network, часто более disentangled.
- **Mapping network**: MLP, преобразующая `z` в `w`.
- **Synthesis network**: генератор, начинающий не с изображения, а с обучаемой константы.
- **Style modulation**: управление весами/активациями слоев через style vector.
- **Noise injection**: добавление случайного шума для стохастических деталей, например волос или пор кожи.
- **Style mixing**: использование разных `w` на разных слоях.
- **Truncation trick**: приближение `w` к среднему для повышения качества ценой разнообразия.

## Архитектура StyleGAN

Классический GAN:

```text
z -> Generator -> image
```

StyleGAN:

```text
z -> Mapping network -> w
learned constant + styles(w) + noise -> Synthesis network -> image
```

В StyleGAN1 использовалась AdaIN:

$$
\operatorname{AdaIN}(x, y) =
\operatorname{scale}(y)\frac{x - \operatorname{mean}(x)}{\operatorname{std}(x)}
+ \operatorname{bias}(y)
$$

Слои низкого разрешения отвечают за грубую структуру: поза, форма головы, композиция. Средние слои - за черты лица и крупные элементы. Высокие разрешения - за цвет, текстуру, волосы, мелкие детали.

## Эволюция

**Progressive GAN** предшествовал StyleGAN: обучение начиналось с низкого разрешения и постепенно добавляло новые слои. Это помогло стабилизировать high-resolution generation.

**StyleGAN1** ввел mapping network, AdaIN, learned constant, noise injection и style mixing. Недостатки: характерные артефакты, например blob-like artifacts и проблемы с нормализацией.

**StyleGAN2** заменил AdaIN на weight modulation/demodulation, убрал часть артефактов и улучшил качество. Также использовал path length regularization, чтобы изменения в latent space давали более предсказуемые изменения изображения.

**StyleGAN2-ADA** добавил adaptive discriminator augmentation для обучения на малых датасетах без сильного переобучения дискриминатора.

**StyleGAN3** улучшил alias-free генерацию и согласованность при трансформациях: изображение стало меньше "прилипать" к координатной сетке генератора.

## Применение

- генерация лиц и объектов;
- редактирование изображений через latent inversion;
- изменение возраста, пола, выражения, прически, освещения;
- dataset augmentation;
- deepfake-related задачи и их детекция;
- поиск направлений в latent space: GANSpace, SeFa, InterfaceGAN;
- условное редактирование с CLIP/StyleCLIP.

Latent inversion решает задачу: найти `w`, такой что `G(w)` похож на заданное изображение. После этого можно редактировать изображение перемещением в latent space.

## Сравнения, плюсы и минусы

Плюсы StyleGAN: высокое качество, управляемость latent space, быстрая генерация, удобство редактирования. Минусы: ограничение доменом обучения, сложность inversion, артефакты при out-of-domain изображениях, необходимость аккуратного обучения GAN.

По сравнению с diffusion, StyleGAN быстрее и удобнее для latent editing, но хуже в открытой текстовой условной генерации. Diffusion-модели универсальнее, но требуют больше шагов сэмплирования.

## Связь с практикой и материалами курса

Тема связана с `03_generation_VAE_GAN.pdf`, ноутбуком `03_02_GANs.ipynb`, а также с вопросом 20 про обход latent space, CLIP и StyleCLIP. В курсе StyleGAN обычно рассматривается как пример зрелой GAN-архитектуры и как основа для редактирования изображений через латентные направления.

## Типичные ошибки

- Считать, что `z` и `w` одно и то же: `w` получается mapping network и имеет другие свойства.
- Объяснять StyleGAN только как "GAN для лиц": архитектура применима к разным визуальным доменам.
- Путать noise injection со входным latent vector: шум в слоях отвечает за стохастические локальные детали.
- Забывать разницу между StyleGAN1, StyleGAN2 и StyleGAN3.
- Считать truncation trick бесплатным улучшением: качество растет, diversity падает.

## Источники

- Материалы курса: `Презентации/03_generation_VAE_GAN.pdf`, `jupiter notebooks/03_02_GANs.ipynb`.
- Karras et al., A Style-Based Generator Architecture for Generative Adversarial Networks.
- Karras et al., Analyzing and Improving the Image Quality of StyleGAN.
- Karras et al., Training Generative Adversarial Networks with Limited Data.
- Karras et al., Alias-Free Generative Adversarial Networks.
