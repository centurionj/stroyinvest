function submitForm() {
    const form = document.getElementById('filterForm');
    const checkboxes = form.querySelectorAll('input[name="productTypes"]:checked');
    const productTypes = Array.from(checkboxes).map(checkbox => checkbox.value).join(',');

    const sortSelect = document.getElementById('sortSelect');
    const sortValue = sortSelect.value;

    const queryParams = `?productTypes=${productTypes}&sort=${sortValue}`;
    const url = window.location.pathname + queryParams;

    window.location.href = url;
}

// Функция для получения значения параметра из URL
function getQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Функция для установки состояния чекбоксов и сортировки
function setInitialState() {
    const form = document.getElementById('filterForm');

    // Восстановление состояния чекбоксов
    const productTypesParam = getQueryParam('productTypes');
    if (productTypesParam) {
        const productTypes = productTypesParam.split(',');
        productTypes.forEach(type => {
            const checkbox = form.querySelector(`input[name="productTypes"][value="${type}"]`);
            if (checkbox) {
                checkbox.checked = true;
            }
        });
    }

    // Восстановление состояния сортировки
    const sortParam = getQueryParam('sort');
    if (sortParam) {
        const sortSelect = document.getElementById('sortSelect');
        sortSelect.value = sortParam;
    }
}

// Функция для сохранения состояния чекбоксов и сортировки в localStorage
function saveState() {
    const form = document.getElementById('filterForm');
    const checkboxes = form.querySelectorAll('input[name="productTypes"]:checked');
    const productTypes = Array.from(checkboxes).map(checkbox => checkbox.value);

    const sortSelect = document.getElementById('sortSelect');
    const sortValue = sortSelect.value;

    // Сохранение в localStorage
    localStorage.setItem('productTypes', JSON.stringify(productTypes));
    localStorage.setItem('sortValue', sortValue);
}

// Функция для загрузки состояния чекбоксов и сортировки из localStorage
function loadState() {
    const productTypes = JSON.parse(localStorage.getItem('productTypes')) || [];
    const sortValue = localStorage.getItem('sortValue');

    const form = document.getElementById('filterForm');

    // Восстановление состояния чекбоксов
    productTypes.forEach(type => {
        const checkbox = form.querySelector(`input[name="productTypes"][value="${type}"]`);
        if (checkbox) {
            checkbox.checked = true;
        }
    });

    // Восстановление состояния сортировки
    const sortSelect = document.getElementById('sortSelect');
    if (sortValue) {
        sortSelect.value = sortValue;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    setInitialState(); // Установка начального состояния при загрузке страницы
    loadState(); // Загрузка сохраненного состояния из localStorage

    // Обработка события отправки формы
    const form = document.getElementById('filterForm');
    form.addEventListener('submit', function () {
        saveState(); // Сохранение состояния перед отправкой формы
    });

    // Обработка события изменения значения сортировки
    const sortSelect = document.getElementById('sortSelect');
    sortSelect.addEventListener('change', function () {
        submitForm(); // Вызов submitForm при изменении значения сортировки
    });
});