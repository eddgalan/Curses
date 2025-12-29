(() => {
  // Inferido
  let prices = [100, 200, 300];
  prices.push('asdf');
  prices.push(true);
  prices.push({});

  prices.push(121212);
  console.log('prices: ', prices);

  let prices2 = [100, 200, 300, 'hola', true];
  prices2.push({});
  prices2.push(2);
  console.log('prices2: ', prices2);

  let mixedArray: (number | string | boolean)[] = [100, 'hola', true];
  mixedArray.push(2);
  mixedArray.push({});
  mixedArray.push([]);
  console.log('mixedArray: ', mixedArray);

  let numbers: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  console.log(numbers.map(number => number * 2));

  let numbers_ = [1, 2, '3', 4, 5, 6, 7, '8, 9'];
  console.log(numbers_.map(number => number * 2));
})();
