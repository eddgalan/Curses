import { faker } from '@faker-js/faker';
import { type Product } from './product.model.js';
import {type CreateProductDto, type SearchProductDto, type UpdateProductDto} from "./product.dto.js";

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

export const updateProduct = (id: string, changes: UpdateProductDto): Product => {
    const index = products.findIndex(product => product.id === id);
    const prevData = products[index];

    products[index] = <Product> {
        ...prevData,
        ...changes
    };

    return products[index];
}

export const searchProducts = (dto: SearchProductDto): Product[] => {
    // ToDo: Implementar filtro
    return products;
};
