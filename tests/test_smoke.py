from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."

def test_help():
    response = reply("help")
    assert "Office lookup" in response
    assert "Greeting" in response
    assert "Exit" in response
    assert "help" in response.lower()
