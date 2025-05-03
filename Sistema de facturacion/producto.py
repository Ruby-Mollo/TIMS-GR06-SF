import json
import os
from validador import validar_nombre, validar_numero_float, validar_numero_int

data_path = "datos/productos.json"

def cargar_productos():
    if not os.path.exists(data_path):
        return []
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def guardar_productos(productos):
    with open(data_path, 'w') as f:
        json.dump(productos, f, indent=4)

def generar_id_producto(productos):
    if not productos:
        return 1
    return max(p["id"] for p in productos) + 1

def registrar_producto():
    print("\n--- Registro de Producto ---")
    while True:
        nombre = input("Nombre del producto: ")
        if validar_nombre(nombre):
            break
        print("Nombre inválido. Solo letras y espacios.")

    while True:
        precio = input("Precio: ")
        if validar_numero_float(precio):
            break
        print("Precio inválido. Debe ser un número positivo.")

    while True:
        stock = input("Stock: ")
        if validar_numero_int(stock):
            break
        print("Stock inválido. Debe ser un número entero.")

    productos = cargar_productos()
    nuevo_id = generar_id_producto(productos)

    productos.append({
        "id": nuevo_id,
        "nombre": nombre,
        "precio": float(precio),
        "stock": int(stock),
        "estado": "activo"
    })
    guardar_productos(productos)
    print(f"Producto registrado con éxito. ID asignado: {nuevo_id}")

def mostrar_productos():
    productos = cargar_productos()
    print("\n--- Productos Registrados ---")
    for producto in productos:
        print(f"ID: {producto['id']} - Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}, Estado: {producto['estado']}")

def editar_producto():
    productos = cargar_productos()
    mostrar_productos()
    producto_id = int(input("Ingrese el ID del producto a editar: "))
    producto = next((p for p in productos if p["id"] == producto_id), None)

    if producto:
        print(f"Editando: {producto['nombre']}")
        while True:
            nuevo_nombre = input("Nuevo nombre: ")
            if validar_nombre(nuevo_nombre):
                producto['nombre'] = nuevo_nombre
                break
            print("Nombre inválido. Solo letras y espacios.")

        while True:
            nuevo_precio = input("Nuevo precio: ")
            if validar_numero_float(nuevo_precio):
                producto['precio'] = float(nuevo_precio)
                break
            print("Precio inválido.")

        while True:
            nuevo_stock = input("Nuevo stock: ")
            if validar_numero_int(nuevo_stock):
                producto['stock'] = int(nuevo_stock)
                break
            print("Stock inválido.")

        while True:
            nuevo_estado = input("Nuevo estado (activo/inactivo): ").lower()
            if nuevo_estado in ["activo", "inactivo"]:
                producto['estado'] = nuevo_estado
                break
            print("Estado inválido. Use 'activo' o 'inactivo'.")

        guardar_productos(productos)
        print("Producto actualizado con éxito.")
    else:
        print("Producto no encontrado.")
