# models/cliente.py
from models.conexion import get_connection

def insertar_cliente(data):
    con = get_connection()
    cursor = con.cursor()
    sql = """
        INSERT INTO cliente (nombre, dni, email, telefono, direccion, razon_social, ruc)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, data)
    con.commit()
    con.close()

def obtener_clientes():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
    con.close()
    return resultados

def actualizar_cliente(id_cliente, data):
    con = get_connection()
    cursor = con.cursor()
    sql = """
        UPDATE cliente SET nombre=%s, dni=%s, email=%s, telefono=%s,
        direccion=%s, razon_social=%s, ruc=%s WHERE id=%s
    """
    cursor.execute(sql, data + (id_cliente,))
    con.commit()
    con.close()

def eliminar_cliente(id_cliente):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM cliente WHERE id = %s", (id_cliente,))
    con.commit()
    con.close()
