import sqlite3

class Invernadero:
    db = sqlite3.connect("invernadero.db")
    c = db.cursor()

    def mostrar_usuario(self):
        r = self.c.execute("SELECT *  FROM usuario")
        r = r.fetchall()
        lista = []

        for fila in r:
            lista.append(fila)
            
        return lista

    def insertar_usuario(self, datos):
        self.c.execute("INSERT INTO usuario (nombre, apellido1, apellido2, correo, passwoord, tipo) VALUES(?,?,?,?,?,?)", (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))
        self.db.commit()
    
    def buscar_usuario(self, palabra):
        self.c.execute("SELECT * FROM usuario WHERE correo LIKE ?", ("%"+palabra+"%",))
        
        lista = []
        for e in self.c:
            usuario = {'id': e[0], 
                       'nombre': e[1],
                       'apellido1': e[2],
                       'apellido2': e[3],
                       'correo': e[4],
                       'password': e[5],
                       'tipo': e[6] }
            lista.append(usuario)
        
        return lista