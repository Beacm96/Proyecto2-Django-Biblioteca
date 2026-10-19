# Biblioteca Digital

Proyecto desarrollado con **Django y Python** como parte del módulo de Django del Máster en Desarrollo Full Stack de Conquer Blocks.

## Descripción

Biblioteca Digital es una aplicación web que permite a los usuarios consultar libros, solicitar préstamos, devolver ejemplares, consultar su historial de préstamos y publicar reseñas.

La aplicación cuenta con un panel de administración de Django desde el que se pueden gestionar los libros y otros registros.

## Proyecto publicado

**Aplicación web:**  
https://proyecto2-django-biblioteca.onrender.com/

**Repositorio de GitHub:**  
https://github.com/Beacm96/Proyecto2-Django-Biblioteca

## Funcionalidades

- Registro de usuarios.
- Inicio y cierre de sesión.
- Listado de libros disponibles.
- Consulta de los detalles de cada libro.
- Préstamo y devolución de libros.
- Historial de préstamos por usuario.
- Sistema de reseñas y valoraciones.
- Administración de libros desde Django Admin.

## Modelos principales

- User
- Author
- Book
- Loan
- Review

## Tecnologías utilizadas

- Python
- Django 
- HTML y CSS
- SQLite para desarrollo local
- PostgreSQL para producción
- Gunicorn como servidor WSGI
- WhiteNoise para archivos estáticos
- Render para el despliegue
- Git y GitHub para control de versiones

## Instalación local

**1. Clonar el repositorio**

```bash
git clone https://github.com/Beacm96/Proyecto2-Django-Biblioteca.git
```

**2. Entrar en el proyecto**

```bash
cd Proyecto2-Django-Biblioteca
```

**3. Crear y activar un entorno virtual**

```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**5. Configurar las variables de entorno**

Para desarrollo local se puede utilizar SQLite sin configurar `DATABASE_URL`.

```bash
export DEBUG=True
```

Para producción se deben configurar `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` y `DATABASE_URL` de forma segura.

**6. Aplicar las migraciones**

```bash
python manage.py migrate
```

**7. Ejecutar el servidor**

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Administración

El proyecto incorpora el panel de administración de Django:

https://proyecto2-django-biblioteca.onrender.com/admin/

El acceso requiere una cuenta con permisos de administrador. Las credenciales no se incluyen en el repositorio.

## Pruebas

Ejecutar los tests:

```bash
python manage.py test
```

Comprobar la configuración:

```bash
python manage.py check
```

## Despliegue en Render

La aplicación está desplegada en Render y utiliza PostgreSQL como base de datos de producción.

El proceso de despliegue incluye:

1. Instalación de dependencias desde `requirements.txt`.
2. Recopilación de archivos estáticos mediante `collectstatic`.
3. Aplicación de migraciones de Django.
4. Inicio del servidor mediante Gunicorn.

**Build Command:**

```bash
bash build.sh
```

**Start Command:**

```bash
gunicorn biblioteca.wsgi:application
```

Las credenciales y configuraciones sensibles se gestionan mediante variables de entorno en Render.

## Autor

Proyecto académico desarrollado como parte del Máster en Desarrollo Full Stack de Conquer Blocks.
