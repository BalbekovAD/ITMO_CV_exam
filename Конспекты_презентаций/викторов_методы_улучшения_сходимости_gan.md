# Методы улучшения сходимости GAN

## Источник
- PDF: `Викторов_Методы_улучшения_сходимости_GAN.pdf`
- Страниц: 26
- Извлечено текста: примерно 5521 символов
- Страниц с малым количеством текста: 9
- Встроенных изображений: 34

## Краткое содержание
Доклад о проблемах обучения GAN и практиках стабилизации: баланс G/D, mode collapse, Wasserstein loss, gradient penalty, spectral normalization.

Связанные экзаменационные вопросы: 14. GAN, проблемы и стабилизация; 16. StyleGAN.

## Подробный разбор
- **mode collapse.** Генератор покрывает лишь часть распределения данных: картинки выглядят правдоподобно, но разнообразие падает. Симптомы — повторяющиеся образцы, плохой recall и расхождение precision/recall для генеративных моделей.
- **vanishing gradients.** Если дискриминатор слишком силён, saturating loss даёт генератору почти нулевой градиент. Поэтому используют non-saturating loss, WGAN-постановку, label smoothing и баланс шагов D/G.
- **WGAN.** Важно понимать состязательную постановку, баланс генератора и дискриминатора, mode collapse и способы стабилизации.
- **gradient penalty.** В WGAN-GP штрафуют отклонение нормы градиента дискриминатора/критика от 1 на интерполяциях между real и fake, чтобы приблизить 1-Lipschitz constraint без жёсткого clipping весов.
- **spectral normalization.** Делит веса слоя на оценку максимального сингулярного числа, ограничивая Lipschitz constant дискриминатора. Это стабилизирует обучение и обычно дешевле gradient penalty.
- **TTUR.** Two Time-Scale Update Rule использует разные learning rates/скорости обновления для генератора и дискриминатора. Идея — не дать одной стороне игры резко доминировать и сорвать сходимость.

## Структура слайдов по извлечённому тексту
- 1. Методы улучшения сходимости
- 2. Generative adversarial network
- 3. Generative adversarial network
- 4. Non-Saturating Loss
- 5. Least Squares Generative Adversarial
- 6. Least Squares Generative Adversarial
- 7. Wasserstein GAN (WGAN)
- 8. Wasserstein GAN (WGAN)
- 9. Wasserstein GAN (WGAN)
- 10. WGAN-GP
- 11. Wasserstein GAN (WGAN)
- 12. Spectral Normalization GAN (SN-GAN)
- 13. Spectral Normalization GAN (SN-GAN)
- 14. Progressive Growing of GANs
- 15. Progressive Growing of GANs
- 25. Two Time-Scale Update Rule (TTUR)
- 26. Спасибо за внимание!

## Важные фрагменты из слайдов
- стр. 1: Методы улучшения сходимости GAN Викторов Борис Викторович М4145 Обработка и генерация изображений Весна 2026 г.
- стр. 2: Generative adversarial network Content preview from Machine Learning with Scala Quick Start Guide
- стр. 3: Generative adversarial network • Дискриминатор и Генератор играют в "минимакс игру": • Дискриминатор обучается максимизировать: • Генератор обучается минимизировать: Goodfellow I. J. et al. Generative adversarial nets //Advances in neural information processing systems. – 2014. – Т. 27.
- стр. 4: Non-Saturating Loss • Замена функции ошибки для генератора с на • Исходный вариант имеет маленький градиент на раннем этапе обучения и большой градиент при сходимости, а предложенный наоборот. Goodfellow I. J. et al. Generative adversarial nets //Advances in neural information processing systems. – 2014. – Т. 27.
- стр. 5: Least Squares Generative Adversarial Networks(LSGAN) • Предлагается схема a-b для дискриминатора, где a и b - метки для фейковых данных и реальных данных соответственно. Перейдём к квадратичной функции ошибки: • Дискриминатор учится отвечать 𝑎 для фейков и 𝑏 для настоящих данных, а генератор хочет убедить его отвечать 𝑐 на фейках. Обычно берут просто 𝑎 = 0, 𝑏 = 𝑐 = 1. Mao X. et al. Least squares generative adversaria
- стр. 6: Least Squares Generative Adversarial Networks(LSGAN) Mao X. et al. Least squares generative adversarial networks //Proceedings of the IEEE international conference on computer vision. – 2017. – С. 2794-2802.
- стр. 7: Wasserstein GAN (WGAN) • Давайте посмотрим на другие метрики близости между 𝑝data и 𝑝model. • Earth Mover distance, или Wasserstein-1: • Двойственность Монжа-Канторовича (Kantorovich-Rubinstein duality) говорит, что данная метрика эквивалетна: • где супремум берётся по всем функциям с липшицевой константой ≤ 1. Arjovsky M., Chintala S., Bottou L. Wasserstein generative adversarial networks //International conference
- стр. 8: Wasserstein GAN (WGAN) Arjovsky M., Chintala S., Bottou L. Wasserstein generative adversarial networks //International conference on machine learning. – Pmlr, 2017. – С. 214-223.

## Важные рисунки и визуальные слайды
В презентации много страниц, где основной смысл передан схемами/скриншотами. Для таких страниц сохранены крупные встроенные изображения в `_assets`; при повторении темы их стоит смотреть рядом с исходным PDF.

- стр. 2: [_assets/викторов_методы_улучшения_сходимости_gan/page_002_01.png](_assets/викторов_методы_улучшения_сходимости_gan/page_002_01.png)
- стр. 16: [_assets/викторов_методы_улучшения_сходимости_gan/page_016_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_016_01.jpg)
- стр. 17: [_assets/викторов_методы_улучшения_сходимости_gan/page_017_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_017_01.jpg)
- стр. 18: [_assets/викторов_методы_улучшения_сходимости_gan/page_018_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_018_01.jpg)
- стр. 19: [_assets/викторов_методы_улучшения_сходимости_gan/page_019_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_019_01.jpg)
- стр. 20: [_assets/викторов_методы_улучшения_сходимости_gan/page_020_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_020_01.jpg)
- стр. 21: [_assets/викторов_методы_улучшения_сходимости_gan/page_021_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_021_01.jpg)
- стр. 22: [_assets/викторов_методы_улучшения_сходимости_gan/page_022_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_022_01.jpg)
- стр. 23: [_assets/викторов_методы_улучшения_сходимости_gan/page_023_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_023_01.jpg)
- стр. 24: [_assets/викторов_методы_улучшения_сходимости_gan/page_024_01.jpg](_assets/викторов_методы_улучшения_сходимости_gan/page_024_01.jpg)

## Связь с практикой
- `03_02_GANs.ipynb`: GAN, CGAN (conditional gan), WGAN и WGAN-GP, WGAN, WGAN-GP

## Ключевые термины для повторения
generative, adversarial, arxiv, networks, wasserstein, gans, international, conference, machine, learning, least, squares, дискриминатора, wgan, spectral, normalization, preprint, progressive

## Замеченные пробелы и что добрать
- Страницы с малым извлекаемым текстом: 16, 17, 18, 19, 20, 21, 22, 23, 24; проверять визуально по PDF/извлечённым изображениям.
- Для GAN обязательно добрать математическую формулировку minimax/Wasserstein loss и практические симптомы mode collapse.

## Использование в итоговых ответах
- Вопрос 14: GAN, проблемы и стабилизация
- Вопрос 16: StyleGAN
