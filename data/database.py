import sqlite3

def crear_base():
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    
    # Tabla de usuarios
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            usuario TEXT UNIQUE NOT NULL,
            clave TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def registrar_usuario(nombre, apellido, usuario, clave, tipo):
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO usuarios (nombre, apellido, usuario, clave, tipo) VALUES (?, ?, ?, ?, ?)",
                  (nombre, apellido, usuario, clave, tipo))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validar_credenciales(usuario, clave):
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("SELECT tipo FROM usuarios WHERE usuario = ? AND clave = ?", (usuario, clave))
    resultado = c.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def obtener_usuarios():
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("SELECT nombre, apellido, tipo FROM usuarios")
    resultados = c.fetchall()
    conn.close()
    return resultados