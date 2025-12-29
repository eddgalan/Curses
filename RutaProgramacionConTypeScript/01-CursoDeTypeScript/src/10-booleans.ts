(() => {
  // Forma inferida
  let isEnabled = true;
  //  isEnabled = 'hola';
  //  isEnabled = 20251228;
  isEnabled = false;

  // Forma explícita
  let isNew: boolean = false;
  console.log('isNew: ', isNew);
  isNew = true;
  console.log('isNew: ', isNew);

  const random = Math.random();
  console.log('random: ', random);

  isNew = random >= 0.5;
  console.log('isNew: ', isNew);
})();
