import { addProduct } from 'products/product.service';

addProduct({
    id: '1',
    title: 'Producto 1',
    createdAt: new Date(),
    stock: 10,
    size: 'M'
});

