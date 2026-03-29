from app import additionner, soustraire

def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(0, 0) == 0
    assert additionner(-1, 1) == 0

def test_soustraire():
    assert soustraire(10, 4) == 6
    assert soustraire(0, 0) == 0
    assert soustraire(5, 10) == -5

print("Tous les tests passent !")
