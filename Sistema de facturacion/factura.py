import json
import os
from datetime import datetime
from cliente import cargar_clientes
from producto import cargar_productos, guardar_productos
from utils import calcular_igv_total

data_path = "datos/facturas.json"

def cargar_facturas():
    """Carga las facturas desde el archivo JSON"""
    if not os.path.exists("datos"):
        os.makedirs("datos")
    if not os.path.exists(data_path):
        return []
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_facturas(facturas):
    """Guarda la lista de facturas en el archivo JSON"""
    with open(data_path, 'w') as f:
        json.dump(facturas, f, indent=4)

def crear_factura():
    """Crea una nueva factura con validaciones"""
    clientes = [c for c in cargar_clientes() if c['estado'] == 'activo']
    productos = [p for p in cargar_productos() if p['estado'] == 'activo' and p['stock'] > 0]
    facturas = cargar_facturas()

    if not clientes:
        print("Error: No hay clientes registrados.")
        return
    if not productos:
        print("Error: No hay productos disponibles.")
        return

    print("\n--- NUEVA FACTURA ---")
    
    # Selección de cliente
    mostrar_clientes(clientes)
    while True:
        try:
            opcion = int(input("\nSeleccione cliente (ID): "))
            cliente = next((c for c in clientes if c['id'] == opcion), None)
            if cliente:
                break
            print("Error: ID no válido.")
        except ValueError:
            print("Error: Ingrese un número.")

    # Selección de productos
    items = []
    while True:
        mostrar_productos(productos)
        try:
            opcion = int(input("\nSeleccione producto (ID): "))
            producto = next((p for p in productos if p['id'] == opcion), None)
            if not producto:
                print("Error: ID no válido.")
                continue
                
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("Error: Cantidad debe ser positiva.")
                continue
            if cantidad > producto['stock']:
                print(f"Error: Stock insuficiente (disponible: {producto['stock']}).")
                continue
                
            items.append({
                "id": producto['id'],
                "nombre": producto['nombre'],
                "precio": producto['precio'],
                "cantidad": cantidad
            })
            producto['stock'] -= cantidad
            
            if input("¿Agregar otro producto? (s/n): ").lower() != 's':
                break
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")

    # Cálculo de totales
    total, igv, subtotal = calcular_igv_total(items)
    nueva_factura = {
        "id": len(facturas) + 1,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "cliente": cliente,
        "items": items,
        "subtotal": subtotal,
        "igv": igv,
        "total": total,
        "estado": "vigente"
    }
    
    guardar_productos(productos)
    facturas.append(nueva_factura)
    guardar_facturas(facturas)
    print("\nACTURA GENERADA CON ÉXITO!")
    imprimir_factura(nueva_factura)

def mostrar_facturas():
    """Muestra todas las facturas vigentes"""
    facturas = [f for f in cargar_facturas() if f['estado'] == 'vigente']
    if not facturas:
        print("\nNo hay facturas registradas.")
        return
    
    print("\n--- HISTORIAL DE FACTURAS ---")
    for fac in facturas:
        print(f"\nFactura #ID: {fac['id']} | Fecha: {fac['fecha']}")
        print(f"Cliente: {fac['cliente']['nombre']} (RUC: {fac['cliente']['ruc']})")
        for item in fac['items']:
            print(f"  - {item['nombre']} x{item['cantidad']} @ S/{item['precio']:.2f}")
        print(f"TOTAL: S/{fac['total']:.2f} (IGV: S/{fac['igv']:.2f})")

def anular_factura():
    """Anula una factura existente"""
    facturas = cargar_facturas()
    productos = cargar_productos()
    mostrar_facturas()
    
    try:
        id_factura = int(input("\nID de factura a anular: "))
        factura = next((f for f in facturas if f['id'] == id_factura), None)
        
        if not factura:
            print("Error: Factura no encontrada.")
            return
            
        factura['estado'] = "anulado"
        guardar_facturas(facturas)
        print("Factura anulada correctamente.")
    except ValueError:
        print("Error: Ingrese un ID numérico válido.")

    if factura['estado'] == "vigente":
        for item in factura['items']:
            for p in productos:
                if p['id'] == item['id']:
                    p['stock'] += item['cantidad']
        guardar_productos(productos)

# Funciones auxiliares
def mostrar_clientes(clientes):
    print("\n--- CLIENTES DISPONIBLES ---")
    for c in clientes:
        print(f"ID: {c['id']} | {c['nombre']}")

def mostrar_productos(productos):
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for p in productos:
        print(f"ID: {p['id']} | {p['nombre']} | S/{p['precio']:.2f} | Stock: {p['stock']}")

def imprimir_factura(factura):
    print("\n--- FACTURA ---")
    print(f"Fecha: {factura['fecha']}")
    print(f"Cliente: {factura['cliente']['nombre']} (RUC: {factura['cliente']['ruc']})")
    print("\nDetalle:")
    for item in factura['items']:
        print(f"  - {item['nombre']:20} x{item['cantidad']:3} @ S/{item['precio']:7.2f} = S/{item['precio'] * item['cantidad']:8.2f}")
    print("\nTOTAL:")
    print(f"Subtotal: S/{factura['subtotal']:.2f}")
    print(f"IGV (18%): S/{factura['igv']:.2f}")
    print(f"TOTAL A PAGAR: S/{factura['total']:.2f}")
    print("\n" + "="*40)
