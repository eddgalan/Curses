(() => {
  // Inferido
  let productName = 'Product 1';
  // productName = null;
  // productName = () => {console.log('Hola')};
  // productName = 123;

  productName = 'My amazing product';
  console.log('productName: ', productName);

  // Explícito
  let productDescription: string = 'This is a product description';
  console.log('productDescription: ', productDescription);

  let productPrice: number = 100;
  let isNew: boolean = true;

  const summary = `
    title: ${productName}
    description: ${productDescription}
    price: ${productPrice}
    isNew: ${isNew}
  `;
  console.log('summary: ', summary);

})();
