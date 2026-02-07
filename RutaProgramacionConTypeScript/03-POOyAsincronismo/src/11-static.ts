console.log('Pi: ', Math.PI);
console.log('Max: ', Math.max(1,2,3));

class MyMath {
  static readonly PI = 3.14;

  static firstValue (... numbers: number[]) {
    return numbers[0];
  }

  static max (... numbers: number[]) {
    return numbers.reduce((max, item) => max >= item ? max: item, 0);
  }
}

console.log('MyMath Pi: ', MyMath.PI);
console.log('MyMath First: ', MyMath.firstValue(1,2,3));

const numbers = [1,2,3, 10,12,7];
console.log('MyMath Max: ', MyMath.max(...numbers));
