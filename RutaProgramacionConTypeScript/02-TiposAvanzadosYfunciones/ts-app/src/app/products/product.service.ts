import { type Product } from './product.model.js';

export const products: Product[] = [];

export const addProduct = (data: Product) => {
//    data.id = Math.random();
//    data.createdAt = new Date();
    products.push(data);
};

export const updateProduct = (id: string, changes:Product) => {
    // ToDo: Implementar
}
