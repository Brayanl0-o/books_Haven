document.addEventListener('DOMContentLoaded', function() {
    console.log('execute script modal');
    var showResults = document.getElementsByClassName('show-results');
    var isOverflowHidden = false;
    var body = document.body;
    for (var i = 0; i < showResults.length; i++) {
        showResults[i].addEventListener('click', function() {
            var resultsModal = document.getElementById('results');
            resultsModal.style.display = (resultsModal.style.display === 'none') ? 'block' : 'none';
       
            this.classList.toggle('active');

            body.style.overflow = isOverflowHidden ? 'hidden' : 'visible';

            // Invertir el estado
            isOverflowHidden = !isOverflowHidden;
        });
    }
});

