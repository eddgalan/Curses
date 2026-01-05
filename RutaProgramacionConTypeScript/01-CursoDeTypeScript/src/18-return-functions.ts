(() => {
  const calcTotal = (prices: number[]): string => {
    return prices.reduce((acc, price) => acc + price, 0).toString();
  };

  const printTotal = (prices: number[]): void => {
    const rta = calcTotal(prices);
    console.log(`Total: $${rta}`);
  };

  printTotal([100, 200, 300]);
})();
