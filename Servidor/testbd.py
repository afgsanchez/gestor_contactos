import sqlite3

try:
    conn = sqlite3.connect('Contactos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Contacto';")
    result = cursor.fetchone()
    if result:
        print("La tabla 'Contacto' existe.")
    else:
        print("La tabla 'Contacto' no existe.")
    conn.close()
except sqlite3.Error as e:
    print("Error al conectar con la base de datos:", e)
