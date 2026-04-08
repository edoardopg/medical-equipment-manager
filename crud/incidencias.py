from database import get_connection


class Incidencias:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
    def insertar(self,id_equipo,fecha,tipo_error,descripcion):
        self.cursor.execute('''INSERT INTO incidencias (id_equipo,fecha,tipo_error,descripcion) VALUES (?,?,?,?)''',(id_equipo,fecha,tipo_error,descripcion))
        self.conn.commit()
    def listar(self):
        self.cursor.execute('''SELECT incidencias.*, equipos_medicos.nombre FROM incidencias JOIN equipos_medicos ON incidencias.id_equipo = equipos_medicos.id_equipos  
                    ''')
        return self.cursor.fetchall()
    def actualizar(self,fecha,tipo_error,descripcion,id_incidencia): 
        self.cursor.execute('''UPDATE incidencias SET fecha=?,tipo_error=?,descripcion=? WHERE id_incidencia=?''',(fecha,tipo_error,descripcion,id_incidencia))
        self.conn.commit()
    def eliminar(self,id_incidencia):
        self.cursor.execute('''DELETE FROM incidencias WHERE id_incidencia=?''',(id_incidencia,))
        self.conn.commit()
    def buscar_por_id(self,id_incidencia):
        self.cursor.execute('''SELECT incidencias.*, equipos_medicos.nombre FROM incidencias JOIN equipos_medicos ON incidencias.id_equipo = equipos_medicos.id_equipos WHERE id_incidencia=?''',(id_incidencia,))
        return self.cursor.fetchone()
    