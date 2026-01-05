(() => {
  type Sizes = 'S' | 'M' | 'L' | 'XL';

  function createProductToJson(
    title: string,
    createdAt: Date,
    stock: number,
    size: Sizes
  ) {
    return {
      title,
      createdAt: createdAt.toISOString(),
      stock,
      size
    }
  }

  const createProductToJsonV2 = (
    title: string,
    createdAt: Date,
    stock: number,
    size?: Sizes    // Indica que el campo size es opcional
  ) => {
    return {
      title,
      createdAt: createdAt.toISOString(),
      stock,
      size
    }
  }

  const product1 = createProductToJson('Camiseta', new Date(), 10, 'M');
  console.log('product1: ', product1);
  console.log('product1: ', product1.title);

  const product2 = createProductToJsonV2('Camiseta', new Date(), 10);
  console.log('product2: ', product2);
  console.log('product2: ', product2.title);
  console.log('product2: ', product2.size);
})();
