from database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipos_medicos(
            id_equipos INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            tipo TEXT,
            ubicacion TEXT
            ) 
            ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS incidencias(
            id_incidencia INTEGER PRIMARY KEY AUTOINCREMENT,
            id_equipo INTEGER,
            fecha TEXT,
            tipo_error TEXT,
            descripcion TEXT,
            FOREIGN KEY (id_equipo) REFERENCES equipos_medicos (id_equipos)
            )
            ''')
    conn.commit()
    conn.close()

def insert_initial_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM equipos_medicos")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('''
                INSERT INTO equipos_medicos (nombre,tipo,ubicacion) VALUES
                    ('FLUOROCYCLER', 'Termociclador', 'Microbiologia'),
                    ('MICROSCOPIO_1', 'Microscopio', 'Sala de Microscopios'),
                    ('CENTRIFUGA_3', 'Centrífuga', 'Laboratorio'),
                    ('ESPECTROFOTOMETRO_2', 'Espectrofotómetro', 'Sala de Espectrofotómetros')
                ''')
    conn.commit()
    conn.close()
        
