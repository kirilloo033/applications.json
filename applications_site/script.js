document.addEventListener('DOMContentLoaded', function() {
    const contactMethodSelect = document.getElementById('contactMethod');
    const phoneField = document.getElementById('phoneField');
    const emailField = document.getElementById('emailField');
    const telegramField = document.getElementById('telegramField');
    const applicationForm = document.getElementById('applicationForm');
    const successMessage = document.getElementById('successMessage');
    const errorMessage = document.getElementById('errorMessage');


    contactMethodSelect.addEventListener('change', function() {
        phoneField.style.display = 'none';
        emailField.style.display = 'none';
        telegramField.style.display = 'none';

        if (this.value === 'phone') {
            phoneField.style.display = 'block';
        } else if (this.value === 'email') {
            emailField.style.display = 'block';
        } else if (this.value === 'telegram') {
            telegramField.style.display = 'block';
        }
    });

    applicationForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Отправка данных на сервер (замените на ваш URL)
        fetch('YOUR_BACKEND_ENDPOINT', {  // Замените на URL вашего backend
            method: 'POST',
            body: new FormData(applicationForm) // Отправляем данные формы
        })
        .then(response => {
            if (response.ok) {
                successMessage.style.display = 'block';
                errorMessage.style.display = 'none';
                applicationForm.reset(); // Очищаем форму
                phoneField.style.display = 'none';
                emailField.style.display = 'none';
                telegramField.style.display = 'none';
            } else {
                throw new Error('Network response was not ok');
            }
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            errorMessage.style.display = 'block';
            successMessage.style.display = 'none';
        });

    });


});
