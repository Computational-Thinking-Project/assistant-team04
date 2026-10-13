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


def test_exam_office_lookup():
    assert "B.04" in reply("Where is the Exam Office?")


def test_medical_station_lookup():
    assert "E.01" in reply("Where is the Medical Station?")
    
    
def test_help():
    response = reply("help")
    assert "Office lookup" in response
    assert "Greeting" in response
    assert "Exit" in response
    assert "help" in response.lower()


def test_partial_office_lookup():
    assert "I.101" in reply("where is training")
    assert "I.101" in reply("training")


def test_ambiguous_office_lookup():
    assert "don't know" in reply("where is training and library")
