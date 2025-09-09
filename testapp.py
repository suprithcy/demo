import app

def test_add_positive():
    assert app.add(3, 5) == 8

def test_add_negative():
    assert app.add(-2, -4) == -6

def test_add_mixed():
    assert app.add(-2, 5) == 3
