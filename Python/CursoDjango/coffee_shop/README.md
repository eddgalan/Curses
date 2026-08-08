# Coffee Shop

Coffee Shop es una aplicación web de ejemplo construida con Django para gestionar
un catálogo de productos, cuentas de clientes y órdenes de compra. Los usuarios
pueden consultar los productos disponibles, registrarse, iniciar sesión, agregar
productos a una cotización (el carrito) y revisar el historial y detalle de sus
órdenes.

El proyecto utiliza PostgreSQL como base de datos. En el entorno de desarrollo,
PostgreSQL se ejecuta dentro de Docker y la aplicación Django se ejecuta
localmente.

## Funcionalidades principales

- Catálogo web de productos con nombre, descripción, precio, disponibilidad e
  imagen opcional.
- Endpoint REST de solo lectura para consultar productos.
- Registro, inicio y cierre de sesión de usuarios.
- Carrito asociado al usuario autenticado mediante una orden en estado `quote`.
- Incremento automático de la cantidad al agregar nuevamente el mismo producto.
- Cálculo del subtotal por producto y del total de la orden.
- Historial de órdenes separado del carrito activo.
- Detalle de órdenes protegido para que cada usuario solo pueda consultar sus
  propias órdenes.
- Panel de administración de Django.
- Suite automatizada de pruebas para modelos, formularios, vistas, autenticación,
  API y restricciones de base de datos.

## Apps del proyecto

### `products`

Administra el catálogo de la tienda.

- Modelo `Product`.
- Listado de productos en la página principal.
- Formulario para crear productos.
- API JSON disponible en `/api/`.
- Soporte para imágenes mediante Pillow.

### `users`

Contiene el flujo de autenticación basado en el modelo `User` incluido en Django.

- Registro de clientes en `/users/register/`.
- Inicio de sesión en `/users/login/`.
- Cierre de sesión mediante una petición `POST` a `/users/logout/`.
- Formularios personalizados para registro e inicio de sesión.

### `orders`

Gestiona el carrito y las órdenes de cada cliente.

- Una orden puede tener los estados `quote`, `pending`, `processing`, `completed`
  o `cancelled`.
- Cada usuario puede tener como máximo una orden en estado `quote`.
- Un producto solo puede aparecer una vez dentro de una orden; al agregarlo otra
  vez se incrementa su cantidad.
- El carrito, historial y detalle requieren autenticación.
- Los productos asociados a una orden están protegidos contra eliminación.

## Tecnologías

- Python 3.13 o posterior.
- Django 6.0.
- PostgreSQL 18.
- Docker y Docker Compose.
- Django REST Framework.
- django-environ.
- django-crispy-forms y crispy-tailwind.
- Pillow.
- psycopg2-binary.

Las versiones concretas se encuentran en `requirements.txt` y las herramientas
opcionales de desarrollo en `requirements-dev.txt`.

## Requerimientos previos

Antes de instalar el proyecto necesitas:

- Python 3.13+ y `pip`.
- Docker Desktop, Docker Engine o una instalación equivalente con el comando
  `docker compose`.
- Git, si vas a clonar el repositorio.

Los siguientes pasos deben ejecutarse desde este directorio:

```text
Python/CursoDjango/coffee_shop
```

## Instalación

### 1. Crear y activar un entorno virtual

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Instalar las dependencias

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para instalar también las herramientas opcionales de desarrollo:

```bash
python -m pip install -r requirements-dev.txt
```

### 3. Configurar las variables de entorno

Crea el archivo `.env` a partir del ejemplo incluido:

```bash
cp .env.example .env
```

En Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

La configuración incluida espera los siguientes valores:

```dotenv
DJANGO_DB_NAME=coffee_shop
DJANGO_DB_HOST=localhost
DJANGO_DB_PORT=5432
DJANGO_DB_USER=coffee_shop
DJANGO_DB_PASSWORD=12345678a
```

Estos datos coinciden con el servicio definido en `docker-compose.yml`. Si los
cambias, actualiza ambos archivos para que sigan coincidiendo. El archivo `.env`
está ignorado por Git y no debe contener credenciales de producción.

### 4. Iniciar PostgreSQL con Docker

```bash
docker compose up -d
docker compose ps
```

El contenedor se llama `coffee_shop_postgres`, publica PostgreSQL en el puerto
local `5432` y conserva sus datos en el volumen `postgres_data`.

Puedes consultar sus logs con:

```bash
docker compose logs -f postgres
```

### 5. Preparar la base de datos

```bash
python manage.py migrate
```

Opcionalmente, crea un usuario administrador:

```bash
python manage.py createsuperuser
```

### 6. Ejecutar la aplicación

```bash
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> en el navegador.

## Rutas principales

| Ruta | Descripción | Autenticación |
| --- | --- | --- |
| `/` | Catálogo de productos | No |
| `/create/` | Creación de productos | No |
| `/api/` | Listado JSON de productos | No |
| `/users/register/` | Registro | No |
| `/users/login/` | Inicio de sesión | No |
| `/users/logout/` | Cierre de sesión mediante `POST` | Sí |
| `/orders/cart/` | Carrito u orden `quote` actual | Sí |
| `/orders/orders_list/` | Historial de órdenes | Sí |
| `/orders/order_details/<id>/` | Detalle de una orden propia | Sí |
| `/admin/` | Administración de Django | Staff |

La acción `/orders/add_product/` recibe peticiones `POST` desde el catálogo y
requiere que el usuario haya iniciado sesión.

## Ejecutar las pruebas

Con PostgreSQL iniciado y el entorno virtual activo:

```bash
python manage.py test
```

También puedes ejecutar una app específica:

```bash
python manage.py test products
python manage.py test users
python manage.py test orders
```

Django crea y elimina una base de datos temporal durante la ejecución. El usuario
de PostgreSQL configurado debe tener permisos para crear esa base de pruebas.

## Comandos útiles

Crear migraciones después de modificar los modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

Comprobar la configuración del proyecto:

```bash
python manage.py check
```

Detener PostgreSQL sin eliminar sus datos:

```bash
docker compose down
```

Para eliminar también el volumen y todos los datos locales se puede usar
`docker compose down -v`. Esta operación es destructiva y no se puede deshacer.

## Estructura resumida

```text
coffee_shop/
├── coffee_shop/       # Configuración y URLs principales
├── products/          # Catálogo y API de productos
├── users/             # Registro y autenticación
├── orders/            # Carrito, órdenes y sus productos
├── templates/         # Templates compartidos
├── docker-compose.yml # PostgreSQL para desarrollo
├── requirements.txt   # Dependencias de ejecución
└── manage.py          # Utilidad de administración de Django
```

## Consideraciones de desarrollo

- La configuración actual tiene `DEBUG = True` y una `SECRET_KEY` de desarrollo;
  no debe utilizarse sin cambios en producción.
- La creación de productos está expuesta públicamente en el estado actual del
  proyecto. En producción conviene restringirla a usuarios administradores.
- La API de productos es pública y de solo lectura.
- Las credenciales de `docker-compose.yml` están pensadas únicamente para el
  entorno local.
- Antes de desplegar se deben configurar `ALLOWED_HOSTS`, archivos estáticos y
  multimedia, HTTPS y secretos mediante variables de entorno.
