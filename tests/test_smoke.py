from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")
    assert "E.005" in reply("Where is the IT Helpdesk office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."


def test_partial_office_lookup():
    assert "I.101" in reply("where is training")
    assert "I.101" in reply("training")


def test_ambiguous_office_lookup():
    assert "don't know" in reply("where is training and library")
