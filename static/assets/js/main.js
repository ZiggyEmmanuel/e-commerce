// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    var dropbtn = document.querySelector('.dropbtn');
    var dropdownContent = document.querySelector('.dropdown-content');

    dropbtn.addEventListener('click', function() {
        dropdownContent.classList.toggle('show');
    });

    window.addEventListener('click', function(event) {
        if (!event.target.matches('.dropbtn')) {
            if (dropdownContent.classList.contains('show')) {
                dropdownContent.classList.remove('show');
            }
        }
    });
});
