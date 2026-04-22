# Image harmonization

## Источник
- PDF: `image harmonization.pdf`
- Страниц: 36
- Извлечено текста: примерно 6721 символов
- Страниц с малым количеством текста: 11
- Встроенных изображений: 82

## Краткое содержание
Методы гармонизации изображений: как сделать вставленный объект визуально согласованным с фоном по освещению, цвету, контрасту и стилю.

Связанные экзаменационные вопросы: 15. image-to-image, Pix2Pix, SPADE, GauGAN, OASIS; 29. гармонизация изображений.

## Подробный разбор
- **foreground/background mask.** Вход обычно задаётся как композит $I_c$, маска вставленного объекта $M$ и иногда исходный foreground. Модель должна менять главным образом область $M$, сохраняя фон и геометрию объекта; без маски задача превращается в неконтролируемое редактирование.
- **color transfer.** Классический baseline — выравнивание статистик цвета/тона foreground под background в Lab/RGB или через histogram matching. Он хорошо исправляет глобальный оттенок, но плохо работает с локальным освещением, тенями и отражениями.
- **illumination matching.** Гармонизация не про feature matching/RANSAC, а про согласование освещённости, контраста, баланса белого, теней и насыщенности вставленного объекта с окружением. В современных методах это учится свёрточной/transformer-сетью по синтетическим композитам с известным “правильным” изображением.
- **domain adaptation.** Композит и реальная фотография лежат в разных доменах: у вставки могут отличаться камера, экспозиция, цветовая температура, шум и степень резкости. Поэтому используют adversarial/perceptual losses, attention по маске и обучение на датасетах вроде iHarmony4.
- **composite realism.** Реализм оценивается не только пиксельной ошибкой: важны согласованные границы, отсутствие halo-артефактов, правильные тени, масштаб и перспектива. Даже идеально подобранный цвет не спасает композицию, если нарушены геометрия или освещение сцены.
- **harmonization loss.** Типовой набор: $L_1/L_2$ по foreground/whole image, perceptual loss по признакам VGG, adversarial loss для фотореализма и иногда mask-weighted loss, чтобы фон не деградировал. Метрики MSE/PSNR полезны, но могут слабо коррелировать с человеческой оценкой реализма.

## Структура слайдов по извлечённому тексту
- 1. Сапунова Елена М4145
- 2. Гармонизация изображения
- 3. Постановка задачи
- 4. Сложности
- 5. Датасеты
- 6. iHarmony4
- 7. Метрики
- 8. Классические методы
- 9. Deep Learning гармонизация
- 10. Deep Image Harmonization
- 11. Deep Image Harmonization
- 12. Deep Image Harmonization
- 13. Deep Image Harmonization
- 14. Deep Image Harmonization
- 15. Spatial-Separated Attention Module (S²AM)
- 16. Spatial-Separated Attention Module (S²AM)
- 17. Spatial-Separated Attention Module (S²AM)
- 18. Spatial-Separated Attention Module (S²AM)

## Важные фрагменты из слайдов
- стр. 3: Постановка задачи Composite image Harmonized image Классическая формулировка: меняется только foreground Foreground mask Цель: сделать внешний вид переднего плана визуально согласованным с фоном 3
- стр. 4: Сложности •Освещение •Различия в цветовых распределениях и контрасте •Глубина резкости •Семантический контекст сцены 4
- стр. 5: Датасеты Для задачи гармонизации изображений нужны •Original Image •Composite Image •Mask 5
- стр. 6: iHarmony4 Состоит из четырех поддатасетов •HCOCO ~ 42k пар •HAdobe5k ~ 21k пар •HFlickr ~ 8k пар •Hday2night ~ 444 пары 6
- стр. 8: Классические методы Histogram Matching •Считаем гистограмму цветов foreground и background •Преобразуем foreground так, чтобы гистограммы совпадали Color transfer •Меняем цветовое распределение одного изображения, чтобы его статистики (среднее, дисперсия) - стали похожи на статистики другого изображения 8
- стр. 9: Deep Learning гармонизация Deep Image Harmonization (2017) •первая end-to-end CNN-модель для гармонизации •Encoder - Decoder •Чтобы правильно изменить foreground, нужен контекст + семантика 9
- стр. 10: Deep Image Harmonization Encoder •Conv BatchNorm ELU •Нет pooling (downsampling через stride) чтобы не терять фактуру, резкость и локальную структуру 10
- стр. 11: Deep Image Harmonization Harmonization Decoder •Восстанавливает выходное RGB- изображение •Корректирует цвет, яркость, контраст и тон foreground области с учетом контекста сцены •Skip connections из encoder для сохранения текстур •Получает семантические признаки из Scene Parsing Decoder для контекстно- и семантически- осведомлённой гармонизации 11

## Важные рисунки и визуальные слайды
В презентации много страниц, где основной смысл передан схемами/скриншотами. Для таких страниц сохранены крупные встроенные изображения в `_assets`; при повторении темы их стоит смотреть рядом с исходным PDF.

- стр. 2: [_assets/image_harmonization/page_002_01.png](_assets/image_harmonization/page_002_01.png)
- стр. 2: [_assets/image_harmonization/page_002_02.jpg](_assets/image_harmonization/page_002_02.jpg)
- стр. 2: [_assets/image_harmonization/page_002_03.png](_assets/image_harmonization/page_002_03.png)
- стр. 3: [_assets/image_harmonization/page_003_01.png](_assets/image_harmonization/page_003_01.png)
- стр. 3: [_assets/image_harmonization/page_003_02.png](_assets/image_harmonization/page_003_02.png)
- стр. 3: [_assets/image_harmonization/page_003_03.png](_assets/image_harmonization/page_003_03.png)
- стр. 3: [_assets/image_harmonization/page_003_04.png](_assets/image_harmonization/page_003_04.png)
- стр. 3: [_assets/image_harmonization/page_003_06.png](_assets/image_harmonization/page_003_06.png)
- стр. 3: [_assets/image_harmonization/page_003_07.png](_assets/image_harmonization/page_003_07.png)
- стр. 3: [_assets/image_harmonization/page_003_08.png](_assets/image_harmonization/page_003_08.png)
- стр. 3: [_assets/image_harmonization/page_003_09.png](_assets/image_harmonization/page_003_09.png)
- стр. 4: [_assets/image_harmonization/page_004_01.png](_assets/image_harmonization/page_004_01.png)

## Связь с практикой
- Явного практического ноутбука для этой презентации не найдено; использовать как теоретический источник.

## Ключевые термины для повторения
image, harmonization, foreground, loss, background, usion, deep, attention, dovenet, сцены, domain, discriminator, гармонизация, контекст, decoder, computer, изображения, гармонизации

## Замеченные пробелы и что добрать
- Страницы с малым извлекаемым текстом: 1, 2, 7, 14, 18, 23, 25, 28, 29, 31, 34; проверять визуально по PDF/извлечённым изображениям.

## Использование в итоговых ответах
- Вопрос 15: image-to-image, Pix2Pix, SPADE, GauGAN, OASIS
- Вопрос 29: гармонизация изображений
