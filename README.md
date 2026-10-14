# Biblioteca Digital

Proyecto desarrollado con Django como parte del módulo de Django del Máster en Desarrollo Full Stack.

## Descripción

Esta aplicación permite gestionar una biblioteca digital en la que los usuarios pueden consultar libros, solicitar préstamos, devolver libros, consultar su historial de préstamos y publicar reseñas.

## Funcionalidades

- Registro de usuarios
- Inicio y cierre de sesión
- Listado de libros
- Detalle de cada libro
- Préstamo de libros
- Devolución de libros
- Historial de préstamos por usuario
- Sistema de reseñas y valoraciones

## Modelos principales

- User
- Author
- Book
- Loan
- Review

## Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- SQLite

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar en la carpeta del proyecto:

```bash
cd Proyecto2.Django
```

Crear un entorno virtual:

```bash
python3 -m venv venv
```

Activar el entorno virtual en macOS/Linux:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Migraciones

Aplicar las migraciones de Django:

```bash
python manage.py migrate
```

## Ejecutar el proyecto

Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Después abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Tests

Ejecutar los tests:

```bash
python manage.py test
```

Comprobar que Django no detecta errores de configuración:

```bash
python manage.py check
```

## Autor

Proyecto realizado como ejercicio académico del módulo de Django.