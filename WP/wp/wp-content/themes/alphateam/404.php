<?php get_header(); ?>

<main class="flex-1 bg-white dark:bg-gray-950">
    <section class="mx-auto flex min-h-[calc(100vh-26rem)] max-w-5xl items-center px-4 py-20 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-2xl text-center">
            <p class="text-sm font-semibold uppercase tracking-[0.25em] text-teal-600 dark:text-teal-300">
                Error 404
            </p>

            <h1 class="mt-4 text-5xl font-semibold text-gray-950 dark:text-white sm:text-7xl">
                Pagina no encontrada
            </h1>

            <p class="mx-auto mt-6 max-w-xl text-base leading-7 text-gray-600 dark:text-gray-400">
                La ruta que abriste no existe o fue movida.
            </p>

            <div class="mt-8 flex flex-col items-center justify-center gap-3 sm:flex-row">
                <a
                    href="<?php echo esc_url( home_url( '/' ) ); ?>"
                    class="inline-flex min-h-11 items-center justify-center rounded-md bg-gray-950 px-5 text-sm font-semibold text-white transition hover:bg-gray-800 dark:bg-white dark:text-gray-950 dark:hover:bg-gray-200"
                >
                    Volver al inicio
                </a>

                <a
                    href="<?php echo esc_url( get_permalink( get_option( 'page_for_posts' ) ) ?: home_url( '/' ) ); ?>"
                    class="inline-flex min-h-11 items-center justify-center rounded-md border border-gray-200 px-5 text-sm font-semibold text-gray-700 transition hover:border-gray-300 hover:bg-gray-50 dark:border-gray-800 dark:text-gray-300 dark:hover:border-gray-700 dark:hover:bg-gray-900"
                >
                    Ver publicaciones
                </a>
            </div>
        </div>
    </section>
</main>

<?php get_footer(); ?>
