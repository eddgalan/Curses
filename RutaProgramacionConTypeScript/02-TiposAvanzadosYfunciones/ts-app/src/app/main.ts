import { faker } from '@faker-js/faker';
import {addProduct, products} from './products/product.service.js';

for (let i = 0; i < 10; i++) {
    addProduct({
        id: faker.string.uuid(),
        title: faker.commerce.productName(),
        description: faker.commerce.productDescription(),
        image: faker.image.url(),
        color: faker.color.human(),
        size: faker.helpers.arrayElement([ 'S', 'M', 'L', 'XL']),
        price: parseFloat(faker.commerce.price()),
        isNew: faker.datatype.boolean(),
        tags: faker.lorem.words(3).split(' '),
        createdAt: faker.date.recent(),
        updatedAt: faker.date.recent(),
        stock: faker.number.int({min: 1, max: 100}),
        category: {
            id: faker.string.uuid(),
            name: faker.commerce.department(),
            createdAt: faker.date.recent(),
            updatedAt: faker.date.recent()
        }
    });
}

console.log('Products: ', products);
