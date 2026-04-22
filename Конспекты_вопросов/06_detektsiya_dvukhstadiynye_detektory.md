# 6. Детектирование объектов на изображении, двухстадийные детекторы

## Краткий ответ

Двухстадийные детекторы сначала находят кандидаты областей, где могут быть объекты, а затем классифицируют эти области и уточняют координаты боксов. Типичная линия развития: R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN. По сравнению с одностадийными подходами они обычно точнее, особенно на сложных сценах, но медленнее и имеют более сложный pipeline.

## Основные понятия

- Region proposal: кандидатная область объекта.
- RPN: Region Proposal Network.
- RoI: region of interest.
- RoI Pooling / RoI Align: преобразование признаков области к фиксированному размеру.
- Bounding box regression: уточнение координат бокса.
- Positive/negative samples: proposals, размеченные по IoU с ground truth.

## Алгоритмы, архитектуры, формулы

R-CNN:

1. selective search генерирует region proposals;
2. каждый proposal вырезается и пропускается через CNN;
3. SVM классифицирует признаки;
4. отдельная регрессия уточняет box.

Минус: очень медленно, потому что CNN запускается много раз.

Fast R-CNN:

1. CNN считается один раз для всего изображения;
2. proposals проецируются на feature map;
3. RoI Pooling делает фиксированный размер;
4. одна сеть предсказывает класс и bbox regression.

Faster R-CNN:

- заменяет selective search на обучаемую RPN;
- RPN скользит по feature map и предсказывает objectness + bbox offsets для anchors;
- вторая стадия классифицирует proposals и уточняет координаты.

Параметризация bbox regression часто задается через смещения:

$$
\begin{aligned}
t_x &= \frac{x - x_a}{w_a}, \\
t_y &= \frac{y - y_a}{h_a}, \\
t_w &= \log\frac{w}{w_a}, \\
t_h &= \log\frac{h}{h_a}.
\end{aligned}
$$

Mask R-CNN:

- расширяет Faster R-CNN веткой instance mask;
- использует RoI Align вместо RoI Pooling, чтобы избежать грубого квантования;
- решает instance segmentation, но базируется на двухстадийной детекции.

RoI Pooling округляет координаты proposal на feature map, из-за чего теряется точность локализации. RoI Align использует билинейную интерполяцию в дробных координатах и поэтому особенно важен для масок и keypoints.

## Сравнения, плюсы и минусы

Двухстадийные детекторы:

- плюс: высокая точность локализации;
- плюс: лучше работают на сложных объектах и плотных сценах;
- плюс: легко расширяются до instance segmentation;
- минус: медленнее одностадийных;
- минус: сложнее обучение и inference.

R-CNN:

- плюс: исторически важный переход к CNN-детекции;
- минус: непрактично медленный.

Faster R-CNN:

- плюс: end-to-end proposals через RPN;
- минус: тяжелее real-time YOLO-подходов.

## Связь с практикой и материалами курса

Тема дополняет вопрос об одностадийных детекторах из `01_cnn_classification_detection.pdf`. Для практики важно понимать различие: YOLO/SSD/RetinaNet сразу делают dense predictions, Faster R-CNN сначала строит ограниченное число качественных proposals. Mask R-CNN связан с последующими темами сегментации.

## Типичные ошибки

- Называть Faster R-CNN одностадийным из-за общей CNN-backbone.
- Путать RoI Pooling и обычный max pooling.
- Не понимать отличие RoI Pooling от RoI Align и влияние квантования на качество масок.
- Не понимать, зачем нужна RPN, если уже есть backbone.
- Игнорировать IoU thresholds при назначении positive/negative anchors.
- Сравнивать скорость без учета размера backbone и разрешения входа.

## Источники

- Girshick et al., *Rich feature hierarchies for accurate object detection and semantic segmentation*, 2014.
- Girshick, *Fast R-CNN*, 2015.
- Ren et al., *Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks*, 2015.
- He et al., *Mask R-CNN*, 2017.
