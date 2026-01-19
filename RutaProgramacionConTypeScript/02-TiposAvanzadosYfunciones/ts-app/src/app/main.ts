import { addProduct } from './products/product.service';

addProduct({
    id: 1,
    title: 'Camisa',
    createdAt: new Date(),
    updatedAt: new Date(),
    stock: 100,
    category: {
        id: 1,
        name: 'Main category',
        createdAt: new Date(),
        updatedAt: new Date()
    }
});
