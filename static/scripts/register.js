
var form_fields = document.getElementsByTagName('input')
const success = document.getElementById("success-msg")
success.style.display= "none"
for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}
const form = document.getElementById('register-form');
const passwordInput = form.querySelector('input[name="password1"]');
const confirmPasswordInput = form.querySelector('input[name="password2"]');
const emailInput = form.querySelector('input[name="email"]');
const passwordStrength = document.getElementById('password-strength');

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