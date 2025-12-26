const { Buffer } = require('buffer');

const bufferFromString = Buffer.from('Hello World!', 'utf-8');
console.log(bufferFromString);

// Crear un buffer de cierto tamaño
const bufferAlloc = Buffer.alloc(10);       // El tamaño de este buffer es de 10 bytes
console.log('Create buffer: ', bufferAlloc);

// Escribir datos dentro de un bloque
bufferAlloc.write('Node.js');
console.log('Write buffer: ', bufferAlloc);

// Leer datos del buffer y construir una cadena
const bufferToString = bufferAlloc.toString('utf-8', 0, 5);
console.log('Read buffer to string: ', bufferToString);
