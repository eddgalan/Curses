const productPrice_: number = 100;
/**
 * const: Declaración
 * productPrice: Nombre de la variable (Identificador)
 * number: Tipo de dato (Tipado - Type Annotation)
 */

// =====================================================================================================================
/**
 *  Función anónima autoejecutada: (() => {})();
 */

(() => {
  let productName = 'Product 1';    // El tipo de dato está 'inferido'
  let productPrice = 100;         // El tipo de dato está 'inferido'

  productName = 'Product 2';
  productName.toLowerCase();

  productPrice.toFixed(2);

  const productStock = 10;
  // productStock--;      // Alerta estos errores
})();
