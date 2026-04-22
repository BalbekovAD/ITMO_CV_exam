# Сегментация, видео, OCR, depth, face recognition

## Источник
- PDF: `02_segmentation_video.pdf`
- Страниц: 71
- Извлечено текста: примерно 31125 символов
- Страниц с малым количеством текста: 6
- Встроенных изображений: 264

## Краткое содержание
Лекция объединяет dense prediction: сегментацию, видеоаналитику, трекинг, OCR, карты глубины, распознавание лиц и скелетные модели.

Связанные экзаменационные вопросы: 7. OCR; 8. семантическая сегментация; 9. карта глубины и вырезание объектов; 10. обработка видеопотока; 11. скелетные модели; 19. распознавание лиц.

## Подробный разбор
- **семантическая, instance и panoptic segmentation.** Задача dense prediction: каждому пикселю назначается класс, объект или panoptic-метка.
- **FCN, U-Net, DeepLab, encoder-decoder и skip connections.** FCN заменяет fully connected слои на свёрточные и выдаёт dense-карту; U-Net возвращает детали через skip connections; DeepLab использует atrous/dilated convolutions и ASPP для большего контекста без грубого downsampling.
- **обработка видеопотока, temporal consistency, optical flow, tracking-by-detection.** В видео важна согласованность между кадрами: optical flow переносит признаки/маски, tracking-by-detection связывает объекты по времени, а temporal smoothing снижает мерцание предсказаний.
- **OCR: детекция текста, распознавание последовательности, CTC/attention.** Пайплайн обычно разделяет детекцию текстовых областей и распознавание последовательности символов.
- **монокулярная глубина и вырезание объектов по маске/глубине.** Глубина описывает расстояние до сцены; монокулярная оценка неоднозначна и часто требует learned priors.
- **face recognition: детекция, выравнивание, embedding, metric learning.** Пайплайн: найти лицо, выровнять по landmarks, извлечь embedding и сравнить cosine/L2. Обучение часто использует triplet/contrastive loss или margin-softmax семейство ArcFace/CosFace.

