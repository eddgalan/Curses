// Count
console.count('contador');
console.count('contador');
console.count('contador');
console.count('contador');
console.countReset('contador');
console.count('contador');
console.count('contador');

// Agrupación
console.group('Grupo 1');
console.log('Hola');
console.log('Mundo');
console.group('Grupo 2');
console.log('Hola');
console.groupEnd();

// Afirmaciones
console.assert(1 === 1, '1 es igual a 1. Esto no se mostrará');
console.assert(1 === 2, 'Esto SÍ se mostrará');

// Crear
console.clear();

console.trace('Pila de llamadas');
