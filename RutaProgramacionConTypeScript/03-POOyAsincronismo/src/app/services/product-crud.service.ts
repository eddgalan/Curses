import {BaseHttpService} from "./base-http-service";
import {Product} from "../models/product.model";
import {UpdateProductDto} from "../dtos/product.dto";
import {ProductHttpService} from "./product-http2.service";

export class ProductCrudService {
  private url = 'https://api.escuelajs.co/api/v1/products';
  private http = new ProductHttpService(this.url);

  async update(id: Product['id'], dto: UpdateProductDto) {
    // Validate permissions
    // Add Logic
    this.http.otherRequest();
    return this.http.update(id, dto);
  }
}
