from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."


def test_exam_office_lookup():
    assert "B.04" in reply("Where is the Exam Office?")


def test_medical_station_lookup():
    assert "E.01" in reply("Where is the Medical Station?")
