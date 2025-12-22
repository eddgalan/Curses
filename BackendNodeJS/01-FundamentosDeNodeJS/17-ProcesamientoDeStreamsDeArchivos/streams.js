const fs = require('fs');

// Crear un stream de lectura
const readStream = fs.createReadStream('text.txt', {
    encoding: 'utf8'
});

// Crear un stream de escritura
const writeStream = fs.createWriteStream('output-text.txt');

// Evento para procesar cada fragmento de datos
readStream.on('data', (chunk) => {
    console.log('Readings chunk: ');
    writeStream.write(chunk);
});

// Evento cuando finaliza la lectura
readStream.on('end', () => {
    console.log('File read completed.');
    writeStream.end();
});

// Manejo de errores en la lectura
readStream.on('error', (error) => {
    console.log('Read error: ', error);
});

// Manejo de errores en la escritura
writeStream.on('error', (error) => {
    console.log('Error in File Write', error);
});
