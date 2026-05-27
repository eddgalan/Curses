import React from 'react';
import './style.css';
import {TodoContext} from "../TodoContext";

function TodoForm() {
  const {
    setOpenModal,
    addTodo,
  } = React.useContext(TodoContext);

  const onChange = (event) => {
    setNewTodo(event.target.value);
  }

  const [newTodo, setNewTodo] = React.useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    addTodo(newTodo);
    setOpenModal(false);
  }

  const handleCancel = () => {
    setOpenModal(false);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>Escribe tu nuevo TODO</label>
      <input type="text" placeholder="Nueva tarea por hacer..." value={newTodo} onChange={onChange} required={true}/>
      <div className="TodoForm-buttonContainer">
        <button className="TodoForm-button TodoForm-button-create" type="submit">Agregar</button>
        <button className="TodoForm-button TodoForm-button-cancel" type="button" onClick={handleCancel}>Cancelar</button>
      </div>
    </form>
  );
}

export { TodoForm };