## Структура слайдов по извлечённому тексту
- 1. ОБРАЗОВАТЕЛЬНЫЕ ПРОГРАММЫ В ОБЛАСТИ
- 2. Задача сегментации
- 3. Семантическая сегментация (Semantic
- 4. Название данного слайда
- 5. Название данного слайда
- 6. Название данного слайда
- 7. Вероятность каждого класса в отдельном канале
- 8. У backbone для классификации отрежем последние
- 9. Max pooling – необратимая операция
- 10. Max pooling – необратимая операция
- 11. Max pooling – необратимая операция
- 12. Max pooling – необратимая операция
- 13. Предложена в 2015 году
- 14. 2015. – С. 234-241.
- 15. 3х3 сверточные слои
- 16. Конкатенируем
- 17. Конкатенируем высокоуровневые
- 18. Конкатенируем высокоуровневые

## Важные фрагменты из слайдов
- стр. 1: ОБРАЗОВАТЕЛЬНЫЕ ПРОГРАММЫ В ОБЛАСТИ ТЕХНОЛОГИЙ ИСКУССТВЕННОГО ИНТЕЛЛЕКТА Сегментация изображений Ефимова Валерия Александровна vefimova@itmo.ru 12.02.2025 1
- стр. 2: • Задача сегментации • Функции ошибки для сегментации • Сети для сегментации изображений (FCN, U-Net, PSPNet, DeepLab) • Segment Anything Название данного слайда 2 План
- стр. 3: • Семантическая сегментация (Semantic Segmentation) – каждому пикселю сопоставлен класс, соответствующий объекту, который в нем находится, нет разницы между объектами. • Сегментация сущностей (Instance Segmentation) – разделяем объекты одного класса на разные сущности, некоторые пиксели (в которых нет объектов, фон) могут быть не размечены. • Паноптическая сегментация (Panoptic Segmentation) – есть разделение на объе
- стр. 7: • Вероятность каждого класса в отдельном канале • Ранее уменьшали размерности, чтобы охватить изображение целиком Название данного слайда 7 Семантическая сегментация img CNN pclass c – число классов мелкие объекты – vs – много вычислений
- стр. 8: У backbone для классификации отрежем последние полносвязные слои Название данного слайда 8 Fully Convolutional Networks Long J., Shelhamer E., Darrell T. Fully convolutional networks for semantic segmentation //Proceedings of the IEEE conference on computer vision and pattern recognition. – 2015. – С. 3431-3440.
- стр. 9: Max pooling – необратимая операция Название данного слайда 9 Fully Convolutional Networks Long J., Shelhamer E., Darrell T. Fully convolutional networks for semantic segmentation //Proceedings of the IEEE conference on computer vision and pattern recognition. – 2015. – С. 3431-3440. Какие есть методы увеличения изображения?
- стр. 10: Max pooling – необратимая операция Название данного слайда 1 0 Fully Convolutional Networks Long J., Shelhamer E., Darrell T. Fully convolutional networks for semantic segmentation //Proceedings of the IEEE conference on computer vision and pattern recognition. – 2015. – С. 3431-3440. 1. Ближайшие соседи (не обучается) 2. Би-линейная интерполяция (не обучается) 3. Max Unpooling (не обучается) 4. Transposed convolutio
- стр. 11: Max pooling – необратимая операция Название данного слайда 1 1 Fully Convolutional Networks bottleneck Long J., Shelhamer E., Darrell T. Fully convolutional networks for semantic segmentation //Proceedings of the IEEE conference on computer vision and pattern recognition. – 2015. – С. 3431-3440.

## Важные рисунки и визуальные слайды
В презентации много страниц, где основной смысл передан схемами/скриншотами. Для таких страниц сохранены крупные встроенные изображения в `_assets`; при повторении темы их стоит смотреть рядом с исходным PDF.

- стр. 3: [_assets/02_segmentation_video/page_003_02.jp2](_assets/02_segmentation_video/page_003_02.jp2)
- стр. 4: [_assets/02_segmentation_video/page_004_02.jpg](_assets/02_segmentation_video/page_004_02.jpg)
- стр. 5: [_assets/02_segmentation_video/page_005_02.jpg](_assets/02_segmentation_video/page_005_02.jpg)
- стр. 6: [_assets/02_segmentation_video/page_006_02.jpg](_assets/02_segmentation_video/page_006_02.jpg)
- стр. 7: [_assets/02_segmentation_video/page_007_02.png](_assets/02_segmentation_video/page_007_02.png)
- стр. 8: [_assets/02_segmentation_video/page_008_02.jpg](_assets/02_segmentation_video/page_008_02.jpg)
- стр. 8: [_assets/02_segmentation_video/page_008_03.png](_assets/02_segmentation_video/page_008_03.png)
- стр. 9: [_assets/02_segmentation_video/page_009_02.png](_assets/02_segmentation_video/page_009_02.png)
- стр. 10: [_assets/02_segmentation_video/page_010_02.png](_assets/02_segmentation_video/page_010_02.png)
- стр. 11: [_assets/02_segmentation_video/page_011_02.png](_assets/02_segmentation_video/page_011_02.png)
- стр. 12: [_assets/02_segmentation_video/page_012_02.png](_assets/02_segmentation_video/page_012_02.png)
- стр. 12: [_assets/02_segmentation_video/page_012_03.png](_assets/02_segmentation_video/page_012_03.png)

## Связь с практикой
- `02_02_Segmentation,_Tracking.ipynb`: UNet сегментация, Kaggle датасет, Проверка картинок, PyTorch датасет и даталоадер, Classic U-net
- `02_03_how_to_segment_anything_with_sam.ipynb`: Segment Anything Model (SAM), Перед началом, Установка Segment Anything Model (SAM) и зависимостей, Скачаем веса SAM, Скачаем данные для примера
- `02_04_SegmentAnything_and_pytorch.ipynb`: Работа с изображениями, Особенности работы с изображениями, Подбор датасета, Форматы разметки изображений, Хорошие и плохие датасеты для машинного обучения
- `02_05_Face_Recognition,_Depth_Anything.ipynb`: Face Recognition, Датасет LFW, Детекция лица, Yolov8n-face (with keypoints), Отрисовка бокса и ключевых точек

## Ключевые термины для повторения
название, данного, слайда, u-net, объектов, image, segmentation, convolutional, arxiv, networks, conference, ieee, видео, контроль, fully, между, international, https

## Замеченные пробелы и что добрать
- Страницы с малым извлекаемым текстом: 4, 5, 6, 20, 31, 44; проверять визуально по PDF/извлечённым изображениям.
- Для OCR полезно разделять document layout, text detection и sequence recognition.

## Использование в итоговых ответах
- Вопрос 7: OCR
- Вопрос 8: семантическая сегментация
- Вопрос 9: карта глубины и вырезание объектов
- Вопрос 10: обработка видеопотока
- Вопрос 11: скелетные модели
- Вопрос 19: распознавание лиц
