# test_calculadora.py
from calculadora import sumar


def test_dos_numeros_separados_por_coma_devuelven_suma():
    assert sumar("1,2") == 3


