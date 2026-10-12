from pathlib import Path

from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."


def test_env_example_placeholders():
    env_path = Path(".env.example")
    assert env_path.exists(), ".env.example must exist in repository root"
    content = env_path.read_text(encoding="utf-8")
    assert "LLM_API_KEY=changeme" in content
    assert "LLM_PROVIDER=" in content
    assert "DB_URL=" in content
