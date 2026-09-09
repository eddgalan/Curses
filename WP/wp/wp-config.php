<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '12345678a' );

/** Database hostname */
define( 'DB_HOST', 'wp-mariadb' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '&_Q?/`~,,IIErbmFx*A6E2a8/Bv{5UdmzXAlze2bDaxI3I!vU-iG2<$.WTks&`cn' );
define( 'SECURE_AUTH_KEY',  'hAT>A+!2Vo^9<jcJd RT65HI h_r4PLCdJ/FPVD[MwP{kr8,e<kTUCF$?yiJpm$=' );
define( 'LOGGED_IN_KEY',    'RBO(Wi;c^GAa}4xQL;j,%V<,{7jBlOw2]5!k8f3w%SL-3jQ&[Kcntm/e#?_QUUHU' );
define( 'NONCE_KEY',        '(lc^KFQUomETE[L>$FZ#h[as^Yu*%1H*v`i9Nn6>9@yReMX_xD=h}K*sPLzU3%fq' );
define( 'AUTH_SALT',        '7E,g41*.;AFo.nzR_pL4DumMZY;e$ND(FdNi]9cg.jg{F9tDu>ZL0IJC)/%FdjB4' );
define( 'SECURE_AUTH_SALT', 't[w~sV~ypsZ5I}w71YRsLxxYx3>!,RriG7ATL]v5i3|e@q&w~.cidbm15~DBN9-A' );
define( 'LOGGED_IN_SALT',   '=,_<p$ItEt>| S1fW6W)9s_ITf~!&b=k7yQQ-Ez%.<YTGVYkWAULC eZ1=#j)Hp+' );
define( 'NONCE_SALT',       'hSUxqNf 3A=e4&N E%pmrNg),CbCKZ%wDQXCYD)_$(nW[zDU*$TyVoY5F}aAnLkA' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
