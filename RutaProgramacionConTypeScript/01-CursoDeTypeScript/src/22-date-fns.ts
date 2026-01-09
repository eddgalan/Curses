import { subDays, format } from 'date-fns';

const date = new Date(1998, 1, 28);
const rta = subDays(date, 10);      // Resta 10 días a date
const str = format(rta, 'yyyy-MM-dd');
console.log(str);
