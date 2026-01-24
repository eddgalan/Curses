import { MyDate } from "./02-class";

const myDate = new MyDate(1999, 7, 10);
console.log('printFormat(): ', myDate.printFormat());
myDate.add(2, 'days');
myDate.add(1, 'months');
console.log('printFormat(): ', myDate.printFormat());

// Accede a las propiedades públicas
//console.log('day: ', myDate.day);
//console.log('month: ', myDate.month);
//console.log('year: ', myDate.year);

