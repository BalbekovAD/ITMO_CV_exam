from __future__ import annotations

import json
import re
import textwrap
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "Презентации"
NB_DIR = ROOT / "jupiter notebooks"
OUT_DIR = ROOT / "Конспекты_презентаций"
ASSET_DIR = OUT_DIR / "_assets"


DECK_META: dict[str, dict[str, object]] = {
    "01_cnn_classification_detection.pdf": {
        "title": "CNN, классификация и детекция объектов",
        "questions": [1, 3, 4, 5, 6],
        "notebooks": [
            "01_1. PyTorch basics, CNNs.ipynb",
            "01_2. VGG, Transfer Learning.ipynb",
            "01_3. CNNs, Detection, Yolov1.ipynb",
            "02_01_(CNNs,_Detection,_Yolov1).ipynb",
        ],
        "summary": "Базовая лекция курса: постановки задач компьютерного зрения, свёрточные сети, классификация, перенос обучения и объектная детекция.",
        "concepts": [
            "изображение как тензор и признаки низкого/высокого уровня",
            "свёртка, padding, stride, receptive field, pooling, upsampling",
            "классификация и transfer learning",
            "VGG, ResNet, Inception как разные способы строить глубокие CNN",
            "object detection, bounding boxes, IoU, NMS, anchor-based и anchor-free идеи",
            "одностадийные и двустадийные детекторы",
        ],
    },
    "02_segmentation_video.pdf": {
        "title": "Сегментация, видео, OCR, depth, face recognition",
        "questions": [7, 8, 9, 10, 11, 19],
        "notebooks": [
            "02_02_Segmentation,_Tracking.ipynb",
            "02_03_how_to_segment_anything_with_sam.ipynb",
            "02_04_SegmentAnything_and_pytorch.ipynb",
            "02_05_Face_Recognition,_Depth_Anything.ipynb",
        ],
        "summary": "Лекция объединяет dense prediction: сегментацию, видеоаналитику, трекинг, OCR, карты глубины, распознавание лиц и скелетные модели.",
        "concepts": [
            "семантическая, instance и panoptic segmentation",
            "FCN, U-Net, DeepLab, encoder-decoder и skip connections",
            "обработка видеопотока, temporal consistency, optical flow, tracking-by-detection",
            "OCR: детекция текста, распознавание последовательности, CTC/attention",
            "монокулярная глубина и вырезание объектов по маске/глубине",
            "face recognition: детекция, выравнивание, embedding, metric learning",
        ],
    },
    "03_generation_VAE_GAN.pdf": {
        "title": "Автокодировщики, VAE, VQ-VAE, GAN и StyleGAN",
        "questions": [12, 13, 14, 15, 16, 20],
        "notebooks": ["03_01_Autoencoders,_DCGAN.ipynb", "03_02_GANs.ipynb"],
        "summary": "Введение в генеративные модели: автоэнкодеры, вариационные автоэнкодеры, дискретные латенты VQ-VAE, GAN и условные/image-to-image модели.",
        "concepts": [
            "encoder-decoder, bottleneck и reconstruction loss",
            "VAE: ELBO, reparameterization trick, KL-регуляризация",
            "VQ-VAE: codebook, vector quantization, commitment loss",
            "GAN: generator, discriminator, minimax-игра и adversarial loss",
            "DCGAN, conditional GAN, Pix2Pix, CycleGAN, SPADE/GauGAN",
            "StyleGAN: mapping network, styles, noise injection, progressive growth, AdaIN/modulated conv",
        ],
    },
    "04_autoregr_diff.pdf": {
        "title": "Attention, ViT, авторегрессия и диффузия",
        "questions": [17, 18, 22],
        "notebooks": ["04_01_Attn,_ViT.ipynb", "04_02_DDPM_и_DDIM.ipynb"],
        "summary": "Лекция связывает self-attention и Vision Transformer с генеративными моделями: авторегрессионной генерацией, VQ-GAN и диффузионными моделями.",
        "concepts": [
            "scaled dot-product attention, multi-head attention, positional encoding",
            "ViT: patch embedding, class token, transformer encoder",
            "autoregressive factorization p(x)=prod p(x_i|x_<i)",
            "VQ-GAN как компрессор изображения в дискретные токены",
            "DDPM: forward noising, reverse denoising, noise prediction",
            "DDIM, ускоренное семплирование и связь с score matching",
        ],
    },
    "05_text2img.pdf": {
        "title": "Text-to-image: CLIP, Stable Diffusion, Imagen, ControlNet",
        "questions": [20, 23, 24, 27, 30, 31],
        "notebooks": [],
        "summary": "Условная генерация изображений по тексту и дополнительным условиям: CLIP-представления, latent diffusion, guidance, ControlNet и оценка соответствия тексту.",
        "concepts": [
            "joint image-text embeddings и contrastive learning",
            "classifier/classifier-free guidance",
            "Latent Diffusion Model и Stable Diffusion pipeline",
            "Imagen и каскадные diffusion-суперрезолверы",
            "ControlNet, layout/inpainting и структурные условия",
            "оценка text-image alignment, aesthetic score и reward models",
        ],
    },
    "06_IQA_depth.pdf": {
        "title": "IQA, depth estimation, 3D и NeRF",
        "questions": [9, 21, 26, 27],
        "notebooks": [
            "CV. Practice 5.1. IQA.ipynb",
            "CV. Practice 5.2. DepthAnythingV2.ipynb",
            "CV. Practice 5.3. 3d_formats_intro_colab.ipynb",
            "CV. Practice 5.4. fit_textured_mesh_ru.ipynb",
            "CV. Practice 5.5. fit_simple_neural_radiance_field_ru.ipynb",
        ],
        "summary": "Качество изображений, карты глубины, 3D-представления и neural rendering: от метрик IQA до NeRF и генерации 3D.",
        "concepts": [
            "full-reference и no-reference image quality assessment",
            "PSNR, SSIM, LPIPS, FID, CLIPScore, ImageReward",
            "depth estimation, disparity, camera geometry",
            "3D formats: point cloud, mesh, voxel, implicit field",
            "NeRF: radiance field, volume rendering, positional encoding",
            "3D generation and reconstruction constraints",
        ],
    },
    "07_img2img_NST.pdf": {
        "title": "Image-to-image, NST, super-resolution, harmonization",
        "questions": [15, 27, 28, 29],
        "notebooks": [
            "CV. Practice #6.1. NST.ipynb",
            "CV. Practice #6.2. SuperResolution_RealESRGAN,_SwinIR,_HYPIR.ipynb",
        ],
        "summary": "Методы преобразования изображений: neural style transfer, super-resolution, image harmonization, vector graphics generation и image-to-image GAN/diffusion подходы.",
        "concepts": [
            "content/style loss и Gram matrix в NST",
            "paired/unpaired image-to-image translation",
            "super-resolution, perceptual loss, adversarial loss",
            "image harmonization: согласование вставленного объекта с фоном",
            "vector image generation и raster-to-vector постановки",
            "метрики композиции, эстетики и соответствия условию",
        ],
    },
    "3d-generation.pdf": {
        "title": "Генерация 3D объектов",
        "questions": [21, 26],
        "notebooks": ["CV. Practice 5.3. 3d_formats_intro_colab.ipynb", "CV. Practice 5.4. fit_textured_mesh_ru.ipynb"],
        "summary": "Доклад о представлениях 3D-объектов и генерации формы/текстуры: meshes, point clouds, implicit fields, NeRF-подходы.",
        "concepts": ["point cloud", "mesh", "voxel grid", "implicit representation", "text-to-3D", "multi-view consistency"],
    },
    "SSL и CL.pdf": {
        "title": "Self-supervised learning и contrastive learning",
        "questions": [30, 31],
        "notebooks": [],
        "summary": "Самообучение и контрастивное обучение как база современных vision-language моделей: инвариантности, augmentations, positive/negative pairs, CLIP-подобные цели.",
        "concepts": ["pretext task", "contrastive loss", "InfoNCE", "SimCLR/MoCo/BYOL", "CLIP", "zero-shot transfer"],
    },
    "adversarial exmp.pptx.pdf": {
        "title": "Adversarial examples",
        "questions": [1, 3, 4],
        "notebooks": [],
        "summary": "Доклад о состязательных примерах: малые возмущения изображения, которые меняют ответ нейросети, и методы защиты.",
        "concepts": ["FGSM", "PGD", "targeted/untargeted attacks", "robustness", "adversarial training", "transferability"],
    },
    "cv_2026_fintech_v2.pdf": {
        "title": "Computer vision в финтехе",
        "questions": [1, 7, 19],
        "notebooks": [],
        "summary": "Прикладной обзор CV-задач в финтехе: OCR документов, KYC, face recognition, антифрод, document understanding.",
        "concepts": ["document OCR", "face verification", "liveness", "fraud detection", "document layout analysis", "privacy"],
    },
    "generative_art_ru_with_images123_compressed.pdf": {
        "title": "Генеративное искусство",
        "questions": [23, 27, 28],
        "notebooks": [],
        "summary": "Обзор генеративного искусства: процедурные и нейросетевые методы, эстетика, композиция, стилизация, векторная/растровая генерация.",
        "concepts": ["procedural generation", "GAN/diffusion art", "prompting", "aesthetics", "composition", "vector graphics"],
    },
    "image harmonization.pdf": {
        "title": "Image harmonization",
        "questions": [15, 29],
        "notebooks": [],
        "summary": "Методы гармонизации изображений: как сделать вставленный объект визуально согласованным с фоном по освещению, цвету, контрасту и стилю.",
        "concepts": ["foreground/background mask", "color transfer", "illumination matching", "domain adaptation", "composite realism", "harmonization loss"],
    },
    "img_report_VLM_Козьма.pdf": {
        "title": "Vision Language Models",
        "questions": [30, 31],
        "notebooks": [],
        "summary": "Доклад о VLM: соединение визуальных энкодеров с языковыми моделями, instruction tuning, image captioning, VQA и LLaVA-подобные архитектуры.",
        "concepts": ["vision encoder", "LLM connector", "image-text alignment", "captioning", "VQA", "LLaVA"],
    },
    "Викторов_Методы_улучшения_сходимости_GAN.pdf": {
        "title": "Методы улучшения сходимости GAN",
        "questions": [14, 16],
        "notebooks": ["03_02_GANs.ipynb"],
        "summary": "Доклад о проблемах обучения GAN и практиках стабилизации: баланс G/D, mode collapse, Wasserstein loss, gradient penalty, spectral normalization.",
        "concepts": ["mode collapse", "vanishing gradients", "WGAN", "gradient penalty", "spectral normalization", "TTUR"],
    },
    "Генерация видео.pdf": {
        "title": "Генерация видео",
        "questions": [25],
        "notebooks": [],
        "summary": "Доклад о генерации видео: временная согласованность, text-to-video, diffusion/video transformers, motion representations и метрики качества.",
        "concepts": ["temporal consistency", "frame interpolation", "video diffusion", "motion field", "text-to-video", "FVD"],
    },
    "Детекция и генерация дипфейков (3).pdf": {
        "title": "Детекция и генерация дипфейков",
        "questions": [1, 14, 19, 25],
        "notebooks": [],
        "summary": "Доклад о deepfake-пайплайнах, face swapping/reenactment и методах обнаружения синтетических лиц и видео.",
        "concepts": ["face swap", "reenactment", "GAN/diffusion deepfakes", "frequency artifacts", "temporal artifacts", "liveness/deepfake detection"],
    },
    "Диффузионные модели.pdf": {
        "title": "Диффузионные модели",
        "questions": [22, 23],
        "notebooks": ["04_02_DDPM_и_DDIM.ipynb"],
        "summary": "Доклад с фокусом на математике диффузионных моделей: зашумление, обратный процесс, DDPM/DDIM, условная генерация.",
        "concepts": ["forward diffusion", "reverse denoising", "noise schedule", "epsilon prediction", "DDPM", "DDIM"],
    },
    "Доклад про автономный транспорт.pdf": {
        "title": "Computer vision в автономном транспорте",
        "questions": [1, 5, 8, 9, 10],
        "notebooks": [],
        "summary": "Прикладной доклад о perception stack автономного транспорта: камеры, детекция, сегментация, трекинг, глубина, sensor fusion.",
        "concepts": ["object detection", "lane segmentation", "tracking", "depth", "sensor fusion", "real-time constraints"],
    },
    "Методы распознования текста.pdf": {
        "title": "Методы распознавания текста",
        "questions": [7],
        "notebooks": [],
        "summary": "Доклад по OCR: предобработка, детекция текстовых областей, распознавание символов/строк, sequence modeling и document understanding.",
        "concepts": ["text detection", "CRNN", "CTC", "attention OCR", "Transformer OCR", "layout analysis"],
    },
    "Скелетные_модели.pdf": {
        "title": "Скелетные модели",
        "questions": [11],
        "notebooks": [],
        "summary": "Доклад о pose estimation и скелетных моделях: ключевые точки тела, heatmaps, top-down/bottom-up pipeline, 2D/3D pose.",
        "concepts": ["keypoints", "heatmaps", "OpenPose", "top-down pose", "bottom-up pose", "3D pose estimation"],
    },
    "Соотвествие изображений и текста.pdf": {
        "title": "Соответствие изображений и текста",
        "questions": [23, 27, 30, 31],
        "notebooks": [],
        "summary": "Доклад о согласовании изображения и текста: CLIPScore, retrieval, captioning, VQA, VLM и метрики semantic alignment.",
        "concepts": ["image-text retrieval", "CLIPScore", "captioning", "VQA", "alignment", "multimodal embedding"],
    },
    "Фотограмметрия.pdf": {
        "title": "Фотограмметрия",
        "questions": [2, 9, 21, 26],
        "notebooks": [],
        "summary": "Визуальная презентация по фотограмметрии: восстановление 3D-сцены по множеству изображений, matching, camera poses, SfM/MVS.",
        "concepts": ["feature matching", "homography", "epipolar geometry", "structure from motion", "multi-view stereo", "bundle adjustment"],
    },
    "нейросетевые методы рендеринга (2).pdf": {
        "title": "Нейросетевые методы рендеринга",
        "questions": [21, 26],
        "notebooks": ["CV. Practice 5.5. fit_simple_neural_radiance_field_ru.ipynb"],
        "summary": "Доклад о neural rendering: NeRF, radiance fields, volume rendering, novel view synthesis и ограничения таких моделей.",
        "concepts": ["neural rendering", "NeRF", "ray marching", "volume rendering", "novel view synthesis", "view consistency"],
    },
}


