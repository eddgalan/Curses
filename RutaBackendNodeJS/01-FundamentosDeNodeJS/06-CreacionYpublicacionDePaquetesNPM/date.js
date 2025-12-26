const dateFormatter = require('platzidate');

console.log('Timestamp: ', dateFormatter.getTimestamp());
console.log('Fecha en español: ', dateFormatter.getLongTime());
console.log('Fecha en inglés: ', dateFormatter.getLongTime('en-US'));
