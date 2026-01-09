import type { Product } from './product.model';

// @ts-ignore
export const products: Product[] = [];

// @ts-ignore
export const addProduct = (data: Product) => {
  products.push(data);
};

// @ts-ignore
export const calculateStock = (): number => {
  return products.reduce((acc, product) => acc + product.stock, 0);
}
