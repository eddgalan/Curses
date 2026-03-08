import axios from 'axios';
import {ProductService} from "../models/product-service.model";
import {CreateProductDto, UpdateProductDto} from "../dtos/product.dto";
import {Product} from "../models/product.model";

export class ProductHttpService implements ProductService {
  private url = 'https://api.escuelajs.co/api/v1/products';

  async getAll(): Promise<Product[]> {
    const { data } = await axios.get<Product[]>(this.url);
    return data;
  }

  async get(id: Product["id"]) : Promise<Product | null> {
    try {
      const { data } = await axios.get<Product>(`${this.url}/${id}`);
      return data;
    } catch {
      return null;
    }
  }

  async create(dto: CreateProductDto): Promise<Product> {
    const { data: newProduct } = await axios.post(this.url, dto);
    return newProduct;
  }

  async update(id: Product['id'], data: UpdateProductDto) : Promise<Product>{
    const { data: updatedProduct } = await axios.put<Product>(`${this.url}/${id}`, data);
    return updatedProduct;
  }
}