QUESTION_TITLES: dict[int, str] = {
    1: "задачи CV и классические методы",
    2: "ключевые точки, дескрипторы, гомография",
    3: "CNN, свёртки, pooling, upsampling",
    4: "классификация, VGG, ResNet, Inception, transfer learning",
    5: "одностадийная детекция",
    6: "двустадийная детекция",
    7: "OCR",
    8: "семантическая сегментация",
    9: "карта глубины и вырезание объектов",
    10: "обработка видеопотока",
    11: "скелетные модели",
    12: "AE, VAE и метрики генерации",
    13: "VQ-VAE и VQ-VAE 2",
    14: "GAN, проблемы и стабилизация",
    15: "image-to-image, Pix2Pix, SPADE, GauGAN, OASIS",
    16: "StyleGAN",
    17: "attention и Vision Transformer",
    18: "авторегрессия и VQ-GAN",
    19: "распознавание лиц",
    20: "условная генерация, CLIP и StyleCLIP",
    21: "NeRF",
    22: "диффузионные модели, DDPM, LDM",
    23: "Stable Diffusion, Imagen, ControlNet",
    24: "layout generation и inpainting",
    25: "генерация видео",
    26: "генерация 3D объектов",
    27: "оценка изображений",
    28: "генерация векторных изображений",
    29: "гармонизация изображений",
    30: "CLIP и модификации",
    31: "Vision Language Models",
}


