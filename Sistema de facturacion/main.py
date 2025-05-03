from cliente import registrar_cliente, mostrar_clientes, editar_cliente
from producto import registrar_producto, mostrar_productos, editar_producto
from factura import crear_factura, mostrar_facturas, anular_factura

def menu():
    while True:
        print("\n--- Sistema de Facturación ---")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Editar cliente")
        print("4. Registrar producto")
        print("5. Ver productos")
        print("6. Editar producto")
        print("7. Crear factura")
        print("8. Ver facturas")
        print("9. Anular factura")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            mostrar_clientes()
        elif opcion == '3':
            editar_cliente()
        elif opcion == '4':
            registrar_producto()
        elif opcion == '5':
            mostrar_productos()
        elif opcion == '6':
            editar_producto()
        elif opcion == '7':
            crear_factura()
        elif opcion == '8':
            mostrar_facturas()
        elif opcion == '9':
            anular_factura()
        elif opcion == '10':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()