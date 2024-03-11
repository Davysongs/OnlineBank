document.getElementById('editNickname').addEventListener('click', function() {
    var nicknameInput = document.querySelector('input[name="nickname"]');
    nicknameInput.readOnly = !nicknameInput.readOnly; // Toggle readonly attribute
    nicknameInput.focus(); // Focus on the input field after making it editable
});
document.getElementById('editImageBtn').addEventListener('click', function() {
document.getElementById('imageInput').click();
});

document.getElementById('imageInput').addEventListener('change', function() {
    // Here you can handle the selected image file
    // For example, you can use FormData to send the file to the server via AJAX
    // Or you can display the selected image preview on the page
    const selectedFile = this.files[0];
    if (selectedFile) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const imgPreview = document.querySelector('.card-img-top');
            imgPreview.src = event.target.result;
        };
        reader.readAsDataURL(selectedFile);
    }
});
document.addEventListener('DOMContentLoaded', function() {
const editImageBtn = document.getElementById('editImageBtn');
const imageInput = document.getElementById('imageInput');
const editNicknameBtn = document.getElementById('editNickname');
const nicknameInput = document.querySelector('input[name="nickname"]');
const submitBtn = document.getElementById('submitBtn');

let isImageChanged = false;
let isNicknameChanged = false;

editImageBtn.addEventListener('click', function() {
    imageInput.click();
});

imageInput.addEventListener('change', function() {
    isImageChanged = true;
    toggleSubmitButton();
});

editNicknameBtn.addEventListener('click', function() {
    isNicknameChanged = true;
    toggleSubmitButton();
});

nicknameInput.addEventListener('input', function() {
    isNicknameChanged = true;
    toggleSubmitButton();
});

function toggleSubmitButton() {
    if (isImageChanged || isNicknameChanged) {
        submitBtn.style.display = 'block';
    } else {
        submitBtn.style.display = 'none';
    }
}
});