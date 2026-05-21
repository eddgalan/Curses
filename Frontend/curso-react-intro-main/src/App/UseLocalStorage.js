import React from 'react';

function useLocalStorage(itemName, initialValue) {
  let parsedItem = JSON.parse(localStorage.getItem(itemName)) || initialValue;

  const [item, setItem] = React.useState(parsedItem);

  const saveItem = (newItem) => {
    localStorage.setItem(itemName, JSON.stringify(newItem));
    setItem(newItem);
  }

  return [item, saveItem];
}

export { useLocalStorage };
