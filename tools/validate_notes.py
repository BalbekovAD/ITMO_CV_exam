from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRESENTATION_DIR = ROOT / "Конспекты_презентаций"
QUESTION_DIR = ROOT / "Конспекты_вопросов"
QUESTIONS_FILE = ROOT / "Вопросы.md"


def read_questions() -> list[tuple[int, str]]:
    text = QUESTIONS_FILE.read_text(encoding="utf-8")
    questions: list[tuple[int, str]] = []
    for line in text.splitlines():
        match = re.match(r"\s*(\d+)\.\s+(.+?)\s*$", line)
        if match:
            questions.append((int(match.group(1)), match.group(2)))
    return questions


def display_question_title(title: str) -> str:
    replacements = {
        "одностадийныедетекторы": "одностадийные детекторы",
        "LlaVA": "LLaVA",
    }
    for old, new in replacements.items():
        title = title.replace(old, new)
    return title


def check_utf8(path: Path) -> list[str]:
    try:
        path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path}: not valid UTF-8: {exc}"]
    return []


def check_markdown_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if "TODO" in text or "TBD" in text:
        errors.append(f"{path}: contains TODO/TBD")
    headings = list(re.finditer(r"(?m)^##\s+.+$", text))
    for idx, heading in enumerate(headings):
        start = heading.end()
        end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
        body = text[start:end].strip()
        if not body:
            errors.append(f"{path}: empty section `{heading.group(0)}`")
    for match in re.finditer(r"\]\(([^)]+)\)", text):
        target = match.group(1)
        if "://" in target or target.startswith("#") or target.startswith("mailto:"):
            continue
        local = (path.parent / target.split("#", 1)[0]).resolve()
        if not local.exists():
            errors.append(f"{path}: broken local link -> {target}")
    return errors


def write_question_index(questions: list[tuple[int, str]]) -> None:
    files = sorted(p for p in QUESTION_DIR.glob("*.md") if p.name != "00_index.md")
    by_number: dict[int, Path] = {}
    for path in files:
        match = re.match(r"(\d{2})_", path.name)
        if match:
            by_number[int(match.group(1))] = path

    presentation_index = PRESENTATION_DIR / "00_index.md"
    lines = [
        "# Индекс конспектов вопросов",
        "",
        "Итоговые ответы к зачёту по компьютерному зрению. Каждый файл содержит краткий ответ, основные понятия, алгоритмы/формулы, сравнения, связь с практикой, типичные ошибки и источники.",
        "",
        f"Связанный индекс презентаций: [{presentation_index.name}](../Конспекты_презентаций/00_index.md).",
        "",
        "| № | Вопрос | Конспект |",
        "| --- | --- | --- |",
    ]
    for number, title in questions:
        path = by_number.get(number)
        link = f"[{path.stem}]({path.name})" if path else "нет файла"
        lines.append(f"| {number} | {display_question_title(title)} | {link} |")
    QUESTION_DIR.mkdir(parents=True, exist_ok=True)
    (QUESTION_DIR / "00_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    questions = read_questions()
    write_question_index(questions)

    errors: list[str] = []
    pdf_count = len(list((ROOT / "Презентации").glob("*.pdf")))
    presentation_notes = [p for p in PRESENTATION_DIR.glob("*.md") if p.name != "00_index.md"]
    question_notes = [p for p in QUESTION_DIR.glob("*.md") if p.name != "00_index.md"]

    if len(presentation_notes) != pdf_count:
        errors.append(f"presentation note count mismatch: {len(presentation_notes)} notes for {pdf_count} PDFs")
    if len(question_notes) != len(questions):
        errors.append(f"question note count mismatch: {len(question_notes)} notes for {len(questions)} questions")

    expected_numbers = {number for number, _ in questions}
    found_numbers = set()
    for path in question_notes:
        match = re.match(r"(\d{2})_", path.name)
        if not match:
            errors.append(f"{path}: filename must start with NN_")
            continue
        found_numbers.add(int(match.group(1)))
    if found_numbers != expected_numbers:
        errors.append(f"question numbers mismatch: missing={sorted(expected_numbers - found_numbers)}, extra={sorted(found_numbers - expected_numbers)}")

    for path in sorted(PRESENTATION_DIR.rglob("*.md")) + sorted(QUESTION_DIR.rglob("*.md")):
        errors.extend(check_utf8(path))
        errors.extend(check_markdown_file(path))

    print(f"PDFs: {pdf_count}")
    print(f"Presentation notes: {len(presentation_notes)}")
    print(f"Questions: {len(questions)}")
    print(f"Question notes: {len(question_notes)}")
    print(f"Validation errors: {len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
