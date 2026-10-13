import csv
from collections.abc import Callable
from pathlib import Path

from assistant.rules import reply


def same_answer(actual: str, expected: str) -> bool:
    return actual.strip().casefold() == expected.strip().casefold()


def evaluate(
    cases_path: Path,
    answer: Callable[[str], str] = reply,
) -> tuple[int, int]:
    correct = 0
    total = 0

    with cases_path.open(encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            question = row["question"]
            expected = row["expected"]
            actual = answer(question)

            total += 1
            if same_answer(actual, expected):
                correct += 1

    return correct, total


def main() -> None:
    cases_path = Path(__file__).resolve().parent / "cases.csv"
    correct, total = evaluate(cases_path)

    accuracy = correct / total * 100 if total else 0.0
    print(f"Correct: {correct}/{total}")
    print(f"Accuracy: {accuracy:.1f}%")


if __name__ == "__main__":
    main()