RUS_STOPWORDS = {
    "что",
    "как",
    "для",
    "или",
    "это",
    "при",
    "над",
    "под",
    "все",
    "так",
    "его",
    "еще",
    "уже",
    "где",
    "the",
    "and",
    "with",
    "from",
    "this",
    "that",
}


@dataclass
class PageInfo:
    number: int
    text: str
    image_count: int


def slugify(name: str) -> str:
    stem = Path(name).stem.lower()
    stem = stem.replace("ё", "е")
    stem = re.sub(r"[^\wа-яА-Я]+", "_", stem, flags=re.IGNORECASE)
    stem = re.sub(r"_+", "_", stem).strip("_")
    return stem or "deck"


def safe_filename(name: str) -> str:
    return f"{slugify(name)}.md"


def extract_pages(pdf_path: Path) -> list[PageInfo]:
    reader = PdfReader(str(pdf_path))
    pages: list[PageInfo] = []
    for idx, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        try:
            image_count = len(list(page.images))
        except Exception:
            image_count = 0
        pages.append(PageInfo(idx, normalize_text(text), image_count))
    return pages


def normalize_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_notebook_headings() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for path in sorted(NB_DIR.glob("*.ipynb")):
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        headings: list[str] = []
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            source = "".join(cell.get("source", []))
            for line in source.splitlines():
                if line.lstrip().startswith("#"):
                    clean = line.strip().lstrip("#").strip()
                    if clean and clean not in headings:
                        headings.append(clean)
                    break
            if len(headings) >= 8:
                break
        result[path.name] = headings
    return result


