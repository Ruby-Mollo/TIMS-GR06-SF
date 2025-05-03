import json
import os
from validador import validar_ruc, validar_email, validar_nombre

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "datos", "clientes.json")

def cargar_clientes():
    if not os.path.exists(data_path):
        return []
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def guardar_clientes(clientes):
    with open(data_path, 'w') as f:
        json.dump(clientes, f, indent=4)

def generar_id_cliente(clientes):
    if not clientes:
        return 1
    return max(c["id"] for c in clientes) + 1

def registrar_cliente():
    print("\n--- Registro de Cliente ---")
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            break
        print("Nombre inválido. Solo letras y espacios son permitidos.")

    while True:
        ruc = input("RUC: ")
        if validar_ruc(ruc):
            if any (c["ruc"] == ruc for c in cargar_clientes()):
                print("Error: RUC ya registrado")
                continue
            break
        print("RUC inválido. Debe contener exactamente 11 dígitos.")

    while True:
        email = input("Correo electrónico: ")
        if validar_email(email):
            break
        print("Correo electrónico inválido. Intente nuevamente.")
    
    clientes = cargar_clientes()
    nuevo_id = generar_id_cliente(clientes)

    clientes.append({
        "id": nuevo_id,
        "nombre": nombre,
        "ruc": ruc,
        "email": email,
        "estado": "activo"
    })
    guardar_clientes(clientes)
    print(f"Cliente registrado con éxito. ID asignado: {nuevo_id}")

def mostrar_clientes():
    clientes = cargar_clientes()
    print("\n--- Clientes Registrados ---")
    for cliente in clientes:
        print(f"ID: {cliente['id']} - Nombre: {cliente['nombre']}, RUC: {cliente['ruc']}, Estado: {cliente['estado']}")

def editar_cliente():
    clientes = cargar_clientes()
    mostrar_clientes()
    cliente_id = int(input("Ingrese el ID del cliente a editar: "))
    cliente = next((c for c in clientes if c["id"] == cliente_id), None)

    if cliente:
        print(f"Editando: {cliente['nombre']}")
        while True:
            nuevo_nombre = input("Nuevo nombre: ")
            if validar_nombre(nuevo_nombre):
                cliente['nombre'] = nuevo_nombre
                break
            print("Nombre inválido. Solo letras y espacios.")

        while True:
            nuevo_email = input("Nuevo correo electrónico: ")
            if validar_email(nuevo_email):
                cliente['email'] = nuevo_email
                break
            print("Correo electrónico inválido.")

        while True:
            nuevo_estado = input("Nuevo estado (activo/inactivo): ").lower()
            if nuevo_estado in ["activo", "inactivo"]:
                cliente['estado'] = nuevo_estado
                break
            print("Estado inválido. Use 'activo' o 'inactivo'.")

        guardar_clientes(clientes)
        print("Cliente actualizado con éxito.")
    else:
        print("Cliente no encontrado.")
