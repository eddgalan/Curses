let anyVar: any;
anyVar = true;
anyVar = null;
anyVar = 1;
anyVar = "Hola";

// Errores
let isNew: boolean = anyVar;
// anyVar.showData();          // TypeError: anyVar.showData is not a function

// Unknow
let unknownVar: unknown;
unknownVar = true;
unknownVar = null;
unknownVar = 1;
unknownVar = "Hola";

// unknownVar.showData();          // TypeError: unknownVar.showData is not a function
unknownVar.toUpperCase();
// Unknow fuerza a realizar una validación de tipo
if (typeof unknownVar === "string") {
    console.log(unknownVar.toUpperCase());
}

let isNew_: boolean = unknownVar;       // Pide verificación de tipo
if (typeof unknownVar === 'boolean') {
    let isNew__ = unknownVar;
}

const parse = (str: string): unknown => JSON.parse(str)