def extract_large_images(pdf_path: Path, pages: list[PageInfo], max_images: int = 12) -> list[tuple[int, str]]:
    reader = PdfReader(str(pdf_path))
    slug = slugify(pdf_path.stem)
    out_dir = ASSET_DIR / slug
    saved: list[tuple[int, str]] = []
    candidates = [p.number for p in pages if len(p.text) < 120 or p.image_count >= 2]
    for page_no in candidates:
        if len(saved) >= max_images:
            break
        page = reader.pages[page_no - 1]
        for image_idx, image in enumerate(page.images, start=1):
            data = image.data
            if len(data) < 25_000:
                continue
            suffix = Path(image.name).suffix.lower() or ".jpg"
            if suffix not in {".jpg", ".jpeg", ".png", ".jp2"}:
                suffix = ".jpg"
            out_dir.mkdir(parents=True, exist_ok=True)
            name = f"page_{page_no:03d}_{image_idx:02d}{suffix}"
            out_path = out_dir / name
            if not out_path.exists():
                out_path.write_bytes(data)
            rel = out_path.relative_to(OUT_DIR).as_posix()
            saved.append((page_no, rel))
            if len(saved) >= max_images:
                break
    return saved


def top_terms(text: str, n: int = 18) -> list[str]:
    words = re.findall(r"[A-Za-zА-Яа-яЁё][A-Za-zА-Яа-яЁё0-9\-]{3,}", text.lower())
    counts = Counter(w for w in words if w not in RUS_STOPWORDS and not w.isdigit())
    return [w for w, _ in counts.most_common(n)]


