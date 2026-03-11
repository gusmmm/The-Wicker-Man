from __future__ import annotations

import sys
from pathlib import Path

import yaml
from pydantic import ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from schemas.scores import ClinicalScore  # noqa: E402


def extract_frontmatter(markdown_text: str) -> dict:
    if not markdown_text.startswith("---"):
        raise ValueError("Missing YAML frontmatter.")

    parts = markdown_text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter block.")

    frontmatter = parts[1].strip()
    data = yaml.safe_load(frontmatter)

    if not isinstance(data, dict):
        raise ValueError("Frontmatter must parse to a YAML mapping.")

    return data


def validate_file(file_path: Path) -> bool:
    try:
        content = file_path.read_text(encoding="utf-8")
        payload = extract_frontmatter(content)
        ClinicalScore.model_validate(payload)
        print(f"VALID: {file_path}")
        return True
    except (ValueError, ValidationError, yaml.YAMLError) as exc:
        print(f"INVALID: {file_path}")
        print(exc)
        return False


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_scores.py <markdown-file> [<markdown-file> ...]")
        return 1

    paths = [Path(arg).resolve() for arg in sys.argv[1:]]
    results = [validate_file(path) for path in paths]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())