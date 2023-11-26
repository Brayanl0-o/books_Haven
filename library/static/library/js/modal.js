document.addEventListener("DOMContentLoaded", function () {
    // Obtener elementos del DOM
    var openModalBtn = document.getElementById("openModalBtn");
    var deleteModalBtn = document.getElementById("deleteModalBtn"); 
    var closeModalBtn = document.getElementById("closeModalBtn");
    var modal = document.getElementById("confirmDeleteModal");

    // Mostrar el modal al hacer clic en el botón
    openModalBtn.addEventListener("click", function () {
        modal.style.display = "flex";
    });

    // Cerrar el modal al hacer clic en el botón de cerrar
    closeModalBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    // Cerrar el modal al hacer clic fuera del contenido del modal
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});

