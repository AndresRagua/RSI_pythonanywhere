const $contactForm = document.getElementById('contactForm')
const $name = document.getElementById('name')

(function() {
    
    $contactForm.addEventListener('submit', function(e) {
        let nombre=String($name.value).trim();
        if(nombre.length==0){
            alert("El nombre no puede estar vacio")
            e.preventDefault();
        }
    });

})();