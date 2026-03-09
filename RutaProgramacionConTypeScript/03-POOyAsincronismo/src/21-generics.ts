/*
function getValue(value: unknown){
  return value
}

getValue(15).toFixed(2);
getValue('12').t();
getValue([]).t();
 */

function getValue<myType>(value: myType) {
  const array: myType[] = [value];
  return value;
}

getValue<number>(15).toFixed(2);
getValue<string>('155').toLowerCase();
getValue<number[]>([]).forEach;
