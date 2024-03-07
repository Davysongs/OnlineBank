
const form = document.getElementById('form')
document.addEventListener('DOMContentLoaded', function() {

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Reset error messages
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(msg => msg.textContent = '');

        // Fetch form input values
        const firstName = document.getElementById('first_name').value.trim();
        const lastName = document.getElementById('last_name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const address = document.getElementById('address').value.trim();
        const city = document.getElementById('city').value.trim();
        const country = document.getElementById('country').value.trim();
        const postcode = document.getElementById('postcode').value.trim();
        const state = document.getElementById('state').value.trim();
        const pin1 = document.getElementById('pin1').value.trim();
        const pin2 = document.getElementById('pin2').value.trim();
        var pinError = document.getElementById('pin-error')

        // Validate numeric inputs
        if (!/^\d+$/.test(phone))  {
            document.getElementById('phone-error').textContent = 'Phone must be numeric';
            return;
        }

        if (!/^\d+$/.test(pin1)|| !/^\d+$/.test(pin2)) {
            pinError.textContent = 'PIN must be numeric';
            return;
        }

        // Check if pin1 and pin2 values match
        if (pin1 !== pin2) {
            // Show error message
            pinError.textContent = 'PINs do not match';
            return;
        } else {
            // Clear error message if values match
            pinError.textContent = '';
        }

        // Check if any field is empty
        if (firstName === '' || lastName === '' || email === '' || phone === '' || address === '' || city === '' || country === '' || postcode === '' || state === '' || pin === '') {
            document.getElementById('form-error').textContent = 'Please fill in all fields';
            return;
        }
        const imageUpload = document.getElementById('image-upload');
        const imagePreview = document.getElementById('image-preview');
        const errorMessage = document.getElementById('upload-error');

        // Reset previous error messages
        errorMessage.textContent = '';

        // Check if a file has been selected
        if (!imageUpload.files || !imageUpload.files[0]) {
            errorMessage.textContent = 'Please select an image';
            event.preventDefault(); // Prevent form submission
        } else {
            // Check if the file type is valid
            const fileType = imageUpload.files[0].type;
            if (!fileType.startsWith('image/')) {
                errorMessage.textContent = 'Please select a valid image file';
                event.preventDefault(); // Prevent form submission
            } else {
                // Optionally, you can display a preview of the selected image
                const file = imageUpload.files[0];
                const reader = new FileReader();

                reader.onload = function(e) {
                    imagePreview.innerHTML = `<img src="${e.target.result}" alt="Image Preview">`;
                };

                reader.readAsDataURL(file);
            }
        }

        // Submit the form if all validations pass
        form.submit();
    });
});

