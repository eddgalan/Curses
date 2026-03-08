import { faker } from '@faker-js/faker';
import { type Product } from '../models/product.model';
import {type CreateProductDto, type UpdateProductDto} from "../dtos/product.dto.js";
import {ProductService} from "../models/product-service.model";

export class ProductMemoryService implements ProductService {
  private products: Product[] = [];

  get(id: Product['id']) : Product | null {
    return this.products.find(product => product.id === id) ?? null;
  }

  getAll(): Product[] {
    return this.products;
  }

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
}
