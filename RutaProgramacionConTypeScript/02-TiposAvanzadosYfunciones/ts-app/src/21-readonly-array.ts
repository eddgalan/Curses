const numbers: ReadonlyArray <number> = [1, 2, 3];
// No se permiten las siguientes mutaciones
/*
numbers.push(4);
numbers.pop();
numbers.unshift(0);
*/

numbers.filter(n => n % 2);
numbers.map(n => console.log(n * 2));
