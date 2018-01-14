GIT
===

- Iniciar repositorio git (solo la primera vez):
(evInversiones) C:\ProyectosDjango>git init
Initialized empty Git repository in C:/ProyectosDjango/.git/
(evInversiones) C:\ProyectosDjango>git config user.name "efolea"
(evInversiones) C:\ProyectosDjango>git config user.email efolea@gmail.com

- Crear .gitignore para que no exporte ficheros que no modificamos.
*.pyc
__pycache__
myvenv
evInversiones
db.sqlite3
.DS_Store

- "git status" nos indica si hay modificaciones que subir a git:
