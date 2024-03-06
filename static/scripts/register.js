
var form_fields = document.getElementsByTagName('input')
const success = document.getElementById("success-msg")
success.style.display= "none"
for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}
const form = document.getElementById('register-form')
const passwordInput = form.querySelector('input[name="password1"]')
const confirmPasswordInput = form.querySelector('input[name="password2"]')
const emailInput = form.querySelector('input[name="email"]')
const passwordStrength = document.getElementById('password-strength')

form.addEventListener('submit', function (event) {
    let password = passwordInput.value;
    let confirmPassword = confirmPasswordInput.value;
    let email = emailInput.value;
    let errors = [];

    // Check if passwords match
    if (password !== confirmPassword) {
        errors.push("Passwords do not match");
    }

    // Check password strength
    if (password.length < 8) {
        errors.push("Password must be at least 8 characters long");
    }

    // Check if email is valid
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        errors.push("Invalid email format");
    }

    // Display error messages
    if (errors.length > 0) {
        event.preventDefault(); // Prevent form submission
        passwordStrength.innerHTML = errors.join("<br>");
    }
});

// Clear error messages when user interacts with the form
[passwordInput, confirmPasswordInput, emailInput].forEach(input => {
    input.addEventListener('input', function () {
        passwordStrength.innerHTML = '';
    });
});

//password visibility
const password =document.querySelector('#password');
const open_eye = document.querySelector('.open-eye');
const close_eye = document.querySelector('.close-eye');

close_eye.addEventListener('click', function(){
    if(password.type === 'password'){
         password.type = 'text';
         close_eye.style.display = 'none';
         open_eye.style.display = 'initial';
    }
 
 })
 
 open_eye.addEventListener('click', function(){
    if(password.type === 'text'){
         password.type = 'password';
         close_eye.style.display = 'initial';
         open_eye.style.display = 'none';
    }
 
 })


 document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('register-form');

    form.addEventListener('submit', function(event) {
        // Prevent default form submission
        event.preventDefault();

        // Get form input values
        const firstName = document.getElementById('first-name').value.trim();
        const lastName = document.getElementById('last-name').value.trim();
        const email = document.getElementById('email').value.trim();
        const username = document.getElementById('username').value.trim();
        const password1 = document.getElementById('password1').value.trim();
        const password2 = document.getElementById('password2').value.trim();

        // Perform client-side validation
        if (firstName === '' || lastName === '' || email === '' || username === '' || password1 === '' || password2 === '') {
            // Show error message for empty fields
            document.querySelector('.register-error').textContent = 'All fields are required.';
            return; // Prevent further execution
        }

        // If passwords do not match, show error message
        if (password1 !== password2) {
            document.querySelector('.register-error').textContent = 'Passwords do not match.';
            return; // Prevent further execution
        }

        // If all validations pass, submit the form
        form.submit();
    });
});
