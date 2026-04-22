# 8. Семантическая сегментация, архитектуры нейронных сетей

## Краткий ответ

Семантическая сегментация присваивает каждому пикселю изображения класс: дорога, человек, небо, здание и т.д. В отличие от классификации, модель должна сохранить пространственную структуру, а в отличие от instance segmentation она не разделяет разные экземпляры одного класса. Основные архитектуры: FCN, U-Net, SegNet, DeepLab, PSPNet, а также transformer-based модели и foundation-подходы вроде SAM для сегментации по подсказкам.

## Основные понятия

- Pixel-wise classification: классификация каждого пикселя.
- Encoder-decoder: encoder сжимает признаки, decoder восстанавливает разрешение.
- Skip connections: передают детали из ранних слоев в decoder.
- mIoU: mean intersection over union, ключевая метрика.
- Dice coefficient: частая метрика в медицинской сегментации.
- Semantic vs instance vs panoptic segmentation.

## Алгоритмы, архитектуры, формулы

FCN:

- заменяет fully connected слои на convolutional;
- выдает dense prediction;
- использует upsampling для восстановления разрешения.

U-Net:

- U-образная encoder-decoder архитектура;
- skip connections соединяют уровни одинакового масштаба;
- особенно популярна в медицине и задачах с малым количеством данных.

SegNet:

- encoder-decoder;
- decoder использует индексы max pooling для unpooling.

DeepLab:

- atrous/dilated convolutions увеличивают receptive field без потери разрешения;
- ASPP - atrous spatial pyramid pooling, признаки на разных масштабах;
- CRF в ранних версиях уточнял границы.

PSPNet:

- pyramid pooling module собирает контекст на нескольких масштабах;
- полезно для scene parsing.

Метрики:

$$
\begin{aligned}
\operatorname{IoU}_c &= \frac{TP_c}{TP_c + FP_c + FN_c}, \\
\operatorname{mIoU} &= \operatorname{mean}_c \operatorname{IoU}_c, \\
\operatorname{Dice} &= \frac{2TP}{2TP + FP + FN}.
\end{aligned}
$$

Loss-функции:

- pixel-wise cross-entropy;
- weighted cross-entropy при дисбалансе классов;
- Dice loss;
- focal loss;
- Lovasz-Softmax как приближение IoU.

## Сравнения, плюсы и минусы

FCN:

- плюс: первая простая fully convolutional схема;
- минус: грубые границы.

U-Net:

- плюс: хорошо сохраняет локальные детали;
- плюс: эффективна на небольших датасетах;
- минус: ограниченный глобальный контекст без дополнительных блоков.

DeepLab:

- плюс: сильная многомасштабность и контекст;
- минус: тяжелее и сложнее.

SAM:

- плюс: мощная promptable segmentation;
- минус: сам по себе не всегда дает семантические классы, часто нужен дополнительный классификатор или pipeline.

## Связь с практикой и материалами курса

Тема соответствует `02_segmentation_video.pdf`, ноутбукам `02_02_Segmentation,_Tracking.ipynb`, `02_03_how_to_segment_anything_with_sam.ipynb`, `02_04_SegmentAnything_and_pytorch.ipynb`. На практике сегментация применяется в медицине, автономном транспорте, анализе документов, удалении фона, промышленном контроле и подготовке масок для генеративных моделей.

## Типичные ошибки

- Путать semantic segmentation и instance segmentation.
- Оценивать сегментацию только pixel accuracy при доминирующем фоне.
- Делать сильный downsampling без skip connections и ждать четких границ.
- Не учитывать class imbalance.
- Использовать SAM как полноценную semantic segmentation модель без классификации масок.

## Источники

- Long et al., *Fully Convolutional Networks for Semantic Segmentation*, 2015.
- Ronneberger et al., *U-Net: Convolutional Networks for Biomedical Image Segmentation*, 2015.
- Chen et al., *DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs*, 2017.
- Kirillov et al., *Segment Anything*, 2023.
- Материалы курса: `02_segmentation_video.pdf`, ноутбуки по segmentation/SAM.
