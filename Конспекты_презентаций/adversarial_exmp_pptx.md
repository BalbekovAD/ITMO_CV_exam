# Adversarial examples

## Источник
- PDF: `adversarial exmp.pptx.pdf`
- Страниц: 13
- Извлечено текста: примерно 3013 символов
- Страниц с малым количеством текста: 2
- Встроенных изображений: 17

## Краткое содержание
Доклад о состязательных примерах: малые возмущения изображения, которые меняют ответ нейросети, и методы защиты.

Связанные экзаменационные вопросы: 1. задачи CV и классические методы; 3. CNN, свёртки, pooling, upsampling; 4. классификация, VGG, ResNet, Inception, transfer learning.

## Подробный разбор
- **FGSM.** Одношаговая white-box атака: $x_{\text{adv}} = x + \epsilon\operatorname{sign}(\nabla_x L(x,y))$. Быстрая, но обычно слабее итеративных методов и чувствительна к выбранному $\epsilon$.
- **PGD.** Итеративная атака: несколько шагов градиента с проекцией обратно в $L_p$-шар вокруг исходного изображения. Часто считается сильным baseline для оценки adversarial robustness.
- **targeted/untargeted attacks.** Untargeted атака хочет любой неверный класс, targeted — конкретный класс-цель и обычно сложнее. Для targeted меняется знак/цель оптимизации: минимизируют loss к target label.
- **robustness.** Устойчивость измеряют accuracy под атакой с заданной нормой, бюджетом и числом шагов. Нельзя делать вывод по слабой атаке: gradient masking может создавать иллюзию защиты.
- **adversarial training.** Обучение на adversarial examples решает min-max задачу и обычно улучшает устойчивость, но снижает clean accuracy и требует дорогого inner-loop поиска атак.
- **transferability.** Примеры, построенные на одной модели, часто атакуют другую из-за похожих decision boundaries. Это делает black-box атаки практичными даже без доступа к градиентам целевой модели.

## Структура слайдов по извлечённому тексту
- 1. Состязательные
- 2. Состязательные примеры
- 3. (x, y)
- 4. Введение
- 5. Алгоритмы x ̃ :
- 6. Fast Gradient Sign Method:
- 8. $x_{\text{adv}} = x + \epsilon \operatorname{sign}(\nabla_x \ell(f(x), y))$ - FGSM
- 9. Fast Gradient Sign Method:
- 10. FGSM vs I-FGSM
- 11. 1. Выбор направления: d ∈ {−1, +1}^n
- 12. ● ASR: кол - во успешных атак / число примеров
- 13. Спасибо

## Важные фрагменты из слайдов
- стр. 2: Состязательные примеры 1. Введение 2. Состязательные атаки 3. FGSM и T-FGSM 4. I-FGSM 5. FGSM vs I-FGSM 6.RayS 7. Метрики 8. Выводы 2
- стр. 3: $(x, y)$, где $x$ - объект (картинка), $y$ - истинная метка, $f$ - модель, $f(x) = y$; $\tilde{x}: \tilde{x} \approx x,\ f(\tilde{x}) \ne y$. Введение 3
- стр. 4: *Explaining and Harnessing Adversarial Examples Ian Goodfellow, Jonathon Shlens, Christian Szegedy 2014 arXiv: 1412.6572 Введение 4
- стр. 5: Алгоритмы $\tilde{x}$: Типы атак: Состязательные атаки 5 *Towards Evaluating the Robustness of Neural Networks Carlini & Wagner, 2017 arXiv: 1608.04644 ● white box: атакующий знает параметры $\theta$ ● black box: у атакующего есть доступ только к оракулу ● untargeted: $f(\tilde{x}) \ne y$ ● targeted: $f(\tilde{x}) = t$
- стр. 6: Fast Gradient Sign Method: ● White box ● Градиентная атака ● Одношаговая атака ● Обычно untargeted(цель – вызвать ошибку классификации) Идея: линейная аппроксимация функции потерь Плюсы: быстро Минусы: слабее итеративных атак FGSM 6 *Explaining and Harnessing Adversarial Examples Ian Goodfellow, Jonathon Shlens, Christian Szegedy 2014 arXiv: 1412.6572
- стр. 7: FGSM 7 *https://neptune.ai/blog/adversarial-attacks-on-neural-networks-exploring-the-fast-gradient-sign-method
- стр. 8: $x_{\text{adv}} = x + \epsilon\operatorname{sign}(\nabla_x \ell(f(x), y))$ - FGSM ● $\max \ell(f(x+\delta), y)$ ● $\lVert\delta\rVert_\infty \le \epsilon$ ● $x_{\text{adv}} = x - \epsilon\operatorname{sign}(\nabla_x \ell(f(x), t))$ - T-FGSM ● $\min \ell(f(x+\delta), t)$ ● $\lVert\delta\rVert_\infty \le \epsilon$ ● Ни один пиксель не изменится больше чем на $\epsilon$ ● Изменение остается малозаметным FGSM 8 *Explaining and Harnessing Adversarial Examples Ian Goodfellow, Jonathon Shlens, Christian Szegedy 2014 arXiv: 1412.6572 $x$ - исходное изображение, $x_{\text{adv}}$ - состязательный пример
- стр. 9: Fast Gradient Sign Method: ● White box ● Градиентная атака ● Итеративная атака ● Обычно untargeted $x_{k+1} = \min(\max(x_k + \alpha\operatorname{sign}(\nabla_x \ell), x-\epsilon), x+\epsilon)$ ● $\max \ell(f(x+\delta), y)$ при $\lVert\delta\rVert_\infty \le \epsilon$ ● I-FGSM 9 *Adversarial Examples in the Physical World Alexey Kurakin, Ian Goodfellow, Samy Bengio 2016 arXiv: 1607.02533

## Важные рисунки и визуальные слайды
Большая часть содержания доступна как извлекаемый текст; изображения в основном иллюстрируют уже описанные идеи.

- Крупные изображения отдельно не извлекались.

## Связь с практикой
- Явного практического ноутбука для этой презентации не найдено; использовать как теоретический источник.

## Ключевые термины для повторения
fgsm, xadv, i-fgsm, adversarial, arxiv, sign, состязательные, examples, goodfellow, атака, введение, rays, explaining, harnessing, jonathon, shlens, christian, szegedy

## Замеченные пробелы и что добрать
- Страницы с малым извлекаемым текстом: 1, 13; проверять визуально по PDF/извлечённым изображениям.

## Использование в итоговых ответах
- Вопрос 1: задачи CV и классические методы
- Вопрос 3: CNN, свёртки, pooling, upsampling
- Вопрос 4: классификация, VGG, ResNet, Inception, transfer learning
