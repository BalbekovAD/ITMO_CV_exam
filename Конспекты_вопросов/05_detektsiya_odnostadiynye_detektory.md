# 5. Детектирование объектов на изображении, одностадийные детекторы

## Краткий ответ

Детекция объектов отвечает не только на вопрос "что на изображении?", но и "где это находится?". Результат - набор bounding boxes, классов и confidence scores. Одностадийные детекторы предсказывают классы и координаты боксов за один проход по feature map, без отдельного этапа генерации region proposals. Главные примеры: YOLO, SSD, RetinaNet. Их сильная сторона - скорость и пригодность для real-time.

## Основные понятия

- Bounding box: прямоугольник объекта, обычно `(x, y, w, h)` или `(x1, y1, x2, y2)`.
- Confidence/objectness: уверенность, что в боксе есть объект.
- IoU: intersection over union, мера совпадения боксов.
- Anchor box: заранее заданная форма бокса.
- NMS: non-maximum suppression, удаление дублирующих предсказаний.
- AP/mAP: площадь под precision-recall кривой для класса и среднее AP по классам/IoU-порогам.

## Алгоритмы, архитектуры, формулы

IoU:

$$
\operatorname{IoU}(A, B) =
\frac{\operatorname{area}(A \cap B)}{\operatorname{area}(A \cup B)}
$$

Precision и recall для детекции считаются после сопоставления предсказаний с ground truth по IoU-порогу:

$$
\begin{aligned}
\operatorname{precision} &= \frac{TP}{TP + FP}, \\
\operatorname{recall} &= \frac{TP}{TP + FN}, \\
AP &= \text{area under precision-recall curve}.
\end{aligned}
$$

Общий pipeline одностадийного детектора:

1. backbone извлекает признаки;
2. detection head на каждой ячейке/позиции предсказывает боксы, objectness и классы;
3. боксы декодируются в координаты изображения;
4. отбрасываются низкие confidence;
5. применяется NMS.

YOLOv1:

- делит изображение на сетку `S x S`;
- каждая ячейка отвечает за объект, центр которого попал в нее;
- предсказывает несколько боксов и class probabilities;
- loss объединяет ошибку координат, confidence и классификации.

SSD:

- делает предсказания на нескольких feature maps разного разрешения;
- использует default/anchor boxes разных масштабов и aspect ratios;
- лучше YOLOv1 работает с объектами разных размеров.

RetinaNet:

- одностадийный detector с Feature Pyramid Network;
- ключевая идея - focal loss для борьбы с дисбалансом easy background examples.

Focal loss:

$$
FL(p_t) = -\alpha (1 - p_t)^\gamma \log(p_t)
$$

Она уменьшает вклад легких примеров и концентрирует обучение на трудных.

## Сравнения, плюсы и минусы

Одностадийные детекторы:

- плюс: быстрые, удобны для видео и edge inference;
- плюс: простее pipeline;
- минус: исторически уступали двухстадийным по точности на малых объектах;
- минус: требуют аккуратной настройки anchors/loss/NMS, хотя современные anchor-free версии уменьшают зависимость от anchors.

YOLO:

- плюс: высокая скорость, единый end-to-end подход;
- минус: ранние версии хуже локализовали малые и плотные объекты.

SSD:

- плюс: multi-scale detection;
- минус: зависит от набора default boxes.

RetinaNet:

- плюс: сильный баланс точности и скорости;
- минус: focal loss добавляет гиперпараметры.

## Связь с практикой и материалами курса

Тема напрямую связана с `01_cnn_classification_detection.pdf`, ноутбуками `01_3. CNNs, Detection, Yolov1.ipynb` и `02_01_(CNNs,_Detection,_Yolov1).ipynb`. На экзамене важно уметь объяснить YOLOv1 как базовый одностадийный подход и связать его с общими понятиями IoU, anchors, NMS и mAP.

## Типичные ошибки

- Путать classification confidence и objectness.
- Считать, что NMS является обучаемой частью модели.
- Оценивать детектор только accuracy, а не mAP/precision-recall.
- Не учитывать IoU threshold и протокол mAP, например `AP50` против COCO-style `AP@[.50:.95]`.
- Забывать про проблему дисбаланса фон/объект.
- Сравнивать confidence разных моделей без калибровки порогов и одинакового postprocessing.

## Источники

- Redmon et al., *You Only Look Once: Unified, Real-Time Object Detection*, 2016.
- Liu et al., *SSD: Single Shot MultiBox Detector*, 2016.
- Lin et al., *Focal Loss for Dense Object Detection*, 2017.
- Материалы курса: `01_cnn_classification_detection.pdf`, ноутбуки по YOLOv1.
