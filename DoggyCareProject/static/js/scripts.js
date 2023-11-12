$(document).ready(function() {
    // Get the field to upload a image and the selected image
    const imageInput = $('#id_image');
    const selectedImage = $('#selected-image');

    // Create the event when the user selects a image
    imageInput.on('change', function() {
        const input = this;
        if (input.files && input.files[0]) {
            const reader = new FileReader();

            reader.onload = function(e) {
                selectedImage.attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    });
})

// Event for the delete button to show a confirmation message
document.addEventListener("DOMContentLoaded", function () {
    const deleteButton = document.getElementById("delete-button");
    const deleteForm = document.getElementById("delete-form");

    deleteButton.addEventListener("click", function () {
        const confirmation = confirm("Are you sure you want to delete this?");
        if (confirmation) {
            deleteForm.submit();
        }
    });
});


// Event for the star rating
const starRating = document.querySelectorAll('.star-rating input');
starRating.forEach(input => {
    input.addEventListener('mouseenter', function () {
        input.parentNode.querySelectorAll('label').forEach((label, index) => {
            label.style.color = index < this.value ? '#FFD700' : '#ddd';
        });
    });

    input.addEventListener('mouseleave', function () {
        input.parentNode.querySelectorAll('label').forEach(label => {
            label.style.color = label.previousElementSibling && label.previousElementSibling.checked ? '#FFD700' : '#ddd';
        });
    });
});
