(() => {
  type UserID = string | number | boolean;
  let userId: UserID;

  // Literal types
  let shirtSize: 'S' | 'M' | 'L' | 'XL';
  shirtSize = 'XL';
  shirtSize = 'XXL';

  type Sizes = 'S' | 'M' | 'L' | 'XL';
  let shirtSize_: Sizes;

  function greeting(userId: UserID, size: Sizes) {
    if (typeof userId === 'string') {
      console.log(`string: ${userId.toLowerCase()}`);
    }
  }

  greeting(100023, 'L');
  greeting('Edson', 'XXL');

})();
