const headerBurger = document.querySelector('#js-header-burger');
const headerMenu = document.querySelector('#js-header-menu');

const onBurgerClickCallback = () => {
    headerMenu.classList.toggle('hidden');
};

const headerNav = () => {
    headerBurger.addEventListener('click', onBurgerClickCallback);
};

headerNav();
