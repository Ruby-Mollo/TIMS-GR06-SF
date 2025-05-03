import re

def validar_ruc(ruc):
    return re.match(r"^[0-9]{11}$", ruc)

def validar_email(email):
    return re.match(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

def validar_numero_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def validar_numero_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def validar_nombre(nombre):
    return re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", nombre) is not None
