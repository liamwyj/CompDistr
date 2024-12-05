# 7311-02

En esta práctica hemos consumido una API externa usando la API de prueba de REQRES, también hemos configurado un servidor backend que implementa una API RESTful básica y lo hemos conectado al frontend de nuestro portafolio.

![Screenshot](ruta/de/la/imagen.png)

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Instalación

Se ha de descargar la carpeta comprimida con el nombre '7311-02'. Además, asegúrate de tener instaladas las siguientes librerías: *flask*, *flask_cors*, *sqlite3*, y *requests*, así como *Node.js*, *Axios*, y *Vue.js*.

## Uso

Para ejecutar este proyecto, sigue estos pasos en el orden indicado:

### 1. Configuración de la base de datos

Primero al haber eliminado la carpeta de node_modulos tenemos que ejecutar estos comandos por separado:

```bash
npm install
```

```bash
npm run build
```

Luego, nos situamos en el directorio de database y ejecutamos el siguiente comando:

```bash
python setup_db.py
```

### 2. Inicialización del backend

Nos situamos en el directorio de backend y ejecutamos en la terminal:

```bash
python app.py
```
### 3. Ejecución del frontend

Nos movemos al directorio principal del proyecto y ejecutamos:

```bash
npm run dev
```
### 4. Ejecución del script de pruebas
Para probar la creación de proyectos con el script script_test.py, asegúrate de que el backend esté en ejecución con python app.py y luego ejecuta:

```bash

python script_test.py
```
## Características

- Visualización de proyectos en el portafolio.
- Añadir nuevos proyectos si se ha autenticado correctamente.
- Eliminar proyectos existentes o recién añadidos.
- Búsqueda entre los proyectos disponibles.
- Autenticación
- Credenciales de Usuario

Para acceder a la funcionalidad de agregar proyectos, utiliza las siguientes credenciales:

Usuario: admin
Contraseña: contraseña1234
Métodos de Autenticación Soportados y Alternativos
Actualmente, este proyecto utiliza autenticación basada en sesiones de Flask, que permite al servidor almacenar una cookie de sesión que identifica al usuario después de iniciar sesión.

A continuación, se describen brevemente otros métodos de autenticación comunes que podrían implementarse:

- Sesiones de Flask (Actual):

El servidor crea una sesión y almacena una cookie en el navegador del usuario después del inicio de sesión.
Ideal para aplicaciones donde el servidor y el cliente están en el mismo dominio o en un entorno controlado.
Limitación: Las sesiones son menos ideales para aplicaciones distribuidas o sin estado.

- JSON Web Tokens (JWT):

JWT permite emitir un token después de la autenticación que el cliente envía en cada solicitud, generalmente en el encabezado Authorization.
Este método es popular en aplicaciones RESTful y facilita el escalado, ya que no depende de un estado en el servidor.
Ventaja: El token es portable y puede ser usado en aplicaciones distribuidas o con múltiples servicios.

- Autenticación Básica (Basic Auth):

En cada solicitud, el cliente envía un encabezado con una combinación de usuario y contraseña codificada en Base64.
Es simple de implementar pero menos segura, ya que las credenciales se envían en cada solicitud.
Usualmente se utiliza en aplicaciones internas o en combinación con HTTPS para mayor seguridad.
Estos métodos de autenticación ofrecen alternativas a las sesiones de Flask y pueden ser útiles en distintos contextos según los requisitos de seguridad y escalabilidad.

## Contribuciones

Contribuciones son bienvenidas y se verán reflejadas en la nota.

## Licencia
Este proyecto fue creado por Yijun Wang, Jimena de Prado y Geer Wang.
