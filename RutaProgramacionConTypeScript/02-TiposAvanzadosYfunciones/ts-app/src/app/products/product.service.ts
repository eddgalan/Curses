import { type Product} from './product.model';

export const products: Product[] = [];

export const addProduct = (data: Product) => {
//    data.id = Math.random();
//    data.createdAt = new Date();
    products.push(data);
};
