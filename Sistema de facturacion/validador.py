import re

def validar_ruc(ruc):
    """
    Valida un RUC peruano según normas SUNAT:
    - Longitud exacta de 11 dígitos
    - Empieza con 10 (personas naturales) o 20 (personas juridicas)
    - No es una secuencia repetida
    """
    if not re.match(r"^[0-9]{11}$", ruc):
        return False
    
    # Validar primeros dígitos (10 o 20)
    primeros_digitos = ruc[:2]
    if primeros_digitos not in ["10", "20"]:
        return False
    
    # Evitar secuencias repetidas (ej. 11111111111)
    if all(c == ruc[0] for c in ruc):
        return False
    
    return True

def validar_email(email):
    """
    Valida estructura general de correo y prohíbe duplicación de caracteres
    consecutivos en el dominio (ej: gmaill.com, coom, ..).
    """
    # Verificar estructura básica con regex (no valida duplicados aún)
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        return False

    # Separar parte local y dominio
    try:
        local, domain = email.split('@')
    except ValueError:
        return False  # más de un @

    # Revisar duplicación de caracteres consecutivos en dominio
    for i in range(1, len(domain)):
        if domain[i] == domain[i - 1]:
            return False  # hay duplicación de letra o punto

    return True


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

def validar_nombre_empresa(nombre):
    """
    Valida nombres de empresas/productos:
    - Mínimo 3 caracteres, máximo 100
    - Permite letras (incluido ñ/Ñ y tildes), números, espacios y guiones
    - No permite caracteres especiales ni secuencias inválidas
    """
    if not 3 <= len(nombre) <= 100:
        return False
    
    return re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\-\.]+$", nombre) is not None

def validar_nombre_producto(nombre):
    """
    Valida nombres de productos:
    - Mínimo 3 caracteres, máximo 100
    - Permite letras, números, espacios y algunos símbolos comunes
    - No permite solo números
    """
    if not 3 <= len(nombre) <= 100:
        return False
    
    if re.match(r"^[0-9\s\-\.]+$", nombre):  # Si contiene solo números
        return False
    
    return re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\-\.\,\/]+$", nombre) is not None