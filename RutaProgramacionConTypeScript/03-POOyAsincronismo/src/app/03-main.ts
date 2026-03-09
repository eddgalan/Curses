import { ProductHttpService } from "./services/product-http.service";

(async () => {
  const productHttpService = new ProductHttpService();

  console.log('---'.repeat(10));
  console.log('Getting products');
  const products = await productHttpService.getAll();
  console.log(products.length);

  console.log('---'.repeat(10));
  console.log('Updating product');
  const product = products[0];
  if (!product) throw new Error('No hay productos');
  const productId = product?.id ?? 1;
  await productHttpService.update(productId, {
    title: 'Chamarra (Editado)',
    price: 850,
    description: 'Lorem ipsum dolor sit amet',
    images: product.images,
    categoryId: product.category.id
  });

  console.log('---'.repeat(10));
  console.log('Getting single product');
  const productUpdated = await productHttpService.get(productId);
  console.log(productUpdated);

})();
