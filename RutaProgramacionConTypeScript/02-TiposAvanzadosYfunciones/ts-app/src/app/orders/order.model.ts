import { type Product } from './../products/product.model.js';
import { type User } from './../users/user.model.js';
import type {BaseModel} from "../base.model.js";

export interface Order extends BaseModel{
    products: Product[]
    user: User
}
