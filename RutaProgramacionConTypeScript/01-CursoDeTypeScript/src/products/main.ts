// @ts-ignore
import { addProduct, calculateStock, products } from  './product.service';

addProduct({
  name: 'Camisa',
  createdAt: new Date(),
  stock: 10,
  size: 'L'
});

addProduct({
  name: 'Pantalon',
  createdAt: new Date(),
  stock: 5,
});

console.log(products);

const total = calculateStock();
console.log('total: ', total);