def slide_outline(pages: list[PageInfo], limit: int = 18) -> list[str]:
    outline: list[str] = []
    for page in pages:
        if not page.text:
            continue
        lines = [l.strip(" •\t") for l in page.text.splitlines() if l.strip()]
        candidate = ""
        for line in lines[:6]:
            if 5 <= len(line) <= 90 and not re.fullmatch(r"\d+", line):
                candidate = line
                break
        if candidate and candidate not in outline:
            outline.append(f"{page.number}. {candidate}")
        if len(outline) >= limit:
            break
    return outline


def compact_excerpt(pages: list[PageInfo], limit_pages: int = 8) -> list[str]:
    excerpts: list[str] = []
    for page in pages:
        if len(page.text) < 80:
            continue
        text = re.sub(r"\s+", " ", page.text)
        excerpts.append(f"стр. {page.number}: {text[:420].strip()}")
        if len(excerpts) >= limit_pages:
            break
    return excerpts


def question_links(numbers: list[int]) -> str:
    parts = []
    for number in numbers:
        title = QUESTION_TITLES.get(number, "")
        parts.append(f"{number}. {title}")
    return "; ".join(parts)


def render_deck_note(pdf_path: Path, nb_headings: dict[str, list[str]]) -> str:
    meta = DECK_META.get(pdf_path.name, {})
    title = str(meta.get("title") or pdf_path.stem)
    summary = str(meta.get("summary") or "Конспект презентации по теме компьютерного зрения.")
    concepts = list(meta.get("concepts") or [])
    questions = list(meta.get("questions") or [])
    notebooks = list(meta.get("notebooks") or [])

    pages = extract_pages(pdf_path)
    total_text = sum(len(p.text) for p in pages)
    low_text_pages = [p.number for p in pages if len(p.text) < 80]
    image_count = sum(p.image_count for p in pages)
    all_text = "\n".join(p.text for p in pages)
    terms = top_terms(all_text)
    outline = slide_outline(pages)
    excerpts = compact_excerpt(pages)
    saved_images = extract_large_images(pdf_path, pages) if (len(low_text_pages) >= 5 or image_count >= 20) else []

    visual_note = (
        "В презентации много страниц, где основной смысл передан схемами/скриншотами. "
        "Для таких страниц сохранены крупные встроенные изображения в `_assets`; при повторении темы их стоит смотреть рядом с исходным PDF."
        if saved_images or len(low_text_pages) >= 5
        else "Большая часть содержания доступна как извлекаемый текст; изображения в основном иллюстрируют уже описанные идеи."
    )

    nb_lines: list[str] = []
    for notebook in notebooks:
        headings = nb_headings.get(notebook, [])
        suffix = f": {', '.join(headings[:5])}" if headings else ""
        nb_lines.append(f"- `{notebook}`{suffix}")
    if not nb_lines:
        nb_lines.append("- Явного практического ноутбука для этой презентации не найдено; использовать как теоретический источник.")

    asset_lines = [
        f"- стр. {page_no}: [{rel}]({rel})" for page_no, rel in saved_images
    ] or ["- Крупные изображения отдельно не извлекались."]

    md = f"""# {title}

## Источник
- PDF: `{pdf_path.name}`
- Страниц: {len(pages)}
- Извлечено текста: примерно {total_text} символов
- Страниц с малым количеством текста: {len(low_text_pages)}
- Встроенных изображений: {image_count}

## Краткое содержание
{summary}

Связанные экзаменационные вопросы: {question_links(questions) if questions else "прямые связи не размечены"}.

## Подробный разбор
"""

    for concept in concepts:
        md += f"- **{concept}.** {concept_explanation(concept)}\n"

    md += "\n## Структура слайдов по извлечённому тексту\n"
    for item in outline:
        md += f"- {item}\n"
    if not outline:
        md += "- Текстовая структура почти не извлекается; ориентироваться по визуальным слайдам и сохранённым изображениям.\n"

    md += "\n## Важные фрагменты из слайдов\n"
    for excerpt in excerpts:
        md += f"- {excerpt}\n"
    if not excerpts:
        md += "- В PDF почти нет извлекаемого текста; тема восстановлена по названию, изображениям и связям с вопросами.\n"

    md += f"""
## Важные рисунки и визуальные слайды
{visual_note}

"""
    md += "\n".join(asset_lines)
    md += "\n\n## Связь с практикой\n"
    md += "\n".join(nb_lines)
    md += "\n\n## Ключевые термины для повторения\n"
    md += ", ".join(terms[:18]) if terms else "Ключевые термины извлекаются из темы презентации: " + ", ".join(concepts)
    md += "\n\n## Замеченные пробелы и что добрать\n"
    md += gap_notes(pdf_path.name, concepts, low_text_pages)
    md += "\n\n## Использование в итоговых ответах\n"
    if questions:
        for q in questions:
            md += f"- Вопрос {q}: {QUESTION_TITLES.get(q, '')}\n"
    else:
        md += "- Использовать как дополнительный материал при ответах по близким темам.\n"
    return md


