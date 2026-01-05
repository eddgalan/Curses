(() => {
  const login = (data: {email: string, password: string}) => {
    console.log(data.email, data.password);
  }

  login({
    email: 'edsongalan@correo.com',
    password: '12345678a'
  });

  type Sizes = 'S' | 'M' | 'L' | 'XL';

  const products: any[] = [];

  const addProduct = (data: {
    title: string,
    createdAt: Date,
    stock: number
    size?: Sizes
  }) => {
    products.push(data);
  };

  addProduct({
    title: 'Camiseta',
    createdAt: new Date(),
    stock: 10,
    size: 'M'
  });
  addProduct({
    title: 'Pantalon',
    createdAt: new Date(),
    stock: 5,
  })
  console.log('Products: ', products);

})();
