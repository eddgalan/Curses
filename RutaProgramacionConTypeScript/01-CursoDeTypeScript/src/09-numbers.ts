(() => {
  // Declaración de forma inferida
  let productPrice = 100;
  productPrice = 50;
  console.log('productPrice: ', productPrice);

  // Declaración de forma explícita
  let customerAge: number = 28;
  customerAge = customerAge + 1;
  console.log('customerAge: ', customerAge);

  let productInStock: number;
  console.log('productInStock: ', productInStock);
  if (productInStock > 10) {
    console.log('Product in stock');
  }

  let discount = parseInt('200');
  console.log('discount: ', discount);
  if (discount <= 200) {
    console.log('Discount is valid');
  } else {
    console.log('Discount is NOT valid');
  }

  let hex = 0xfff;
  console.log('hex: ', hex);

  let bin = 0b1010;
  console.log('bin: ', bin);

  const myNumber: number = 10;
})();
