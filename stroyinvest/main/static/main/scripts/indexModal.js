function openModal() {
    document.getElementById('myModal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('myModal').classList.add('hidden');
}

function getFormData() {
    return {
        name: document.querySelector('#name').value,
        phone: document.querySelector('#phone').value,
        email: document.querySelector('#email').value,
        message: document.querySelector('#message').value,
    };
}

function submitForm() {
    const data = getFormData();

    const hasErrors = formValidation(data);

    if (hasErrors) return;

    const url = '/customers/api/v1/question/create/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            return response.json().then(json => ({
                status: response.status,
                ok: response.ok,
                json,
            }));
        })
        .then(result => {
            if (!result.ok) {
                Object.keys(result.json).map(fieldName => {
                    document.querySelector(`#${fieldName}`)?.classList?.add('border-red-600');
                    document.querySelector(`#${fieldName}-error`)?.classList?.remove('hidden');
                    document.querySelector(`#${fieldName}-error`)
                        .innerHTML = result.json[fieldName].join('<br>');
                });
            } else {
                document.querySelector('#name').value = '';
                document.querySelector('#phone').value = '';
                document.querySelector('#email').value = '';
                document.querySelector('#message').value = '';
                document.querySelector('#js-form-success-message').classList.remove('hidden');
            }
        })
        .catch(error => {
            console.error('Error:', error.message);
        });
}

function formValidation(data) {
    let hasErrors = false;
    const fields = ['name', 'phone', 'email', 'message'];

    for (const filedIndex in fields) {
        if (!data[fields[filedIndex]]) {
            hasErrors = true;
            document.querySelector(`#${fields[filedIndex]}-error`)?.classList?.remove('hidden');
            document.querySelector(`#${fields[filedIndex]}-error`).innerHTML = 'Это обязательное поле';
            document.querySelector(`#${fields[filedIndex]}`)?.classList?.add('border-red-600');
        } else {
            document.querySelector(`#${fields[filedIndex]}-error`)?.classList?.add('hidden');
            document.querySelector(`#${fields[filedIndex]}`)?.classList?.remove('border-red-600');
        }
    }

    return hasErrors;
}

const indexModal = () => {
    document.getElementById('openModal').addEventListener('click', openModal);
    document.getElementById('modalOverlay').addEventListener('click', closeModal);
    document.getElementById('js-close-modal-button').addEventListener('click', closeModal);
    document.getElementById('js-submit-form').addEventListener('click', submitForm);
    document.querySelector('#name').addEventListener('change', () => {
        formValidation(getFormData());
    });
    document.querySelector('#phone').addEventListener('change', () => {
        formValidation(getFormData());
    });
    document.querySelector('#email').addEventListener('change', () => {
        formValidation(getFormData());
    });
    document.querySelector('#message').addEventListener('change', () => {
        formValidation(getFormData());
    });
};

indexModal();
