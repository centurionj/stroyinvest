const activeSelectors = ['!bg-blue1', 'hover:!bg-blue1-hover', 'text-white'];

const navSelectorsEnums = {
    index: '#js-index',
    products: '#js-products',
    service: '#js-services',
    news: '#js-news',
    contacts: '#js-contacts',
    'about-us': '#js-about-us',
    documents: '#js-documents',
};

const linksEnums = {
    '/': 'index',
    '/products': 'products',
    '/products/': 'products',
    '/service': 'service',
    '/service/': 'service',
    '/news': 'news',
    '/news/': 'news',
    '/contacts': 'contacts',
    '/contacts/': 'contacts',
    '/about-us': 'about-us',
    '/about-us/': 'about-us',
    '/documents': 'documents',
    '/documents/': 'documents',
};

const setActiveNav = () => {
    const currentPath = window.location.pathname;

    const navName = linksEnums[currentPath];

    if (!navName) return;

    const navSelector = navSelectorsEnums[navName];

    const nav = document.querySelector(navSelector);

    activeSelectors.map(activeSelector => {
        nav.classList.add(activeSelector);
    });
};

setActiveNav();