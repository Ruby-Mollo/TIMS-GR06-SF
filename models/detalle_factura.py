from models.conexion import Conexion

class DetalleFactura:
    def __init__(self):
        self.conexion = Conexion()

    def agregar(self, id_factura, id_producto, cantidad, precio_unitario, subtotal):
        conn = self.conexion.conectar()
        cursor = conn.cursor()
        sql = '''
            INSERT INTO detalle_factura (id_factura, id_producto, cantidad, precio_unitario, subtotal)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (id_factura, id_producto, cantidad, precio_unitario, subtotal))
        conn.commit()
        conn.close()

    def modificar(self, id_detalle, id_factura, id_producto, cantidad, precio_unitario, subtotal):
        conn = self.conexion.conectar()
        cursor = conn.cursor()
        sql = '''
            UPDATE detalle_factura
            SET id_factura=%s, id_producto=%s, cantidad=%s, precio_unitario=%s, subtotal=%s
            WHERE id=%s
        '''
        cursor.execute(sql, (id_factura, id_producto, cantidad, precio_unitario, subtotal, id_detalle))
        conn.commit()
        conn.close()

    def eliminar(self, id_detalle):
        conn = self.conexion.conectar()
        cursor = conn.cursor()
        sql = 'DELETE FROM detalle_factura WHERE id=%s'
        cursor.execute(sql, (id_detalle,))
        conn.commit()
        conn.close()

    def listar(self):
        conn = self.conexion.conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT df.*, p.nombre AS producto_nombre
            FROM detalle_factura df
            JOIN producto p ON df.id_producto = p.id
        ''')
        resultados = cursor.fetchall()
        conn.close()
        return resultados
