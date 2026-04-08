from database import get_connection #importo la función para obtener la conexión a la base de datos

class Equipos: #creo clase donde hacer el CRUD de los equipos médicos
    def __init__(self): #al inicializar la clase se hace conexion con la base de datos  y se crea el cursor para ejecutar las consultas
        self.conn = get_connection() 
        self.cursor = self.conn.cursor()
    def insertar(self, nombre, tipo, ubicacion): #funcion para insertar un nuevo equipo medico, recibe como parametros el nombre, tipo y ubicacion del equipo medico
        self.cursor.execute('''
            INSERT INTO equipos_medicos (nombre, tipo, ubicacion) VALUES (?, ?, ?)
        ''', (nombre, tipo, ubicacion)) #ejecuta la consulta para insertar un nuevo equipo medico en la tabla equipos_medicos, los valores se pasan como tupla para evitar inyecciones SQL
        self.conn.commit()
    def listar(self):
        self.cursor.execute('''SELECT * FROM equipos_medicos''')
        return self.cursor.fetchall() #devuelve datos de equipos medicos
    def actualizar(self, nombre, tipo, ubicacion, id_equipo):
        self.cursor.execute(''' UPDATE equipos_medicos SET nombre=?, tipo=?, ubicacion=? WHERE id_equipos=?''',(nombre,tipo,ubicacion,id_equipo)) #ejecuta la consulta para actualizar un equipo medico de la tabla equipos_medicos, los valores se pasan como tupla para evitar inyecciones SQL
        self.conn.commit()
    def eliminar(self, id_equipo):
        self.cursor.execute('''DELETE FROM equipos_medicos WHERE id_equipos = ?''', (id_equipo,)) #ejecuta la consulta para eliminar un equipo medico de la tabla equipos_medicos, el id del equipo medico se pasa como tupla para evitar inyecciones SQL
        self.conn.commit()
    def buscar_por_id(self,id_equipo):
        self.cursor.execute('''SELECT * FROM equipos_medicos WHERE id_equipos=?''', (id_equipo,))
        return self.cursor.fetchone() #devuelve datos de un equipo medico por su id
