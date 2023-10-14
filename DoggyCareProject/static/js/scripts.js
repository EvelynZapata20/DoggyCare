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
