import axios from 'axios';
import {Category} from "../models/category.model";
import {Product} from "../models/product.model";

export class BaseHttpService<TypeClass> {
  // data: TypeClass[] = [];

  constructor(
    private url: string
  ) {

  }

  async getAll() {
    const { data } = await axios.get<TypeClass[]>(this.url);
    return data;
  }
}

// const service = new BaseHttpService<string>();
// service.getAll();
//
// const service2 = new BaseHttpService<Category>();
// service2.getAll();

(async () => {
  const url1 = 'https://api.escuelajs.co/api/v1/products';
  const productsService = new BaseHttpService<Product>(url1);
  const response = await productsService.getAll();
  console.log('products qty', response.length);

  const url2 = 'https://api.escuelajs.co/api/v1/categories';
  const categoryService = new BaseHttpService<Category>(url2);
  const response2 = await categoryService.getAll();
  console.log('categories qty', response2.length);
})();
