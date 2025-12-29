(() => {
  let userId: string | number;
  userId = 100023;
  userId = 'U0001';

  function greeting(myText: string | number) {
    if (typeof myText === 'string') {
      console.log(`string: ${myText.toLowerCase()}`);
    } else {
      console.log(`number: ${myText.toFixed(3)}`);
    }
  }

  greeting(100023);
  greeting('Edson');
})();
