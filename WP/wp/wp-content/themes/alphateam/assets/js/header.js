document.addEventListener('DOMContentLoaded', function () {
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.getElementById('user-menu');

    if (!userMenuButton || !userMenu) {
        return;
    }

    const closeUserMenu = () => {
        userMenu.classList.add('hidden');
        userMenuButton.setAttribute('aria-expanded', 'false');
    };

    const toggleUserMenu = () => {
        const isOpen = userMenuButton.getAttribute('aria-expanded') === 'true';

        userMenu.classList.toggle('hidden', isOpen);
        userMenuButton.setAttribute('aria-expanded', String(!isOpen));
    };

    userMenuButton.addEventListener('click', function (event) {
        event.stopPropagation();
        toggleUserMenu();
    });

    userMenu.addEventListener('click', function (event) {
        event.stopPropagation();
    });

    document.addEventListener('click', closeUserMenu);

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            closeUserMenu();
        }
    });
});