from models.conexion import Conexion

class Factura:
    def __init__(self):
        self.conexion = Conexion()

    def agregar(self, id_cliente, fecha, subtotal, igv, total, estado='Pendiente'):
        conn = self.conexion.conectar()
        cursor = conn.cursor()
        sql = '''
            INSERT INTO factura (id_cliente, fecha, subtotal, igv, total, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (id_cliente, fecha, subtotal, igv, total, estado))
        conn.commit()
        conn.close()

    def modificar(self, id_factura, id_cliente, fecha, subtotal, igv, total, estado):
        conn = self.conexion.conectar()
        cursor = conn.cursor()
        sql = '''
            UPDATE factura
            SET id_cliente=%s, fecha=%s, subtotal=%s, igv=%s, total=%s, estado=%s
            WHERE id=%s
        '''
        cursor.execute(sql, (id_cliente, fecha, subtotal, igv, total, estado, id_factura))
        conn.commit()
        conn.close()

    def eliminar(self, id_factura):
        conn = self.conexion.conectar()
        cursor = conn.cursor()
        sql = 'DELETE FROM factura WHERE id=%s'
        cursor.execute(sql, (id_factura,))
        conn.commit()
        conn.close()

    def listar(self):
        conn = self.conexion.conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM factura')
        resultados = cursor.fetchall()
        conn.close()
        return resultados
