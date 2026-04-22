# Генеративное искусство

## Источник
- PDF: `generative_art_ru_with_images123_compressed.pdf`
- Страниц: 37
- Извлечено текста: примерно 6281 символов
- Страниц с малым количеством текста: 18
- Встроенных изображений: 60

## Краткое содержание
Обзор генеративного искусства: процедурные и нейросетевые методы, эстетика, композиция, стилизация, векторная/растровая генерация.

Связанные экзаменационные вопросы: 23. Stable Diffusion, Imagen, ControlNet; 27. оценка изображений; 28. генерация векторных изображений.

## Подробный разбор
- **procedural generation.** Генеративное искусство началось не с нейросетей: художник задаёт правила, случайность, ограничения и параметрическое пространство, а система создаёт вариации. В CV-терминах это важно как ранний пример controllable generation без обучения на данных.
- **GAN/diffusion art.** GAN-арт опирается на латентное пространство и interpolation/latent editing, но может страдать mode collapse. Diffusion-модели дают более устойчивую text-to-image генерацию, classifier-free guidance и inpainting/outpainting, ценой дорогого итеративного семплинга.
- **prompting.** Prompt — это не магическая команда, а условие генерации: объект, стиль, композиция, освещение, ограничения и negative prompt. Для diffusion важно различать text encoder, denoising U-Net/DiT и guidance scale: слишком высокий scale часто даёт пересатурированные или артефактные изображения.
- **aesthetics.** Эстетическая оценка отличается от фотореализма: изображение может быть “нереальным”, но художественно согласованным. В ML это часто моделируют через aesthetic predictors, human preference data, RLHF/DPO-подобное выравнивание и curated datasets.
- **composition.** Композиция задаёт расположение объектов, баланс масс, перспективу, фокус и читаемость сцены. Text-to-image модели хуже контролируют точные пространственные отношения, поэтому используют ControlNet, depth/pose/edge conditions, layout-to-image и редактирование по маскам.
- **vector graphics.** Векторная генерация работает с примитивами, кривыми и параметрами, а не с пикселями; она удобна для масштабируемых логотипов/плоттерной графики. Нейросетевые методы могут оптимизировать SVG-примитивы по CLIP/perceptual loss, но сложные текстуры проще получать растровыми моделями.

## Структура слайдов по извлечённому тексту
- 1. Генерация изображений в современном
- 2. Насущные вопросы
- 3. Идея до компьютеров: инструкция как
- 4. Sol LeWitt, Wall Drawing
- 5. Sol LeWitt, Variations of Incomplete Open Cubes (1974)
- 6. 1960-е: раннее компьютерное искусство
- 7. Georg Nees, the ink
- 8. Frieder Nake, the beginning Frieder Nake, cubes
- 9. 1970-е: автономная художественная
- 10. AARON, Mac OS program
- 11. Малыш AARON в действии
- 12. AARON, contemporary-museum, Berlin
- 14. 1990-е–2010-е: код как художественный язык
- 15. Casey Reas , self-portrait
- 16. Технологический сдвиг: от правил к
- 17. 2010-е: AI-art и эстетика машинного
- 18. Mario Klingemann, Memories of Passersby II
- 19. Mario Klingemann, Between Us (Temperance)

