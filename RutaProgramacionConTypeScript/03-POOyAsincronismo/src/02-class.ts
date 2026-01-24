const date = new Date();
console.log('hours: ', date.getHours());
console.log('time: ', date.getTime());
console.log('date: ', date.toISOString());

const date2 = new Date(1998, 2, 1998);
console.log('hours: ', date2.getHours());
console.log('time: ', date2.getTime());
console.log('date: ', date2.toISOString());

console.log('date 1: ', date);
console.log('date 2: ', date2);

class MyDate {
  year: number;
  month: number;
  day: number;

  constructor(year: number, month: number, day: number) {
    this.year = year;
    this.month = month;
    this.day = day;
  }
}

const myDate = new MyDate(2026, 1, 15);
console.log('myDate: ', myDate);
