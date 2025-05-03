# controllers/cliente_controller.py
from models import cliente

def agregar_cliente(data):
    cliente.insertar_cliente(data)

def listar_clientes():
    return cliente.obtener_clientes()

def editar_cliente(id_cliente, data):
    cliente.actualizar_cliente(id_cliente, data)

def borrar_cliente(id_cliente):
    cliente.eliminar_cliente(id_cliente)
