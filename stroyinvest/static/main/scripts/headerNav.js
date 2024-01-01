const headerOpenBurger = document.querySelector('#js-header-open-burger');
const headerCloseBurger = document.querySelector('#js-header-close-burger');
const headerMenu = document.querySelector('#js-header-menu');

const onBurgerClickCallback = () => {
    headerMenu.classList.toggle('hidden');
};

const headerNav = () => {
    headerOpenBurger.addEventListener('click', onBurgerClickCallback);
    headerCloseBurger.addEventListener('click', onBurgerClickCallback);
    document.addEventListener('resize', () => {
        headerMenu.classList.remove('hidden');
    });
};

headerNav();
