
document.addEventListener('DOMContentLoaded', function() {
    // console.log('execute script modal');
    var showResults = document.getElementsByClassName('show-results');
    var isOverflowHidden = false;
    var body = document.body;

    for (var i = 0; i < showResults.length; i++) {
        showResults[i].addEventListener('click', function() {
            var category = this.textContent.trim();
            var resultsModal = document.getElementById('results');
            resultsModal.style.display = (resultsModal.style.display === 'none') ? 'block' : 'none';

            loadBoooksForCategory(category);

            this.classList.toggle('active');

            body.style.overflow = isOverflowHidden ? 'hidden' : 'visible';

            // Invertir el estado
            isOverflowHidden = !isOverflowHidden;
        });
    }

    function loadBoooksForCategory(category){
        $.ajax({
            type:'GET',
            url: `/book/books-for-category/${category}/`,
            dataType:'json',
            success:function(data){
                // console.log('Datos recibidos:', data);
                updateModalContent(data);
            },
            error:function(error){
                console.error('Error en la solicitud AJAX:', error);
            }
        });
        // console.log('Categoría seleccionada:', category);
    }

    function updateModalContent(data) {
        var modalContainer = document.getElementById('modal-content');
        modalContainer.innerHTML = '';  // Limpiar contenido anterior

        // Crear elementos y agregarlos al contenedor
        var ul = document.createElement('ul');
        ul.className = 'titles';
        
        // Asegúrate de que data.books sea un array
        if (Array.isArray(data.books) && data.books.length > 0) {
            data.books.forEach(function (book) {
                var li = document.createElement('li');
                li.innerHTML = '<h3>' + book.name + '</h3>' +
                            '<p>' + (book.author.name || 'Autor no disponible') + '</p>' +
                            '<p>' + (book.release_date || 'Fecha no disponible') + '</p>';
                ul.appendChild(li);
            });
        } else {
            // Manejar caso de que no haya libros
            var li = document.createElement('li');
            li.innerHTML = '<p>' + 'No hay libros con esa categoría'+ '</p>'
            ul.appendChild(li);
        }

        // Agregar la lista al contenedor del modal
        modalContainer.appendChild(ul);
    }
});

