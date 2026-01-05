(()=> {
  // let myNumber: number = undefined;  // Error
  // let myString: string = null;       // Error

  let myNumber: number | null = null;
  let myString: string | undefined = undefined;

  myNumber = 15;
  myString = 'TypeScript';

  console.log(myNumber);
  console.log(myString);

  function hi(name: string | null) {
    let hello = 'Hello ';
    if (name) {
      hello += name.toUpperCase();
    } else {
      hello += 'World';
    }
    console.log(hello);
  }

  function hi_(name: string | null) {
    let hello = 'Hello ';
    hello += name?.toLowerCase() || 'World';
    console.log(hello);
  }

  hi('Edson');
  hi(null);

  hi_('Edson');
  hi_(null);
})();
