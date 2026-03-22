import {IsEnum, IsNotEmpty, IsOptional, IsUrl, Length, validate, validateOrReject} from 'class-validator';
import { ACCESS_TYPE, Category } from "../models/category.model";

export interface CategoryDtoInterface extends Omit<Category, 'id'> {}

export class CreateCategoryDto implements CategoryDtoInterface {
  @IsNotEmpty()
  @Length(4, 140)
  name!: string;

  @IsUrl()
  @IsNotEmpty()
  image!: string;

  @IsOptional()
  @IsEnum(ACCESS_TYPE)
  access?: ACCESS_TYPE;
}

(async () => {
  try {
    const dto = new CreateCategoryDto();
    dto.name = 'Hombre';
    dto.image = 'https://google.com';
    //  await validate(dto);
    await validateOrReject(dto);
  } catch (error) {
    console.log(error);
  }
})();
