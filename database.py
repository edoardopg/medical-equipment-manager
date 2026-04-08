import sqlite3 #importamos libreria para manejar la base de datos

def get_connection():
    conn = sqlite3.connect("data.db")
    return conn
