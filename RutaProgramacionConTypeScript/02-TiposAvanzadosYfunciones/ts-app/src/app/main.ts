import { faker } from '@faker-js/faker';
import {addProduct, products, updateProduct, searchProducts} from './products/product.service.js';

for (let i = 0; i < 10; i++) {
    addProduct({
        title: faker.commerce.productName(),
        description: faker.commerce.productDescription(),
        image: faker.image.url(),
        color: faker.color.human(),
        size: faker.helpers.arrayElement([ 'S', 'M', 'L', 'XL']),
        price: parseFloat(faker.commerce.price()),
        isNew: faker.datatype.boolean(),
        tags: faker.lorem.words(3).split(' '),
        stock: faker.number.int({min: 1, max: 100}),
        categoryId: faker.string.uuid()
    });
}

console.log('Products: ', products);

const product = products[0];
console.log('Product: ', product);

if (typeof product === 'undefined') throw new Error(
    'No hay productos registrados'
)

const productUpdated = updateProduct(
    product.id, {
        title: 'Producto modificado',
        stock: 99,
        price: 199,
        // createdAt: new Date()            // Prohibe que se modifique
    }
);

console.log('Product updated: ', productUpdated);

const findProduct = searchProducts({
    stock: 10,
    color: 'red',
    isNew: true,
    tags: ['rojo', 'blusas']
});
console.log('Products found: ', findProduct);