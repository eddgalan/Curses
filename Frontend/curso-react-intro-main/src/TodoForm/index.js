import React from 'react';
import './style.css';

function TodoForm() {
  return (
    <form onSubmit={(event) => {
      event.preventDefault();
    }}>
      <label>Escribe tu nuevo TODO</label>
      <input type="text" placeholder="Nueva tarea por hacer..." />
      <div className="TodoForm-buttonContainer">
        <button className="TodoForm-button TodoForm-button-create" type="submit">Agregar</button>
        <button className="TodoForm-button TodoForm-button-cancel" type="button">Cancelar</button>
      </div>
    </form>
  );
}

export { TodoForm };
