from Bonjour import saluer

def test_saluer_ahmed():
    assert saluer("Ahmed") == "Bonjour Ahmed"

def test_saluer_vide():
    assert saluer("") == "Bonjour "