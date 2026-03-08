import { Product } from "./product.model";
import { CreateProductDto, UpdateProductDto } from "../dtos/product.dto";

export interface ProductService {
  getAll(): Product[] | Promise<Product[]>;
  get(id: Product['id']): Product | null | Promise<Product | null>;
  create(dto: CreateProductDto): Product | Promise<Product>;
  update(id: Product['id'], data: UpdateProductDto): Product | Promise<Product>;
}
