/*
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
*/
export class MyDate {
  /*
  private year: number;
  private month: number;
  private day: number;
  */
  readonly initDate: string;      // No se puede modificar ni desde dentro de esta clase

  // El constructor crea las propiedades
  constructor(
    private year: number = 1999,
    private month: number = 1,
    private day: number = 1
  ) {
    this.initDate = this.printFormat();
  }

  printFormat(): string {
    const day = this.addPadding(this.day);
    const month = this.addPadding(this.month);

    return `${day}/${month}/${this.year}`;
  }

  private addPadding(value: number) {
    if (value < 10) {
      return `0${value}`;
    }
    return `${value}`;
  }

  add(amount: number, type: 'days' | 'months' | 'years') {
    if (type === 'days') {
      this.day += amount;
    }
    if (type === 'months') {
      this.month += amount;
    }
    if (type === 'years') {
      this.year += amount;
    }
  }
}
/*
const myDate = new MyDate(2026, 1, 15);
console.log('myDate: ', myDate);
 */
