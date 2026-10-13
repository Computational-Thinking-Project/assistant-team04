from pathlib import Path

from eval.run import evaluate


def test_correct_case(tmp_path: Path) -> None:
    cases = tmp_path / "cases.csv"
    cases.write_text(
        "question,expected,category\nq,yes,normal\n",
        encoding="utf-8",
    )

    assert evaluate(cases, answer=lambda _: " YES ") == (1, 1)


def test_incorrect_case(tmp_path: Path) -> None:
    cases = tmp_path / "cases.csv"
    cases.write_text(
        "question,expected,category\nq,yes,normal\n",
        encoding="utf-8",
    )

    assert evaluate(cases, answer=lambda _: "no") == (0, 1)


def test_empty_case_set(tmp_path: Path) -> None:
    cases = tmp_path / "cases.csv"
    cases.write_text("question,expected,category\n", encoding="utf-8")

    assert evaluate(cases, answer=lambda _: "unused") == (0, 0)
