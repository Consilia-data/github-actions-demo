from calculator import addition

def test_addition():
    result = addition(2, 3)
    print("Résultat de l'addition :", result)
    assert result == 5