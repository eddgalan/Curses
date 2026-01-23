import type { Product } from "./product.model.js";

// Sirve para omitir datos
export interface CreateProductDto extends Omit<Product, 'id' | 'createdAt' | 'updatedAt' | 'category'> {
    categoryId: string;
}
// Hace lo opuesto que el Omit, es decir, obligar a mandar datos
type example = Pick<Product, 'color' | 'description'>

// Se usa para actualizar, crea un Partial de CreateProductDto
export interface UpdateProductDto extends Partial<CreateProductDto> {

}

// Hace lo opuesto que el Partial, es decir, obligar a mandar datos
type example2 = Required<Product>;

export interface SearchProductDto extends Readonly<Partial<Omit<Product, 'tags'>>> {
    readonly tags: ReadonlyArray<string>;
}

type example3 = Readonly<Product>;
