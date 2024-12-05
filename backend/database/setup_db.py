import sqlite3
import os
import json

# Obtener la ruta absoluta de la base de datos
base_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta de la carpeta actual
db_path = os.path.join(base_dir, 'practicas.db')       # Ruta completa del archivo de la base de datos

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Crear la tabla 'practicas' si no existe
c.execute('''
CREATE TABLE IF NOT EXISTS practicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image TEXT,
    title TEXT,
    description TEXT,
    links TEXT
)
''')

# Datos de ejemplo para insertar en la tabla 'practicas'
practicas = [
    (
        "https://blog.orange.es/wp-content/uploads/sites/4/2022/02/wifillogo.png", 
        "Redes de Ordenadores", 
        "Es un campo fundamental en la informática que se enfoca en la interconexión de múltiples dispositivos.",
        json.dumps([
            {"label": "Práctica 1", "url": "practicas/p1redes.pdf"},
            {"label": "Práctica 2", "url": "practicas/p2redes.pdf"},
            {"label": "Práctica 3", "url": "practicas/p3redes.pdf"},
            {"label": "Práctica 4", "url": "practicas/p4redes.pdf"}
        ])
    ),
    (
        "https://image.freepik.com/free-vector/company-icon-simple-element-illustration-company-concept-symbol-design-can-be-used-web-mobile_159242-7784.jpg", 
        "Empresas, emprendimiento e innovación", 
        "Se centra en proporcionar una comprensión integral de cómo identificar oportunidades de negocio, desarrollar ideas innovadoras y crear empresas exitosas.",
        json.dumps([
            {"label": "Práctica Empresa", "url": "practicas/Practica_Empresa.pdf"}
        ])
    ),
    (
        "https://brandslogos.com/wp-content/uploads/images/large/python-logo-black-and-white.png", 
        "Programación II", 
        "Se centra en el estudio y aplicación de Tipos Abstractos de Datos (TAD), fundamentales para el desarrollo de software eficiente y bien estructurado.",
        json.dumps([
            {"label": "Práctica 1A", "url": "practicas/P1A_EX1.py"},
            {"label": "Práctica 1B", "url": "practicas/P1B_EX1.py"}
        ])
    ),
    (
        "https://cdn-icons-png.flaticon.com/512/30/30240.png", 
        "Bases de datos", 
        "Se enfoca en proporcionar los conocimientos y habilidades necesarios para crear, gestionar y utilizar bases de datos de manera efectiva en la solución de problemas informáticos.",
        json.dumps([
            {"label": "Práctica 1", "url": "practicas/p1datos.pdf"},
            {"label": "Práctica 2", "url": "practicas/p2datos.pdf"},
            {"label": "Práctica 3", "url": "practicas/p3datos.pdf"},
            {"label": "Práctica 4", "url": "practicas/p4datos.pdf"}
        ])
    )
]

# Insertar los datos en la tabla si el título no existe ya en la tabla
for practica in practicas:
    c.execute("SELECT COUNT(*) FROM practicas WHERE title = ?", (practica[1],))
    if c.fetchone()[0] == 0:  # Si el título no existe, inserta el registro
        c.execute("INSERT INTO practicas (image, title, description, links) VALUES (?, ?, ?, ?)", practica)

# Guardar y cerrar la conexión
conn.commit()
conn.close()
