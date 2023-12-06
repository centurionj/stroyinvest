function openModal() {
    document.getElementById('myModal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('myModal').classList.add('hidden');
}

const indexModal = () => {
    document.getElementById('openModal').addEventListener('click', openModal);
    document.getElementById('modalOverlay').addEventListener('click', closeModal);
    document.getElementById('js-close-modal-button').addEventListener('click', closeModal);
};

indexModal();
