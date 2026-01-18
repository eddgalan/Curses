function parseStr(input: string | string[]): string | string[] {
    if (Array.isArray(input)) {
        return input.join('');     // Return string
    } else {
        return input.split('');     // Return string
    }
}

const array_ = parseStr('Edson');
console.log('array_: ', array_);
array_.reverse();           // No sabe que array_ es un string o un array hasta que se valida como en la siguiente condición
if (Array.isArray(array_)) {
    array_.reverse();
}


const string_ = parseStr(['E', 'd', 's', 'o', 'n']);
console.log('string_: ', string_);
string_.toLowerCase();      // No sabe que string_ es un string o un array
if (typeof string_ === 'string') {
    string_.toLowerCase();
}
