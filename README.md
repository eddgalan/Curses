# Curses

Proyecto local de WordPress usando Docker, MariaDB y un tema personalizado llamado **AlphaTeam**.

## Estructura

```text
.
├── README.md
└── WP
    ├── Dockerfile
    ├── docker-compose.yml
    ├── docker/
    └── wp/
        └── wp-content/
            └── themes/
                └── alphateam/
                    ├── 404.php
                    ├── footer.php
                    ├── functions.php
                    ├── header.php
                    ├── index.php
                    ├── screenshot.jpeg
                    └── style.css
```

## Requisitos

- Docker
- Docker Compose

## Levantar el proyecto

El archivo principal de Docker esta en `WP/docker-compose.yml`.

```bash
cd WP
docker compose up -d --build
```

El sitio queda disponible en:

```text
http://localhost:8086
```

La base de datos MariaDB queda expuesta en el puerto:

```text
3308
```

Credenciales locales configuradas:

```text
Database: wordpress
User: root
Password: 12345678a
Host: mariadb
```

## Red de Docker

El `docker-compose.yml` usa una red externa llamada `wordpress-network`. Si no existe, creala antes de levantar los contenedores:

```bash
docker network create wordpress-network
```

Luego ejecuta:

```bash
cd WP
docker compose up -d --build
```

## Tema AlphaTeam

El tema personalizado esta en:

```text
WP/wp/wp-content/themes/alphateam
```

Archivos principales:

- `header.php`: estructura del header, menu principal y submenu de usuario.
- `footer.php`: footer del sitio.
- `index.php`: plantilla base para renderizar entradas/paginas.
- `404.php`: pagina personalizada para rutas no encontradas.
- `functions.php`: carga estilos y scripts del tema.
- `style.css`: metadatos del tema para WordPress.

El tema usa clases de TailwindCSS. Actualmente Tailwind se carga desde CDN.

## Comandos utiles

Levantar contenedores:

```bash
cd WP
docker compose up -d
```

Detener contenedores:

```bash
cd WP
docker compose down
```

Ver logs de WordPress:

```bash
cd WP
docker compose logs -f wordpress
```

Ver logs de MariaDB:

```bash
cd WP
docker compose logs -f mariadb
```

Entrar al contenedor de WordPress:

```bash
cd WP
docker compose exec wordpress bash
```

Entrar a MariaDB:

```bash
cd WP
docker compose exec mariadb mariadb -uroot -p12345678a wordpress
```

Validar sintaxis PHP de un archivo:

```bash
php -l WP/wp/wp-content/themes/alphateam/header.php
```

## Notas

- El contenedor de WordPress usa PHP 8.4 con Apache.
- El Dockerfile instala extensiones comunes para WordPress como `mysqli`, `pdo_mysql`, `gd`, `intl`, `zip` y `exif`.
- Xdebug se instala porque `INSTALL_XDEBUG` esta configurado como `true` en `docker-compose.yml`.
- `functions.php` referencia `assets/js/header.js`; si se necesita JavaScript del header en archivo separado, crea ese archivo dentro del tema o ajusta la ruta.
