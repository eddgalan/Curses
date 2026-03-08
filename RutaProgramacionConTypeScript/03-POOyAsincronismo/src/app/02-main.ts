import { ProductMemoryService } from './services/product-memory.service';

const productMemoryService = new ProductMemoryService();

productMemoryService.create({
  title: 'Producto1',
  price: 100,
  description: 'My First Product',
  categoryId: 1,
  images: []
});

const products = productMemoryService.getAll();
console.log(products);

const productId = products[0]?.id;

if (typeof productId === "number") {
  productMemoryService.update(productId, {
    title: 'Producto Actualizado',
    price: 199,
    description: 'My First Product Updated',
    categoryId: 1,
  });

  const response = productMemoryService.get(productId);
  console.log(response);
}
