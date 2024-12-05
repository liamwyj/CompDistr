import requests
from flask import session

# URL base de la API
BASE_URL = 'http://localhost:9000'

def test_obtener_practicas():
    response = requests.get(BASE_URL + '/practicas')
    if response.status_code != 200:
        print(f'Error: Código de estado recibido: {response.status_code}')
        print(f'Respuesta del servidor: {response.text}')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print('Prueba de GET /practicas pasada con éxito.')

#Para iniciar sesión antes de hacer el POST
    
def login():
    login_data = {
        "username": "admin",  
        "password": "contraseña1234" 
    }
    session = requests.Session()  # Crea una sesión de Requests
    response = session.post(BASE_URL + "/login", json=login_data)
    
    if response.status_code == 200:
        print("Inicio de sesión exitoso")
        return session  # Devuelve la sesión autenticada para su uso posterior
    else:
        print("Error al iniciar sesión:", response.status_code, response.json())
        return None
    
def test_crear_proyecto_computacion_distribuida():
    session = login()
    if not session:
        print("No se pudo autenticar")
        return
    
    nueva_practica = {
        'title': 'Computación Distribuida',
        'description': 'Este proyecto aborda la implementación y despliegue de aplicaciones distribuidas, con un enfoque en la creación de páginas web empleando HTML y VUE.js. También se estudió la integración fluida entre el backend y el frontend para construir aplicaciones modernas y escalables.',
        'image': 'https://elalbirdotcom.files.wordpress.com/2017/07/computacion-p.jpg?w=768&h=331',
        'links': [
            {'label': 'Práctica 1', 'url': 'practicas/practica1_cd.html'}
        ]
    }
    
    # Usa la misma sesión para enviar la solicitud de creación de proyecto
    response = session.post(BASE_URL + '/practicas', json=nueva_practica)
    
    if response.status_code != 201:
        print(f'Error: Código de estado recibido: {response.status_code}')
        print(f'Respuesta del servidor: {response.text}')
    assert response.status_code == 201
    created_project = response.json()
    print(f'Prueba de creación de proyecto "Computación Distribuida" pasada con éxito. ID creado: {created_project["id"]}')
    return created_project['id']

def test_crear_proyecto_aprendizaje_automatico_ii():
    session = login()
    if not session:
        print("No se pudo autenticar")
        return
    
    nueva_practica = {
        'title': 'Aprendizaje Automático II',
        'description': 'Este proyecto se centró en el análisis y aplicación de algoritmos de aprendizaje automático, como los árboles de decisión y el método K-Nearest Neighbors (KNN). Se exploraron estos modelos para resolver problemas complejos y entender sus implicaciones en la clasificación de datos.',
        'image': 'https://th.bing.com/th/id/OIP.KFHMNHw7EN1yKiJ5UVzkAQHaET?rs=1&pid=ImgDetMain',
        'links': [
            {'label': 'Práctica Funciones', 'url': 'practicas/solo_funciones.html'}
        ]
    }
    
    response = session.post(BASE_URL + '/practicas', json=nueva_practica)
    if response.status_code != 201:
        print(f'Error: Código de estado recibido: {response.status_code}')
        print(f'Respuesta del servidor: {response.text}')
    assert response.status_code == 201
    created_project = response.json()
    print(f'Prueba de creación de proyecto "Aprendizaje Automático II" pasada con éxito. ID creado: {created_project["id"]}')
    return created_project['id']

def test_crear_proyecto_metodos_estadisticos_avanzados():
    session = login()
    if not session:
        print("No se pudo autenticar")
        return
    
    nueva_practica = {
        'title': 'Métodos Estadísticos Avanzados en Clasificación de Datos',
        'description': 'En esta asignatura, se estudiaron enfoques estadísticos avanzados para describir y analizar conjuntos de datos de alta dimensionalidad. Se exploraron técnicas de clasificación no supervisada, incluyendo métodos que ayudan a descubrir patrones subyacentes y estructura en los datos complejos, mejorando la comprensión y el análisis.',
        'image': 'https://aprendiendoadministracion.com/wp-content/uploads/2016/01/20140305-estadistica.jpg',
        'links': [
            {'label': 'Laboratorio 1', 'url': 'practicas/Solucion-Lab-1.html'}
        ]
    }
    
    response = session.post(BASE_URL + '/practicas', json=nueva_practica)
    if response.status_code != 201:
        print(f'Error: Código de estado recibido: {response.status_code}')
        print(f'Respuesta del servidor: {response.text}')
    assert response.status_code == 201
    created_project = response.json()
    print(f'Prueba de creación de proyecto "Métodos Estadísticos Avanzados en Clasificación de Datos" pasada con éxito. ID creado: {created_project["id"]}')
    return created_project['id']

def test_actualizar_practica(practice_id):
    practica_actualizada = {
        'title': 'Métodos Estadísticos Avanzados en Clasificación de Datos',
        'description': 'Esta actualización profundiza en el uso de técnicas estadísticas avanzadas para describir y analizar conjuntos de datos de alta dimensión. Se evaluaron métodos de clasificación no supervisada que permiten identificar patrones complejos y estructuras ocultas en los datos, proporcionando insights valiosos para aplicaciones analíticas.',
        'image': 'https://isdfundacion.org/wp-content/uploads/2019/11/Plantilla-entradas-ESTADISTICA-1.jpg',
        'links': [
            {'label': 'Solución Laboratorio 1 Actualizada', 'url': 'practicas/Solucion-Lab-1.html'}
        ]
    }
    response = requests.put(BASE_URL + f'/practicas/{practice_id}', json=practica_actualizada)
    if response.status_code != 200:
        print(f'Error: Código de estado recibido: {response.status_code}')
        print(f'Respuesta del servidor: {response.text}')
    assert response.status_code == 200
    print(f'Prueba de actualización de proyecto "Métodos Estadísticos Avanzados en Clasificación de Datos" con ID {practice_id} pasada con éxito.')

def test_eliminar_practica(practice_id):
    response = requests.delete(BASE_URL + f'/practicas/{practice_id}')
    if response.status_code != 200:
        print(f'Error: Código de estado recibido: {response.status_code}')
        print(f'Respuesta del servidor: {response.text}')
    assert response.status_code == 200
    print(f'Prueba de eliminación del "proyecto Aprendizaje Automático II" con ID {practice_id} pasada con éxito.')

if __name__ == '__main__':
    # Ejecutar pruebas
    test_obtener_practicas()
    # Ejecutar pruebas de creación de proyectos específicos
    id_computacion_distribuida = test_crear_proyecto_computacion_distribuida()
    id_aprendizaje_automatico_ii = test_crear_proyecto_aprendizaje_automatico_ii()
    id_metodos_estadisticos = test_crear_proyecto_metodos_estadisticos_avanzados()

    test_actualizar_practica(id_metodos_estadisticos)
    test_eliminar_practica(id_aprendizaje_automatico_ii)
