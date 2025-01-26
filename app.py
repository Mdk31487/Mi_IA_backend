# app.py

from flask import Flask, jsonify

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta básica
@app.route('/')
def hello_world():
    return jsonify(message="Hola, Mundo! Bienvenido a mi IA Backend")

# Ejecutar la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)
