// Métodos básicos de salida
console.log('Hello World');
console.info('Console.info(): Similar a console.log() pero para mostrar información');
console.warn('Console.warn(): Similar a console.log() pero para mostrar advertencias');
console.error('Console.error(): Similar a console.log() pero para mostrar errores');

const users = [
    { name: 'John', age: 30 },
    { name: 'Mary', age: 28},
    { name: 'Susan', age: 25},
    { name: 'Jane', age: 24}
];
console.table(users);
console.table(users, ['name']);

//Time
console.time('Operation 1');
for (let i = 0; i < 100000000; i++) {
    // Dummy operation
}
console.timeEnd('Operation 1');
