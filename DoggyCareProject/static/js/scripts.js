$(document).ready(function() {
    // Obtener el campo de carga de imágenes y la etiqueta de la imagen seleccionada
    const imageInput = $('#id_image');
    const selectedImage = $('#selected-image');

    // Escuchar el evento de cambio en el campo de carga de imágenes
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