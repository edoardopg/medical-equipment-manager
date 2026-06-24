from database import get_connection
import bcrypt

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS medical_equipments(
            id_equipment INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            location TEXT
            ) 
            ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS incidents(
            id_incident INTEGER PRIMARY KEY AUTOINCREMENT,
            id_equipment INTEGER,
            date TEXT,
            type_error TEXT,
            description TEXT,
            FOREIGN KEY (id_equipment) REFERENCES medical_equipments (id_equipment)
            )
            ''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                email TEXT UNIQUE,
                password TEXT,
                failed_attempts INTEGER DEFAULT 0,
                block INTEGER DEFAULT 0,
                token_reset TEXT,
                token_expires TEXT
                )
                ''')
    conn.commit()
    conn.close()

def insert_initial_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM medical_equipments")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('''
                INSERT INTO medical_equipments (name,type,location) VALUES
                    ('FLUOROCYCLER', 'Termociclador', 'Microbiologia'),
                    ('MICROSCOPIO_1', 'Microscopio', 'Sala de Microscopios'),
                    ('CENTRIFUGA_3', 'Centrífuga', 'Laboratorio'),
                    ('ESPECTROFOTOMETRO_2', 'Espectrofotómetro', 'Sala de Espectrofotómetros')
                ''')
    conn.commit()
    conn.close()


def create_admin():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    if count == 0:
        hashed = bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")        
        cursor.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)", ("admin", "admin@example.com", hashed))
        conn.commit()
    conn.close()
        
