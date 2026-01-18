export const createProduct = (
    id: string | number,
    isNew: boolean = true,
    stock: number = 10,
) => {
    return {
        id,
        stock,
        isNew
    };
};

const product = createProduct('1', true,10);
console.log('product: ', product);

const product2 = createProduct('2', true);
console.log('product2: ', product2);

const product3 = createProduct('3', false, 0);
console.log('product3: ', product3);

const product4 = createProduct('4', true, 100);
console.log('product3: ', product4);

const product5 = createProduct('5');
console.log('product3: ', product5);
