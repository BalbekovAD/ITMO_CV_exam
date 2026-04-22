# 10. Особенности обработки видеопотока

## Краткий ответ

Видео - это последовательность кадров, поэтому кроме пространственной информации появляется временная: движение, траектории, задержка, частота кадров, межкадровая согласованность. Обработка видеопотока отличается от обработки отдельных изображений требованиями real-time, устойчивостью к изменению освещения и сцены, трекингом объектов, использованием оптического потока/temporal models и борьбой с накоплением ошибок. Для практики важно балансировать точность, latency, throughput и стабильность результатов во времени.

## Основные понятия

- FPS: кадров в секунду.
- Latency: задержка от получения кадра до результата.
- Throughput: пропускная способность системы.
- Optical flow: поле движения пикселей между кадрами.
- Tracking: поддержание идентичности объекта во времени.
- Temporal consistency: согласованность предсказаний на соседних кадрах.
- Online/offline processing: потоковая обработка или анализ всего видео целиком.

## Алгоритмы, архитектуры, формулы

Базовый pipeline real-time video analytics:

1. захват кадра;
2. декодирование и resize;
3. inference модели: detection/segmentation/classification;
4. postprocessing: NMS, masks, filtering;
5. tracking и temporal smoothing;
6. вывод результата или события.

Оптический поток:

- классические методы: Lucas-Kanade, Horn-Schunck;
- современные нейросетевые: FlowNet, PWC-Net, RAFT;
- используется для стабилизации, motion segmentation, интерполяции, tracking.

Уравнение brightness constancy:

$$
\begin{aligned}
I(x, y, t) &= I(x + u, y + v, t + 1), \\
I_x u + I_y v + I_t &= 0.
\end{aligned}
$$

Трекинг:

- tracking-by-detection: детектор на кадрах + ассоциация объектов;
- Kalman filter: прогноз положения;
- Hungarian algorithm: сопоставление predicted tracks и detections;
- SORT: Kalman + IoU association;
- DeepSORT: добавляет appearance embeddings;
- ByteTrack: использует и высокие, и низкие confidence detections.

Видео-модели:

- 3D CNN: свертки по пространству и времени;
- two-stream networks: RGB + optical flow;
- ConvLSTM/GRU: временная память;
- video transformers: attention по пространственно-временным токенам.

## Сравнения, плюсы и минусы

Frame-by-frame обработка:

- плюс: просто использовать image model;
- плюс: легко распараллеливать;
- минус: мерцание предсказаний, нет явного понимания движения.

Temporal smoothing/tracking:

- плюс: стабильные боксы и маски;
- минус: может запаздывать и накапливать ошибки.

3D CNN/video transformers:

- плюс: учитывают движение и контекст;
- минус: тяжелее, требуют больше данных и памяти.

Optical flow:

- плюс: точное низкоуровневое движение;
- минус: чувствителен к размытию, окклюзиям, большим смещениям и вычислительно дорог.

## Связь с практикой и материалами курса

Тема связана с `02_segmentation_video.pdf`, `Доклад про автономный транспорт.pdf`, `Генерация видео.pdf` и ноутбуком `02_02_Segmentation,_Tracking.ipynb`. В задачах автономного транспорта, видеонаблюдения и AR важны не только качество на отдельном кадре, но и стабильность треков, задержка, пропуски кадров, работа с потоковым вводом.

## Типичные ошибки

- Оценивать видеосистему только по точности на отдельных кадрах.
- Не учитывать latency и FPS при выборе модели.
- Заново детектировать все объекты без трекинга, получая нестабильные ID.
- Игнорировать motion blur, compression artifacts и dropped frames.
- Считать, что высокий FPS камеры автоматически означает высокий FPS inference.

## Источники

- Lucas, Kanade, *An Iterative Image Registration Technique with an Application to Stereo Vision*, 1981.
- Horn, Schunck, *Determining Optical Flow*, 1981.
- Bewley et al., *Simple Online and Realtime Tracking*, SORT, 2016.
- Wojke et al., *Simple Online and Realtime Tracking with a Deep Association Metric*, DeepSORT, 2017.
- Материалы курса: `02_segmentation_video.pdf`, `02_02_Segmentation,_Tracking.ipynb`.