def concept_explanation(concept: str) -> str:
    key = concept.lower()
    if "свёрт" in key or "convolution" in key:
        return "Нужно уметь объяснить локальные фильтры, разделение параметров, влияние stride/padding/dilation и рост receptive field."
    if "gan" in key:
        return "Важно понимать состязательную постановку, баланс генератора и дискриминатора, mode collapse и способы стабилизации."
    if "diff" in key or "ddpm" in key or "denois" in key:
        return "Ключевая идея: обучить обратный процесс удаления шума, обычно через предсказание добавленного шума или score."
    if "clip" in key or "contrastive" in key:
        return "Модель учится сближать изображения и соответствующие тексты в общем embedding-пространстве и разводить несоответствующие пары."
    if "nerf" in key or "render" in key:
        return "Сцена задаётся непрерывной функцией плотности и цвета; изображение получается интегрированием вдоль лучей камеры."
    if "depth" in key or "глуб" in key:
        return "Глубина описывает расстояние до сцены; монокулярная оценка неоднозначна и часто требует learned priors."
    if "segmentation" in key or "сегмента" in key:
        return "Задача dense prediction: каждому пикселю назначается класс, объект или panoptic-метка."
    if "ocr" in key or "text" in key:
        return "Пайплайн обычно разделяет детекцию текстовых областей и распознавание последовательности символов."
    if "attention" in key or "vit" in key:
        return "Self-attention строит контекстные признаки через сходство запросов и ключей; ViT применяет это к патчам изображения."
    if "stylegan" in key:
        return "Ключевы mapping network, стиль на разных масштабах, шумовые карты и контроль латентного пространства."
    if "homography" in key or "matching" in key or "feature" in key:
        return "Локальные признаки сопоставляют между видами, после чего геометрическая модель оценивается устойчиво, например через RANSAC."
    return "Термин входит в ядро темы; для экзамена нужно знать постановку задачи, входы/выходы, типовые архитектуры и ограничения."


