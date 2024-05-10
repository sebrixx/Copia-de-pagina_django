// Seleccionamos los elementos del formulario
const form = document.querySelector('form');
const nameInput = document.querySelector('#name');
const dateInput = document.querySelector('#date');
const emailInput = document.querySelector('#email');
const phoneInput = document.querySelector('#phone');
const addressInput = document.querySelector('#address');
const passwordInput = document.querySelector('#password');
const password2Input = document.querySelector('#password2');
const warnings = document.querySelector('#warnings');

form.addEventListener('submit', (event) => {
  // Cancelamos el evento de envío del formulario para validar los campos primero
  event.preventDefault();

  // Validamos cada campo uno por uno
  function validarNombre(nameinput) {
    if (nameinput.value.trim() === '#name') {
      mostrarAdvertencia(nameinput, 'El nombre es obligatorio');
    } else {
      quitarAdvertencia(nameinput);
    }
  }

  validarNombre(nameInput);

  if (nameInput.value === '') {
    mostrarAdvertencia(nameInput, 'El nombre es obligatorio');
  } else {
    quitarAdvertencia(nameInput);
  }

  if (dateInput.value === '') {
    mostrarAdvertencia(dateInput, 'La fecha de nacimiento es obligatoria');
  } else {
    quitarAdvertencia(dateInput);
  }

  if (emailInput.value.trim() === '') {
    mostrarAdvertencia(emailInput, 'El correo electrónico es obligatorio');
  } else if (!validarEmail(emailInput.value.trim())) {
    mostrarAdvertencia(emailInput, 'El correo electrónico no es válido');
  } else {
    quitarAdvertencia(emailInput);
  }

  if (phoneInput.value.trim() === '') {
    mostrarAdvertencia(phoneInput, 'El número de teléfono es obligatorio');
  } else if (phoneInput.value.trim().length !== 9) {
    mostrarAdvertencia(phoneInput, 'El número de teléfono debe tener 9 dígitos');
  } else {
    quitarAdvertencia(phoneInput);
  }

  if (addressInput.value.trim() === '') {
    mostrarAdvertencia(addressInput, 'La dirección es obligatoria');
  } else {
    quitarAdvertencia(addressInput);
  }

 

  if (password2Input.value.trim() === '') {
    mostrarAdvertencia(password2Input, 'Debe confirmar la contraseña');
  } else if (password2Input.value.trim() !== passwordInput.value.trim()) {
    mostrarAdvertencia(password2Input, 'Las contraseñas no coinciden');
  } else {
    quitarAdvertencia(password2Input);
  }
});

function mostrarAdvertencia(input, mensaje) {
  // Agregamos la clase "error" al elemento padre del input
  input.parentNode.classList.add('error');
  // Mostramos el mensaje de advertencia
  warnings.textContent = 'Datos no validos ';
}

function quitarAdvertencia(input) {
  // Quitamos la clase "error" del elemento padre del input
  input.parentNode.classList.remove('error');
  // Quitamos el mensaje de advertencia
  warnings.textContent = 'error';
}

function validarEmail(email) {
  // Utilizamos una expresión regular para validar el correo electrónico
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}
