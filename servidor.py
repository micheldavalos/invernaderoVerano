from flask import Flask, jsonify
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

app.run()