(() => {
  let myDynamicVar: any;
  myDynamicVar = 'hola';
  myDynamicVar = 2025;
  myDynamicVar = true;
  myDynamicVar = {};

  myDynamicVar = 'hello';
  const rta = (myDynamicVar as string).toUpperCase();
  console.log(rta);

  myDynamicVar = 2025;
  const rta_ = (myDynamicVar as number).toFixed(2);
  console.log(rta_);

  const rta__ = (<number>myDynamicVar).toFixed(2);
  console.log(rta__);
})();
