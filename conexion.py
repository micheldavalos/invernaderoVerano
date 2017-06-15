import sqlite3

db = sqlite3.connect("invernadero.db")
c = db.cursor()

def mostrar_usuario():
    r = c.execute("SELECT *  FROM usuario")
    r = r.fetchall()
    
    for fila in r:
        print(fila)
        
def insertar_usuario(datos):
    c.execute("INSERT INTO usuario (nombre, apellido1, apellido2, correo, passwoord, tipo) VALUES(?,?,?,?,?,?)", (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))
    db.commit()
    
insertar_usuario(["m", "d", "b", "m@gmail.com", "1", 1])
mostrar_usuario()