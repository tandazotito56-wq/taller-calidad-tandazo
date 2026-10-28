def transferir(cuentas, origen, destino, monto):
    if origen == destino:
        raise ValueError("Cuentas iguales")
    if monto <= 0:
        raise ValueError("Monto invalido")
    if origen not in cuentas or destino not in cuentas:
        raise ValueError("Cuenta inexistente")
    if cuentas[origen] < monto:
        raise ValueError("Saldo insuficiente")
    cuentas[origen] -= monto
    cuentas[destino] += monto
    return True
