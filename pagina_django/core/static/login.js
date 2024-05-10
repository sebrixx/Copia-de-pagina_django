function validar() {
    var correoElectronico = document.getElementById("gmail").value;
    var contraseña = document.getElementById("contraseña").value;
  
    // Verificar si el campo de correo electrónico tiene una dirección de correo electrónico válida
    if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(correoElectronico)) {
      alert("Ingrese una dirección de correo electrónico válida.");
      return false;
    }
  
    // Verificar si el campo de contraseña está vacío
    if (contraseña == "") {
      alert("Ingrese una contraseña.");
      return false;
    }

    location.href ="login.html";
    alert("Ha iniciado secccion")
    return true;
  
    // Si todo está bien, permitir el envío del formulario
    return true;

    
  }