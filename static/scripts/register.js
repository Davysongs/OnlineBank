
var form_fields = document.getElementsByTagName('input')
const success = document.getElementById("success-msg")
success.style.display= "none"


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('register-form');
    const passwordInput = form.querySelector('input[name="password1"]');
    const confirmPasswordInput = form.querySelector('input[name="password2"]');
    const emailInput = form.querySelector('input[name="email"]');
    const passwordStrength = document.getElementById('password-strength');
    const successMessage = document.getElementById('success-msg');

    successMessage.style.display = 'none';

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const password = passwordInput.value.trim();
        const confirmPassword = confirmPasswordInput.value.trim();
        const email = emailInput.value.trim();

        const errors = [];

        if (password !== confirmPassword) {
            errors.push("Passwords do not match");
        }

        if (password.length < 8) {
            errors.push("Password must be at least 8 characters long");
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            errors.push("Invalid email format");
        }

        if (errors.length > 0) {
            passwordStrength.innerHTML = errors.join("<br>");
            return;
        }

        passwordStrength.innerHTML = '';
        successMessage.style.display = 'block';

        // Optionally, submit the form after a delay
        setTimeout(() => {
            form.submit();
        }, 3000);
    });

    [passwordInput, confirmPasswordInput, emailInput].forEach(input => {
        input.addEventListener('input', function () {
            passwordStrength.innerHTML = '';
        });
    });

    const password = document.querySelector('#password');
    const openEye = document.querySelector('.open-eye');
    const closeEye = document.querySelector('.close-eye');

    closeEye.addEventListener('click', function () {
        password.type = 'text';
        closeEye.style.display = 'none';
        openEye.style.display = 'initial';
    });

    openEye.addEventListener('click', function () {
        password.type = 'password';
        closeEye.style.display = 'initial';
        openEye.style.display = 'none';
    });
});
