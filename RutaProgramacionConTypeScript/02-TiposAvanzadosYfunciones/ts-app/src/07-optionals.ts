export const createProduct = (
    id: string | number,
    isNew?: boolean,
    stock?: number,
) => {
    /*
    El operador || tiene el siguiente comportamiento:
    0 === false
    '' === false
    null === false
    false === false
    Es mejor usar el operador ??
     */
    return {
        id,
        stock: stock ?? 10,
        isNew: isNew ?? true
    };
};

const product = createProduct('1', true,10);
console.log('product: ', product);

const product2 = createProduct('2', true);
console.log('product2: ', product2);

const product3 = createProduct('3', false, 0);
console.log('product3: ', product3);
