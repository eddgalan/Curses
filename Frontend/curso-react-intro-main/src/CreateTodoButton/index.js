import './style.css'

function CreateTodoButton() {
  return (
    <button
      className="CreateTodoButton"
      onClick={(event) => {
        console.log('Button clicked', event)
      }}
    >+</button>);
}

export { CreateTodoButton };
