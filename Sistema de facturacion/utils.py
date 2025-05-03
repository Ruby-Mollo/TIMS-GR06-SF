def calcular_igv_total(productos):
    total = sum(p['precio'] * p['cantidad'] for p in productos)
    igv = round(total-(total / 1.18),2)
    subtotal = round((total / 1.18),2)
    return total, igv, subtotal
