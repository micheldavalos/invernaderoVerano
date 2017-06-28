from flask import Flask, jsonify, request
from conexion import Invernadero

app = Flask("bd")
inv = Invernadero()

@app.route("/")
def raiz():
    return "Hola"

@app.route("/usuarios")
def usuarios():
    usuarios = inv.mostrar_usuario()
    print(usuarios)
    respuesta = jsonify(usuarios)
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    return respuesta

@app.route("/agregar_usuario", methods=['POST'])
def agregar_usuario():
    print(request.form)
    nombre = request.form['nombre']
    apellido1 = request.form['apellido1']
    apellido2 = request.form['apellido2']
    correo = request.form['correo']
    password = request.form['password']
    tipo = request.form['tipo']
    
    inv.insertar_usuario([nombre, apellido1, apellido2, correo, password, tipo])
    
    respuesta = jsonify({'status': 'Ok'})
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    return respuesta

app.run()