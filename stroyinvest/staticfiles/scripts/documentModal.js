const documentModal = document.querySelector('#documentModal');
const modalOverlay = document.querySelector('#modalOverlay');
const documentModalTitle = document.querySelector('#documentModalTitle');
const documentModalImage = document.querySelector('#documentModalImage');
const modalCloseBtn = document.querySelector('#modalCloseBtn');

const openDocumentModal = (obj) => {
    const { imageSrc, title } = obj.dataset;

    documentModal.classList.remove('hidden');
    documentModalTitle.innerHTML = title;
    documentModalImage.setAttribute('src', imageSrc);
};

modalOverlay.addEventListener('click', () => {
    documentModal.classList.add('hidden');
})
modalCloseBtn.addEventListener('click', () => {
    documentModal.classList.add('hidden');
})