import sqlite3

db = sqlite3.connect("invernadero.db")
c = db.cursor()

def mostrar_usuario():
    r = c.execute("SELECT *  FROM usuario")
    r = r.fetchall()
    
    for fila in r:
        print(fila)
        
mostrar_usuario()