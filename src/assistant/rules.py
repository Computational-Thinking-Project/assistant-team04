"""A tiny rule-based responder. No AI yet — that comes in Week 4."""

from __future__ import annotations

import csv
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

GREETINGS = {"hi", "hello", "hey", "xin chao", "chao"}
COMMON_WORDS = {"office"}

HELP_MESSAGE = (
    "I can help you with:\n"
    "- Greeting: Say hello\n"
    "- Office lookup: Ask for office location or opening hours\n"
    "- Help: Type 'help' to see supported commands \n"
    "- Exit: Type 'quit' or 'exit' to leave"
)


def load_offices(path: Path = DATA_DIR / "offices.csv") -> dict[str, dict[str, str]]:
    """Return {office_name_lower: row} from the offices CSV."""
    with path.open(encoding="utf-8", newline="") as f:
        return {row["name"].lower(): row for row in csv.DictReader(f)}


def reply(message: str, offices: dict[str, dict[str, str]] | None = None) -> str:
    """Answer a message with simple rules."""
    text = message.strip().lower().rstrip("?!.")
    if not text:
        return "Please type a question."
    if text in GREETINGS:
        return "Hello! Ask me where an office is, or when it opens."
    if text == "help":
        return HELP_MESSAGE
    offices = offices if offices is not None else load_offices()

    query_words = set(re.findall(r"\b\w+\b", text))
    matches: list[dict[str, str]] = []
    for name, row in offices.items():
        office_words = set(re.findall(r"\b\w+\b", name)) - COMMON_WORDS
        if name in text or (office_words and office_words & query_words):
            matches.append(row)

    if len(matches) == 1:
        row = matches[0]
        return f"{row['name']}: room {row['room']}, open {row['hours']}."

    return "I don't know that yet. Try asking about an office, e.g. 'training office'."
