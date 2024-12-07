from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
import sqlite3
import json
import os

# Configuración de la aplicación Flask
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Clave secreta desde variables de entorno

# Configuración para sesiones persistentes
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

# Configurar CORS para permitir solicitudes desde el frontend desplegado
CORS(app, resources={r"/*": {"origins": "https://portfolio-02-ft7r.onrender.com"}}, supports_credentials=True)

# Ruta de la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'practicas.db')

# Datos del usuario administrador
USER_DATA = {
    "username": "admin",
    "password": generate_password_hash("contraseña1234")  # Contraseña cifrada
}

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API de Prácticas"})

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/practicas', methods=['GET'])
def obtener_practicas():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT * FROM practicas")
            practicas = [dict(row) for row in c.fetchall()]
            for practica in practicas:
                practica['links'] = json.loads(practica['links'])
        return jsonify(practicas), 200
    except sqlite3.Error as e:
        return jsonify({"error": "Error de base de datos: " + str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username == USER_DATA["username"] and check_password_hash(USER_DATA["password"], password):
        session['logged_in'] = True
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return jsonify({"message": "Cierre de sesión exitoso"}), 200

@app.route('/practicas', methods=['POST'])
def agregar_practica():
    if not session.get('logged_in'):
        return jsonify({"error": "No autorizado"}), 403
    try:
        data = request.json
        links = json.dumps(data.get('links', []))
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO practicas (image, title, description, links) VALUES (?, ?, ?, ?)",
                      (data['image'], data['title'], data['description'], links))
            new_id = c.lastrowid
            data['id'] = new_id
        return jsonify(data), 201
    except sqlite3.Error as e:
        return jsonify({"error": "Error de base de datos: " + str(e)}), 500

@app.route('/practicas/<int:id>', methods=['DELETE'])
def eliminar_practica(id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM practicas WHERE id = ?", (id,))
            if c.rowcount == 0:
                return jsonify({"error": "Práctica no encontrada."}), 404
        return jsonify({"message": "Práctica eliminada."}), 200
    except sqlite3.Error as e:
        return jsonify({"error": "Error de base de datos: " + str(e)}), 500

@app.route('/practicas/<int:id>', methods=['PUT'])
def actualizar_practica(id):
    try:
        data = request.json
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute(
                "UPDATE practicas SET image = ?, title = ?, description = ?, links = ? WHERE id = ?",
                (data['image'], data['title'], data['description'], json.dumps(data['links']), id)
            )
            conn.commit()
        return jsonify({"message": "Práctica actualizada correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/practicas/buscar', methods=['GET'])
def buscar_practicas():
    search_term = request.args.get('searchTerm', '').strip().lower()
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            if search_term:
                c.execute("SELECT * FROM practicas WHERE LOWER(title) LIKE ?", ('%' + search_term + '%',))
            else:
                c.execute("SELECT * FROM practicas")
            practicas = [dict(row) for row in c.fetchall()]
            if not practicas:
                return jsonify({"error": "No se encontraron prácticas que coincidan con la búsqueda."}), 404
            for practica in practicas:
                practica['links'] = json.loads(practica['links'])
        return jsonify(practicas), 200
    except sqlite3.Error as e:
        return jsonify({"error": "Error de base de datos: " + str(e)}), 500

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9000)
