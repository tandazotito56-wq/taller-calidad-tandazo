import pytest
from banco import transferir

def test_transferencia_valida():
    cuentas = {"A": 10000, "B": 5000}
    assert transferir(cuentas, "A", "B", 3000) is True
    assert cuentas == {"A": 7000, "B": 8000}

def test_saldo_insuficiente():
    cuentas = {"A": 10000, "B": 5000}
    with pytest.raises(ValueError):
        transferir(cuentas, "A", "B", 12000)
    assert cuentas == {"A": 10000, "B": 5000}

@pytest.mark.parametrize("monto", [0, -100])
def test_monto_invalido(monto):
    cuentas = {"A": 10000, "B": 5000}
    with pytest.raises(ValueError):
        transferir(cuentas, "A", "B", monto)
    assert cuentas == {"A": 10000, "B": 5000}

@pytest.mark.parametrize("origen,destino", [("X", "B"), ("A", "X")])
def test_cuenta_inexistente(origen, destino):
    cuentas = {"A": 10000, "B": 5000}
    with pytest.raises(ValueError):
        transferir(cuentas, origen, destino, 100)
    assert cuentas == {"A": 10000, "B": 5000}

def test_misma_cuenta():
    cuentas = {"A": 10000, "B": 5000}
    with pytest.raises(ValueError):
        transferir(cuentas, "A", "A", 100)
    assert cuentas == {"A": 10000, "B": 5000}