import sqlite3 

def conectar():
    return sqlite3.connect("inventario.db")

def inicializar_db():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL,
            descripcion TEXT,
            categoria TEXT DEFAULT 'General'
        );
        """
    )
    conexion.commit()
    conexion.close()

inicializar_db()