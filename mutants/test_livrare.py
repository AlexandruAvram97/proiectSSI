import pytest
from livrare_colete import Livrare  # presupunem că clasa este în fișierul livrare.py

# C111: weight < 1, distance < 10, express = True
def test_C111():
    livrare = Livrare(0.5, 5, True)
    assert livrare.calculate() == 12.5

# C112: weight < 1, distance < 10, express = False
def test_C112():
    livrare = Livrare(0.5, 5, False)
    assert livrare.calculate() == 10

# C121: 1 <= weight <= 5, 10 <= distance <= 50, express = True
def test_C121():
    livrare = Livrare(3, 30, True)
    assert livrare.calculate() == 31.25

# C122: 1 <= weight <= 5, 10 <= distance <= 50, express = False
def test_C122():
    livrare = Livrare(3, 30, False)
    assert livrare.calculate() == 25

# C131: weight > 5, distance > 50, express = True
def test_C131():
    livrare = Livrare(6, 60, True)
    assert livrare.calculate() == 81.25

# C132: weight > 5, distance > 50, express = False
def test_C132():
    livrare = Livrare(6, 60, False)
    assert livrare.calculate() == 65

# C2: weight < 0 (invalid)
def test_C2_invalid_weight():
    with pytest.raises(ValueError):
        Livrare(-1, 10).calculate()

# C3: distance < 0 (invalid)
def test_C3_invalid_distance():
    with pytest.raises(ValueError):
        Livrare(3, -5, True).calculate()

# valori de frontiera
@pytest.mark.parametrize("weight, distance, expected", [
    (0, 9.99, 10),     # frontieră greutate la 0, distanță sub 10
    (1, 10, 25),       # frontieră greutate la 1, distanță la 10
    (5, 50, 25),       # frontieră greutate la 5, distanță la 50
    (5.01, 50.01, 65), # peste limita 5 și 50
])
def test_boundary_values(weight, distance, expected):
    livrare = Livrare(weight, distance)
    assert livrare.calculate() == expected