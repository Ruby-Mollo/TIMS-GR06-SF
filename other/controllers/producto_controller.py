# controllers/producto_controller.py
from models import producto

def agregar_producto(data):
    producto.insertar_producto(data)

def listar_productos():
    return producto.obtener_productos()

def editar_producto(id_producto, data):
    producto.actualizar_producto(id_producto, data)

def borrar_producto(id_producto):
    producto.eliminar_producto(id_producto)
