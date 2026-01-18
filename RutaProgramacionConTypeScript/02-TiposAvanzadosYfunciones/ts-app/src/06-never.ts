const withoutEnd = () => {
  while (true) {console.log('Hello world');}
};

const fail = (message: string) => {
  throw new Error(message);
};

const example = (input: unknown) => {
  if (typeof input === 'string') {
    return 'Is a string: ' + input;
  } else if (Array.isArray(input)) {
      return 'Is an array';
  }
  return fail('Expected a string or an array, got ' + typeof input);
};

console.log(example('Hello world'));
console.log(example([]));
console.log(example(10));           // End here
console.log(example('After fail'));