def gap_notes(name: str, concepts: list[str], low_text_pages: list[int]) -> str:
    notes: list[str] = []
    if low_text_pages:
        preview = ", ".join(map(str, low_text_pages[:12]))
        if len(low_text_pages) > 12:
            preview += ", ..."
        notes.append(f"- Страницы с малым извлекаемым текстом: {preview}; проверять визуально по PDF/извлечённым изображениям.")
    if any("gan" in c.lower() for c in concepts):
        notes.append("- Для GAN обязательно добрать математическую формулировку minimax/Wasserstein loss и практические симптомы mode collapse.")
    if any("diff" in c.lower() or "ddpm" in c.lower() for c in concepts):
        notes.append("- Для диффузии отдельно повторить forward/posterior q, reverse p_theta и отличие DDPM/DDIM/LDM.")
    if any("ocr" in c.lower() or "text" in c.lower() for c in concepts):
        notes.append("- Для OCR полезно разделять document layout, text detection и sequence recognition.")
    if "Фотограмметрия" in name:
        notes.append("- Для фотограмметрии добрать строгие связи feature matching, epipolar geometry, SfM, MVS и bundle adjustment.")
    if not notes:
        notes.append("- Явных пробелов не найдено; использовать как опорную презентацию для связанных вопросов.")
    return "\n".join(notes)


def write_index(deck_files: list[tuple[Path, str, list[int]]]) -> None:
    lines = [
        "# Индекс конспектов презентаций",
        "",
        "Каждый файл содержит краткое содержание, подробный разбор, важные термины, связи с вопросами и практическими ноутбуками.",
        "",
        "| PDF | Конспект | Вопросы |",
        "| --- | --- | --- |",
    ]
    for pdf_path, md_name, questions in deck_files:
        qs = ", ".join(map(str, questions)) if questions else "-"
        lines.append(f"| `{pdf_path.name}` | [{Path(md_name).stem}]({md_name}) | {qs} |")
    lines += [
        "",
        "## Низкотекстовые/визуальные презентации",
        "",
        "Особенно внимательно сверять с исходным PDF и `_assets`: `Фотограмметрия.pdf`, `Детекция и генерация дипфейков (3).pdf`, `img_report_VLM_Козьма.pdf`, `SSL и CL.pdf`, `generative_art_ru_with_images123_compressed.pdf`, `image harmonization.pdf`.",
    ]
    (OUT_DIR / "00_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    nb_headings = extract_notebook_headings()
    deck_files: list[tuple[Path, str, list[int]]] = []
    for pdf_path in sorted(PDF_DIR.glob("*.pdf"), key=lambda p: p.name.casefold()):
        md_name = safe_filename(pdf_path.name)
        content = render_deck_note(pdf_path, nb_headings)
        (OUT_DIR / md_name).write_text(content, encoding="utf-8")
        questions = list(DECK_META.get(pdf_path.name, {}).get("questions", []))
        deck_files.append((pdf_path, md_name, questions))
    write_index(deck_files)


if __name__ == "__main__":
    main()
