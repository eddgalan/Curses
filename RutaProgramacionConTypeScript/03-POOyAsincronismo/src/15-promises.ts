import axios from 'axios';


(async () => {
  function delay (time: number) {
    const promise = new Promise<boolean>((resolve) => {
      setTimeout(() => {
        resolve(true);
      }, time);
    });
    return promise;
  }

  function getProducts() {
    const promise = axios.get('https://api.escuelajs.co/api/v1/products');
    return promise;
  }

  async function getProductsAsync() {
    const response = await axios.get('https://api.escuelajs.co/api/v1/products');
    return response.data;
  }

  // Calling delay function
  console.log('Waiting...'.repeat(5));
  const response = await delay(3000);
  console.log(response);

  // Calling getProducts function
  const products = await getProducts();
  console.log(products.data);

  // Calling getProductsAsync function
  const productsAsync = await getProductsAsync();
  console.log(productsAsync);
})();
