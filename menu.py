from conexion import Invernadero
class Menu:
    inv = Invernadero()
    def __init__(self):
        while True:
            print("1) Mostrar Usuarios")
            print("2) Agregar Usuario")
            print("3) Buscar")
            print("0) Salir")
            op = input()
            
            if op == "1":
                self.mostrar()
            elif op == "2":
                self.capturar()
            elif op == "3":
                self.buscar()            
            elif op == "0":
                break
                
    def mostrar(self):
        usuarios = self.inv.mostrar_usuario()
        for u in usuarios:
            print("{0:2} {1:10} {2:8} {3:8} {4:15} {5:6} {6:1}".format(u[0], u[1], u[2], u[3], u[4], u[5], u[6]))
            
    def capturar(self):
        nombre = input("Nombre: ")
        apellido1 = input("Apellido 1: ")
        apellido2 = input("Apellido 2: ")
        correo = input("Correo: ")
        password = input("Password: ")
        tipo = input("Tipo: ")
        
        self.inv.insertar_usuario([nombre, apellido1, apellido2, correo, password, tipo])
    
    def buscar(self):
        palabra = input("Ingresa la palabra de busqueda")
        lista = self.inv.buscar_usuario(palabra)
        for u in lista:
            print("{0:2} {1:10} {2:8} {3:8} {4:15} {5:6} {6:1}".format(u['id'], u['nombre'], u['apellido1'], u['apellido2'], u['correo'], u['password'], u['tipo']))
                  