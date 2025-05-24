import json
import os
from validador import validar_nombre_producto, validar_numero_float, validar_numero_int

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "datos", "productos.json")


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
        if validar_nombre_producto(nombre):
            break
        print("Error: Nombre inválido. Use 3-100 caracteres (no solo números).")

    while True:
        precio = input("Precio: ")
        if validar_numero_float(precio):
            valor_precio = float(precio)
            if 0.10 <= valor_precio <= 1_00:
                break
            else:
                print("Precio fuera de rango. Debe estar entre 0.10 y 100.")
        else:
            print("Precio inválido. Debe ser un número positivo.")


    while True:
        stock = input("Stock: ")
        if validar_numero_int(stock):
            valor_stock = int(stock)
            if 1 <= valor_stock <= 100:
                break
            else:
                print("Stock fuera de rango. Debe estar entre 1 y 100.")
        else:
            print("Stock inválido. Debe ser un número entero positivo.")


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
    producto = None
    while not producto:
        entrada = input("Ingrese el ID del producto a editar: ")
        try:
            producto_id = int(entrada)
            producto = next((p for p in productos if p["id"] == producto_id), None)
            if not producto:
                print("Producto no encontrado. Intente nuevamente.")
        except ValueError:
            print("Error: Solo se permiten números. Intente nuevamente.")

    print(f"Editando: {producto['nombre']}")

    producto = next((p for p in productos if p["id"] == producto_id), None)

    if producto:
        print(f"Editando: {producto['nombre']}")
        while True:
            nuevo_nombre = input("Nuevo nombre: ")
            if validar_nombre_producto(nuevo_nombre):
                producto['nombre'] = nuevo_nombre
                break
            print("Error: Nombre inválido. Use 3-100 caracteres (no solo números)")

        while True:
            nuevo_precio = input("Nuevo precio: ")
            if validar_numero_float(nuevo_precio) and 0.01 <= float(nuevo_precio) <= 1_000_000:
                producto['precio'] = float(nuevo_precio)
                break
            print("Precio inválido.")

        while True:
            nuevo_stock = input("Nuevo stock: ")
            if validar_numero_int(nuevo_stock):
                stock_valor = int(nuevo_stock)
                if 0 <= stock_valor <= 100:
                    producto['stock'] = stock_valor
                    break
                else:
                    print("Stock fuera de rango. Máximo permitido: 100,000.")
            else:
                print("Stock inválido. Debe ser un número entero positivo.")

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
