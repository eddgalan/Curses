import type {BaseModel} from "../base.model.js";

export enum ROLES {
    ADMIN = 'admin',
    SELLER = 'seller',
    CUSTOMER = 'customer'
}

export interface User extends BaseModel{
    username: string;
    role: ROLES;
}
