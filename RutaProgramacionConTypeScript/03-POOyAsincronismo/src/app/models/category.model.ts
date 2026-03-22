export enum ACCESS_TYPE {
  PUBLIC = 'public',
  PRIVATE = 'private',
}

export interface Category {
  id:         number;
  name:       string;
  image:      string;
  access?:     ACCESS_TYPE;
}
