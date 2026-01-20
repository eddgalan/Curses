import { faker } from '@faker-js/faker';
import { type Product } from './product.model.js';
import { type CreateProductDto } from "./product.dto.js";

export const products: Product[] = [];

export const addProduct = (data: CreateProductDto): Product => {
//    data.id = Math.random();
//    data.createdAt = new Date();
    const newProduct = {
        ...data,
        id: faker.string.uuid(),
        createdAt: faker.date.recent(),
        updatedAt: faker.date.recent(),
        category: {
            id: data.categoryId,
            name: faker.commerce.department(),
            createdAt: faker.date.recent(),
            updatedAt: faker.date.recent(),
        }
    };
    products.push(newProduct);
    return newProduct;
};

export const updateProduct = (id: string, changes:Product) => {
    // ToDo: Implementar
}