## Важные фрагменты из слайдов
- стр. 1: Генерация изображений в современном искусстве Люди, концепты, подходы….обо всём Нехаенко Паша
- стр. 2: Насущные вопросы Кто такой художник….. Какой ключевой вопрос в искусстве? • как технологии меняют понятие автора, стиля и оригинальности? • почему художник всё чаще создаёт не изображение, а систему его порождения? • Есть ли метрика оценивания? генерация изображений — не только модель, но и художественная логика.
- стр. 3: Идея до компьютеров: инструкция как произведение Sol LeWitt • В концептуальном искусстве важной становится не ручная техника, а заранее заданное правило. • Wall Drawings LeWitt выполнялись по инструкции — как по партитуре или алгоритму. • Это важный предшественник генеративного искусства: алгоритм появляется раньше компьютера. Инсталляция Sol LeWitt, Wall Drawing #260, MoMA
- стр. 5: Sol LeWitt, Variations of Incomplete Open Cubes (1974) Sol LeWitt, Variations of Incomplete Open Cubes (1974)
- стр. 6: 1960-е: раннее компьютерное искусство Vera Molnár, Georg Nees, Frieder Nake • Вера Мольнар одной из первых использует компьютер как художественный инструмент и строит алгоритмические композиции. • Раннее computer art связано с геометрией, комбинаторикой и плоттерной графикой. • Изображение здесь понимается как результат вычисления: художник задаёт систему, а машина создаёт вариации. Vera Molnár
- стр. 9: 1970-е: автономная художественная система Harold Cohen и AARON • AARON называют одной из самых ранних AI-систем для создания искусства. • Коэн задумал программу в конце 1960-х и развивал её десятилетиями как долгоживущего соавтора. • Здесь художник уже не просто пишет правила для серии работ, а создаёт систему, которая сама рисует. Выставка Harold Cohen: AARON, Whitney Museum
- стр. 14: 1990-е–2010-е: код как художественный язык Casey Reas • С начала 2000-х Casey Reas строит практику вокруг написания софта, который генерирует изображения. • Код становится не вспомогательным инструментом, а самостоятельным художественным медиумом. • На этом этапе генеративное искусство всё чаще понимается как процесс, система и вычислительное поведение, а не как один объект. Casey Reas, Linear Perspective (2015)
- стр. 16: Технологический сдвиг: от правил к данным как меняется сама логика генерации Rule-based система Procedural генерация Machine Learning GAN / diffusion / text-to-image художник постепенно переходит от создание к кураторству.

## Важные рисунки и визуальные слайды
В презентации много страниц, где основной смысл передан схемами/скриншотами. Для таких страниц сохранены крупные встроенные изображения в `_assets`; при повторении темы их стоит смотреть рядом с исходным PDF.

- стр. 1: [_assets/generative_art_ru_with_images123_compressed/page_001_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_001_01.jpg)
- стр. 4: [_assets/generative_art_ru_with_images123_compressed/page_004_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_004_01.jpg)
- стр. 4: [_assets/generative_art_ru_with_images123_compressed/page_004_02.jpg](_assets/generative_art_ru_with_images123_compressed/page_004_02.jpg)
- стр. 5: [_assets/generative_art_ru_with_images123_compressed/page_005_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_005_01.jpg)
- стр. 5: [_assets/generative_art_ru_with_images123_compressed/page_005_02.jpg](_assets/generative_art_ru_with_images123_compressed/page_005_02.jpg)
- стр. 7: [_assets/generative_art_ru_with_images123_compressed/page_007_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_007_01.jpg)
- стр. 7: [_assets/generative_art_ru_with_images123_compressed/page_007_02.jpg](_assets/generative_art_ru_with_images123_compressed/page_007_02.jpg)
- стр. 8: [_assets/generative_art_ru_with_images123_compressed/page_008_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_008_01.jpg)
- стр. 10: [_assets/generative_art_ru_with_images123_compressed/page_010_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_010_01.jpg)
- стр. 10: [_assets/generative_art_ru_with_images123_compressed/page_010_02.jpg](_assets/generative_art_ru_with_images123_compressed/page_010_02.jpg)
- стр. 11: [_assets/generative_art_ru_with_images123_compressed/page_011_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_011_01.jpg)
- стр. 12: [_assets/generative_art_ru_with_images123_compressed/page_012_01.jpg](_assets/generative_art_ru_with_images123_compressed/page_012_01.jpg)

## Связь с практикой
- Явного практического ноутбука для этой презентации не найдено; использовать как теоретический источник.

## Ключевые термины для повторения
lewitt, aaron, klingemann, anadol, художник, mario, refik, unsupervised, создаёт, художественный, casey, reas, tyler, hobbs, систему, искусства, cubes, искусство

## Замеченные пробелы и что добрать
- Страницы с малым извлекаемым текстом: 4, 7, 8, 10, 11, 12, 13, 15, 18, 21, 22, 24, ...; проверять визуально по PDF/извлечённым изображениям.
- Для GAN обязательно добрать математическую формулировку minimax/Wasserstein loss и практические симптомы mode collapse.
- Для диффузии отдельно повторить forward/posterior q, reverse p_theta и отличие DDPM/DDIM/LDM.

## Использование в итоговых ответах
- Вопрос 23: Stable Diffusion, Imagen, ControlNet
- Вопрос 27: оценка изображений
- Вопрос 28: генерация векторных изображений
