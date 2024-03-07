const imageUpload = document.getElementById('image-upload');
const imagePreview = document.getElementById('image-preview');
imagePreview.innerHTML = `<img id="default-image" src="{% static 'img/profile.gif' %}" alt="Default Image" width="500px" height"500px">`
const defaultImage = document.getElementById('upload-container');
defaultImage.addEventListener('click', function() {
    imageUpload.click();
});

imageUpload.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const img = document.createElement('img');
            img.src = event.target.result;
            imagePreview.innerHTML = '';
            imagePreview.appendChild(img);
        }
        reader.readAsDataURL(file);
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registration-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Reset error messages
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(msg => msg.textContent = '');

        // Fetch form input values
        const firstName = document.getElementById('first-name').value.trim();
        const lastName = document.getElementById('last-name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const address = document.getElementById('address').value.trim();
        const city = document.getElementById('city').value.trim();
        const country = document.getElementById('country').value.trim();
        const postcode = document.getElementById('postcode').value.trim();
        const state = document.getElementById('state').value.trim();
        const pin = document.getElementById('pin').value.trim();

        // Validate numeric inputs
        if (!/^\d+$/.test(phone)) {
            document.getElementById('phone-error').textContent = 'Phone must be numeric';
            return;
        }

        if (!/^\d+$/.test(pin)) {
            document.getElementById('pin-error').textContent = 'PIN must be numeric';
            return;
        }

        // Check if any field is empty
        if (firstName === '' || lastName === '' || email === '' || phone === '' || address === '' || city === '' || country === '' || postcode === '' || state === '' || pin === '') {
            document.getElementById('form-error').textContent = 'Please fill in all fields';
            return;
        }

        // Submit the form if all validations pass
        form.submit();
    });
});

