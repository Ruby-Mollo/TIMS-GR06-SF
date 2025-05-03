def calcular_igv_total(productos):
    subtotal = sum(p['precio'] * p['cantidad'] for p in productos)
    igv = subtotal * 0.18
    total = subtotal + igv
    return total, igv, subtotal