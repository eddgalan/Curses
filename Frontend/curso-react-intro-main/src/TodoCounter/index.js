import './style.css';

/*
const style = {
  fontSize: '24px',
  textAlign: 'center',
  margin: '0',
  padding: '48px',
}
 */

function TodoCounter({ totalTodos, completedTodos }) {
  return <h2 className="TodoCounter">Has completado <span>{ completedTodos }</span> de <span>{ totalTodos }</span> TODOs</h2>;
}

export { TodoCounter };
