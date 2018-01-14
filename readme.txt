Projectos Django
================
Suponemos que ya tenemos instalado Python 3.

- Instalar entorno virtual en directorio de proyectos:

python -m venv evInversiones

- Activar entorno virtual en directorio de proyectos:

python -m venv evInversiones

- Instalar Django en entorno virtual. Permite que cada proyecto tenga la versión de Django que nos interese:

pip install Django==2.0.1

- Crear proyecto (fijate que lleva un "." al final):

django-admin startproject Inversiones .

- Modificamos archivos Inversiones\settings.py para añadir TIME_ZONE correcto y urls státicas:

TIME_ZONE = 'Europe/Berlin'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

- Creamos la base de datos de nuestro proyecto:

(evInversiones) C:\ProyectosDjango>python manage.py migrate

- Para activar el servidor y poder abrir la url:

(evInversiones) C:\ProyectosDjango>python manage.py runserver

- Una vez arrancado comprobar con "http://127.0.0.1:8000/"

- Creamos una aplicación

(evInversiones) C:\ProyectosDjango>python manage.py startapp cartera

- Incluir aplicación de el sitio Inversiones, editando "Inversiones/settings.py":

INSTALLED_APPS = (
...
'cartera',
)

- Creamos el modelo "entradas" en cartera\models.py:
- Creamos la tabla en la base de datos:

(evInversiones) C:\ProyectosDjango>python manage.py makemigrations cartera
(evInversiones) C:\ProyectosDjango>python manage.py migrate cartera

- Administrar la BBDD creada. Editar "cartera\admin.py"
