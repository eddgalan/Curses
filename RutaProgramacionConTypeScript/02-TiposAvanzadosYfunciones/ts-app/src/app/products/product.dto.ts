import type { Product } from "./product.model.js";

export interface CreateProductDto extends Omit<Product, 'id' | 'createdAt' | 'updatedAt' | 'category'> {
    categoryId: string;
}

type example = Pick<Product, 'color' | 'description'>
