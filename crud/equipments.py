from database import get_connection #importo la función para obtener la conexión a la base de datos

class Equipments: #creo clase donde hacer el CRUD de los equipos médicos
    def __init__(self): #al inicializar la clase se hace conexion con la base de datos  y se crea el cursor para ejecutar las consultas
        self.conn = get_connection() 
        self.cursor = self.conn.cursor()
    def insert(self, name, type, location): #funcion para insertar un nuevo equipo medico, recibe como parametros el nombre, tipo y ubicacion del equipo medico
        self.cursor.execute('''
            INSERT INTO medical_equipments (name, type, location) VALUES (?, ?, ?)
        ''', (name, type, location)) #ejecuta la consulta para insertar un nuevo equipo medico en la tabla medical_equipments, los valores se pasan como tupla para evitar inyecciones SQL
        self.conn.commit()
    def list(self):
        self.cursor.execute('''SELECT * FROM medical_equipments''')
        return self.cursor.fetchall() #devuelve todos los datos de equipos medicos
    def update(self, name, type, location, id_equipment):
        self.cursor.execute(''' UPDATE medical_equipments SET name=?, type=?, location=? WHERE id_equipment=?''',(name,type,location,id_equipment)) #ejecuta la consulta para actualizar un equipo medico de la tabla medical_equipments, los valores se pasan como tupla para evitar inyecciones SQL
        self.conn.commit()
    def delete(self, id_equipment):
        self.cursor.execute('''DELETE FROM medical_equipments WHERE id_equipment = ?''', (id_equipment,)) #ejecuta la consulta para eliminar un equipo medico de la tabla equipos_medicos, el id del equipo medico se pasa como tupla para evitar inyecciones SQL
        self.conn.commit()
    def find_by_id(self,id_equipment):
        self.cursor.execute('''SELECT * FROM medical_equipments WHERE id_equipment=?''', (id_equipment,))
        return self.cursor.fetchone() #devuelve datos de un equipo medico por su id
