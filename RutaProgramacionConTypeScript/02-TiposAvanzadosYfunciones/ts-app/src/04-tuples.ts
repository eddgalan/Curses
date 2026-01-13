const prices: (string | number)[] = [1, 2, 3];

const user: [string, number] = ['edson', 29];       // Definir una tupla y hacer asignación en una sola línea

let user_: [string, number];                        // Define la tupla
user_ = user;                                       // Hace la asignación (Se asigna la primer tupla a la segunda)
user_ = [12, 'edson'];                              // Asignación erronea, en las tuplas, importa el orden y tamaño

// Desestructuración de tuplas
const [name, age] = user;
console.log(name, age);
