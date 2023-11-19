const archivo = document.getElementById("archivo");
const subir = document.getElementById("subir");

subir.addEventListener("click", () => {
  const archivos = archivo.files;

  // Validar archivos
  if (archivos.length === 0) {
    alert("Debe seleccionar al menos un archivo");
    return;
  }

  // Subir archivos
  // ...
});
