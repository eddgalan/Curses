import { faker } from '@faker-js/faker';
import { type Product } from '../models/product.model';
import {type CreateProductDto, type UpdateProductDto} from "../dtos/product.dto.js";

export class ProductMemoryService {
  private products: Product[] = [];

  create(data: CreateProductDto) {
    const newProduct = {
      ...data,
      id: faker.number.int(),
      category: {
        id: data.categoryId,
        name: faker.commerce.department(),
        image: faker.image.url(),
      }
    };
    return this.add(newProduct);
  };

  add(product: Product) {
    this.products.push(product);
    return product;
  }

  update(id: Product['id'], changes: UpdateProductDto): Product {
    const index = this.products.findIndex(product => product.id === id);
    const prevData = this.products[index];

    this.products[index] = <Product> {
      ...prevData,
      ...changes
    };

    return this.products[index];
  }

  get(id: Product['id']) {
    return this.products.find(product => product.id === id);
  }

  getAll() {
    return this.products;
  }
}

export const products: Product[] = [];
