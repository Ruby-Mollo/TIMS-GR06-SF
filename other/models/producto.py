# models/producto.py
from models.conexion import get_connection

def insertar_producto(data):
    con = get_connection()
    cursor = con.cursor()
    sql = """
        INSERT INTO producto (nombre, descripcion, categoria, cantidad, precio)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, data)
    con.commit()
    con.close()

def obtener_productos():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    con.close()
    return resultados

def actualizar_producto(id_producto, data):
    con = get_connection()
    cursor = con.cursor()
    sql = """
        UPDATE producto SET nombre=%s, descripcion=%s, categoria=%s, cantidad=%s, precio=%s
        WHERE id=%s
    """
    cursor.execute(sql, data + (id_producto,))
    con.commit()
    con.close()

def eliminar_producto(id_producto):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM producto WHERE id = %s", (id_producto,))
    con.commit()
    con.close()
