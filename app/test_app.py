from app import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(1000, 2000) == 3000
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma('a', 2) == 3 # Teste com falha.
