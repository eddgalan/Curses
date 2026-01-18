import { type User, ROLES } from './03-enum';

const currentUser: User = {
    username: 'egalan',
    role: ROLES.CUSTOMER
};

// Check Admin
export const checkIsAdmin = () => {
    return currentUser.role === ROLES.ADMIN;
};

checkIsAdmin();
console.log(currentUser);
console.log(checkIsAdmin());

// Check Role
export const checkRole = (roles: string[]) => {
    return roles.includes(currentUser.role);
};
console.log('checkRole: ', checkRole([ROLES.ADMIN, ROLES.SELLER]));

// Refactor Check Role
export const checkRole_ = (...roles: string[]) => {
    return roles.includes(currentUser.role);
};
console.log('checkRole_: ', checkRole_(ROLES.ADMIN, ROLES.SELLER, ROLES.CUSTOMER));
