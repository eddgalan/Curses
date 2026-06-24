# Práctica de Tailwind CSS con Astro

Proyecto de aprendizaje creado para practicar **Tailwind CSS 4** dentro de una aplicación de **Astro**. Incluye páginas de autenticación y contacto, ejemplos de diseño responsive, formularios estilizados y un blog basado en contenido Markdown y MDX.

El proyecto parte del starter de blog de Astro, pero incorpora distintas interfaces construidas principalmente con clases de utilidad de Tailwind CSS.

## Objetivos de aprendizaje

- Construir interfaces mediante clases de utilidad.
- Practicar layouts con Flexbox y CSS Grid.
- Crear diseños adaptables con los breakpoints de Tailwind.
- Aplicar estados interactivos como `hover`, `focus` y variantes de modo oscuro.
- Estilizar controles de formulario con `@tailwindcss/forms`.
- Dar formato a contenido HTML y Markdown con `@tailwindcss/typography`.
- Integrar Tailwind CSS 4 con Astro mediante el plugin de Vite.
- Reutilizar componentes y layouts de Astro.

## Tecnologías

- [Astro 7](https://astro.build/)
- [Tailwind CSS 4](https://tailwindcss.com/)
- [Tailwind CSS Forms](https://github.com/tailwindlabs/tailwindcss-forms)
- [Tailwind CSS Typography](https://github.com/tailwindlabs/tailwindcss-typography)
- [MDX](https://mdxjs.com/)
- TypeScript

## Páginas disponibles

| Ruta | Descripción |
| --- | --- |
| `/` | Página inicial proveniente del starter de Astro. |
| `/about` | Ejemplo extenso de contenido tipográfico usando la clase `prose`. |
| `/contact` | Formulario de contacto responsive con campos, textarea, botón e iframe. |
| `/login` | Interfaz de inicio de sesión con estados de foco y enlace al registro. |
| `/register` | Formulario de registro organizado con Grid y breakpoints responsive. |
| `/blog` | Listado de publicaciones obtenidas desde una colección de contenido. |
| `/blog/[slug]` | Página generada para cada entrada Markdown o MDX. |
| `/rss.xml` | Feed RSS generado a partir de las publicaciones. |

## Prácticas de Tailwind incluidas

### Diseño responsive

Las páginas utilizan modificadores como `sm:`, `md:` y `lg:` para adaptar el espaciado, las columnas, la navegación y el ancho de los elementos según el tamaño de pantalla.

### Flexbox y Grid

Se usan utilidades como `flex`, `grid`, `place-items-center`, `md:grid-cols-2`, `items-center` y `justify-between` para construir la cabecera y distribuir los formularios.

### Formularios

El plugin `@tailwindcss/forms` normaliza los controles y permite trabajar con clases como `form-input`, `form-textarea` y `form-checkbox`. Los campos incluyen ejemplos de bordes, colores, placeholders y estados de foco.

### Tipografía

El plugin `@tailwindcss/typography` proporciona la clase `prose`, utilizada en la página `/about` para dar formato a encabezados, párrafos, listas, citas, imágenes y bloques de código.

### Estados y variantes

Los componentes incluyen ejemplos de:

- `hover:` para enlaces y botones.
- `focus:` y `focus:ring-*` para controles accesibles.
- `transition` para suavizar cambios visuales.
- `dark:` en la cabecera.
- Valores arbitrarios como `min-h-[calc(100vh-4rem)]` y `bg-[url(...)]`.

### Tema personalizado

El archivo `src/styles/global.css` importa Tailwind y registra sus plugins. También contiene tokens personalizados mediante `@theme`:

```css
@import "tailwindcss";
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/typography";

@theme {
  --color-primary-light: #6028D9;
  --color-primary-dark: #2E1065;
  --font-heading: "Ubuntu", sans-serif;
  --font-body: "Inter", sans-serif;
}
```

## Estructura del proyecto

```text
astro-app/
├── public/                 # Archivos públicos y favicons
├── src/
│   ├── assets/             # Imágenes y fuentes locales
│   ├── components/         # Cabecera, pie, metadatos y utilidades
│   ├── content/blog/       # Publicaciones Markdown y MDX
│   ├── layouts/            # Layout de las entradas del blog
│   ├── pages/              # Rutas de la aplicación
│   ├── styles/global.css   # Tailwind, plugins y tema
│   ├── consts.ts           # Título y descripción globales
│   └── content.config.ts   # Esquema de la colección del blog
├── astro.config.mjs        # Astro, MDX, sitemap, fuentes y Tailwind
├── package.json
└── tsconfig.json
```

## Requisitos

- Node.js `22.12.0` o una versión posterior.
- npm.

## Instalación

Desde la carpeta `astro-app`:

```bash
npm install
npm run dev
```

El servidor de desarrollo estará disponible, de forma predeterminada, en `http://localhost:4321`.

## Comandos

| Comando | Acción |
| --- | --- |
| `npm run dev` | Inicia el servidor de desarrollo. |
| `npm run build` | Genera la versión de producción en `dist/`. |
| `npm run preview` | Sirve localmente la compilación de producción. |
| `npm run astro -- --help` | Muestra la ayuda de la CLI de Astro. |

## Contenido del blog

Las publicaciones se encuentran en `src/content/blog/` y aceptan archivos `.md` y `.mdx`. Su frontmatter se valida con el siguiente esquema:

```yaml
title: Título de la publicación
description: Descripción breve
pubDate: 2026-01-01
updatedDate: 2026-01-02 # Opcional
heroImage: ../../assets/imagen.jpg # Opcional
```

Astro genera las rutas estáticas de cada publicación y utiliza esos mismos datos para crear el listado del blog, los metadatos y el feed RSS.

## Estado actual y limitaciones

Este repositorio es una práctica de maquetación, no una aplicación terminada:

- Los formularios usan `action="#"` y no envían información a un backend.
- El botón del menú móvil es únicamente visual y todavía no implementa apertura o cierre.
- Las variantes `dark:` de la cabecera están definidas, pero no existe un selector de tema.
- La página `/about` referencia `/img/beams.jpg` y `/img/grid.svg`, archivos que no están presentes en `public/`.
- `site` conserva el valor de ejemplo `https://example.com` en `astro.config.mjs`; debe cambiarse antes de publicar para generar URLs canónicas, sitemap y RSS correctos.
- Parte del contenido y de los estilos del blog todavía pertenece al starter original de Astro.

## Créditos

La base del blog proviene del [Astro Blog Starter](https://github.com/withastro/astro/tree/main/examples/blog), cuyo tema está inspirado en [Bear Blog](https://github.com/HermanMartinus/bearblog).
