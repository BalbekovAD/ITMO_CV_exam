# 3. Сверточные нейронные сети. Виды сверток. Пуллинг. Увеличение изображения. Обратная свертка

## Краткий ответ

Сверточная нейронная сеть применяет обучаемые локальные фильтры к изображению и строит иерархию признаков: от границ и текстур к частям объектов и семантическим классам. Свертки используют локальность и разделение весов, поэтому CNN намного эффективнее полносвязных сетей на изображениях. Пуллинг уменьшает пространственный размер и повышает устойчивость к малым сдвигам. Для восстановления разрешения в сегментации, генерации и super-resolution используют upsampling, transposed convolution и другие варианты увеличения feature maps.

## Основные понятия

- Feature map: карта активаций после фильтра.
- Kernel/filter: обучаемая матрица весов.
- Stride: шаг применения фильтра.
- Padding: дополнение границ.
- Receptive field: область исходного изображения, влияющая на нейрон.
- Channel: канал признаков, не обязательно RGB.
- Downsampling/upsampling: уменьшение или увеличение пространственного разрешения.

## Алгоритмы, архитектуры, формулы

Обычная 2D-свертка:

$$
Y[c_{\text{out}}, i, j] =
\sum_c \sum_u \sum_v W[c_{\text{out}}, c, u, v] X[c, i+u, j+v] + b[c_{\text{out}}]
$$

Размер выхода:

$$
H_{\text{out}} = \left\lfloor \frac{H + 2P - K}{S} \right\rfloor + 1
$$

где `H` - входная высота, `P` - padding, `K` - kernel size, `S` - stride.

Виды сверток:

- обычная convolution;
- `1 x 1` convolution: смешивает каналы, меняет их число, используется в bottleneck;
- dilated/atrous convolution: расширяет receptive field без уменьшения разрешения;
- grouped convolution: делит каналы на группы;
- depthwise separable convolution: depthwise по каналам + pointwise `1 x 1`, экономит параметры;
- transposed convolution: обучаемое увеличение разрешения;
- deformable convolution: обучаемые смещения точек выборки.

Пуллинг:

- max pooling: берет максимум в окне;
- average pooling: усредняет;
- global average pooling: превращает карту `H x W x C` в вектор `C`.

Увеличение изображения/feature maps:

- nearest neighbor: быстро, но грубо;
- bilinear/bicubic interpolation: гладко, без обучаемых параметров;
- unpooling: использует индексы max pooling;
- transposed convolution: обучаемый upsampling;
- sub-pixel convolution / pixel shuffle: часто в super-resolution.

Transposed convolution не является строгой обратной сверткой в смысле восстановления потерянной информации. Это операция, соответствующая транспонированной матрице линейной свертки, которая увеличивает пространственный размер.

## Сравнения, плюсы и минусы

Max pooling:

- плюс: устойчивость к малым сдвигам;
- минус: теряет точную локализацию.

Strided convolution:

- плюс: обучаемое уменьшение размера;
- минус: может терять детали.

Transposed convolution:

- плюс: обучаемое восстановление разрешения;
- минус: может давать checkerboard artifacts.

Bilinear upsampling + convolution:

- плюс: часто стабильнее визуально;
- минус: меньше гибкости, чем полностью обучаемый upsampling.

## Связь с практикой и материалами курса

Эта тема напрямую связана с ноутбуками `01_1. PyTorch basics, CNNs.ipynb`, `01_2. VGG, Transfer Learning.ipynb`, `01_3. CNNs, Detection, Yolov1.ipynb`, а также с сегментацией и генеративными моделями. CNN-блоки лежат в основе VGG, ResNet, YOLO, U-Net, автоэнкодеров, GAN и многих depth/segmentation моделей.

## Типичные ошибки

- Называть transposed convolution точным обращением обычной свертки.
- Забывать, что padding и stride меняют размер feature map.
- Не различать channels и spatial dimensions.
- Использовать pooling в dense prediction задачах без механизма восстановления разрешения.
- Считать, что большая глубина всегда лучше без учета переобучения и вычислений.

## Источники

- LeCun et al., *Gradient-Based Learning Applied to Document Recognition*, 1998.
- Dumoulin, Visin, *A guide to convolution arithmetic for deep learning*, 2016.
- Материалы курса: `01_cnn_classification_detection.pdf`, ноутбуки по PyTorch/CNN/VGG.
