import React from 'react';
import './style.css';
import {TodoContext} from "../TodoContext";

/*
const style = {
  fontSize: '24px',
  textAlign: 'center',
  margin: '0',
  padding: '48px',
}
 */

function TodoCounter() {
  const {
    completedTodos,
    totalTodos,
  } = React.useContext(TodoContext)
  return (<h2 className="TodoCounter">
    Has completado <span>{ completedTodos }</span> de <span>{ totalTodos }</span> TODOs
  </h2>);
}

export { TodoCounter };
