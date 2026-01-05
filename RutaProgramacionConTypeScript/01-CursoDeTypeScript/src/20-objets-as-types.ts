(() => {
  type Sizes = 'S' | 'M' | 'L' | 'XL';
  type Product = {
    title: string,
    createdAt: Date,
    stock: number
    size?: Sizes
  };

  const products: Product[] = [];

  const login = (data: {email: string, password: string}) => {
    console.log(data.email, data.password);
  }

  login({
    email: 'edsongalan@correo.com',
    password: '12345678a'
  });

  const addProduct = (data: Product) => {
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

  products.push({
    title: 'Camisa',
    createdAt: new Date(2026,1,4),
    stock: 8,
    size: 'L'
  });

  console.log('Products: ', products);

})();
