enum ROLES {
  ADMIN = 'admin',
  SELLER = 'seller',
    CUSTOMER = 'customer',
}

type User = {
    username: string;
    role: ROLES;
};

const user: User = {
    username: 'edson',
    role: ROLES.ADMIN
};
