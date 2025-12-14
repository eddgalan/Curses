const fs = require('fs');

const fileName = 'example.txt';

// Crear archivo
fs.writeFileSync(fileName, 'Hello World!\n');
console.log('File created!');

// Leer archivos
const content = fs.readFileSync(fileName, 'utf-8');
console.log('File Content: ', content);

// Actualizar (Editar, New Line)
fs.appendFileSync(fileName, 'New Line Added!\n');
console.log('File Updated!');

// Eliminar
fs.unlinkSync(fileName);
console.log('File Deleted!');