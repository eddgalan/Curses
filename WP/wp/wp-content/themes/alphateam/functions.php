<?php

add_action('wp_enqueue_scripts', 'alphateam_enqueue_scripts');

function alphateam_enqueue_scripts() {
    wp_enqueue_style('alphateam-style', get_stylesheet_directory_uri() . '/style.css');
    wp_enqueue_script('alphateam-script', get_template_directory_uri() . '/assets/js/header.js', [], '1.0', true);
}
