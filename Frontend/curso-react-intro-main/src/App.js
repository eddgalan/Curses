import React from 'react';
import {TodoCounter} from './TodoCounter';
import {TodoSearch} from './TodoSearch';
import {TodoList} from './TodoList';
import {TodoItem} from "./TodoItem";
import {CreateTodoButton} from './CreateTodoButton';

const defaultTodos = [
  {text: 'Estudiar React', completed: true},
  {text: 'Llorar con mis amigos', completed: false},
  {text: 'Hacer ejercicio', completed: false},
  {text: 'Dormir', completed: false},
  {text: 'Comer', completed: true},
  {text: 'Aprender ReactJs', completed: true},
];

function App() {
  const [todos, setTodos] = React.useState(defaultTodos)
  const [searchValue, setSearchValue] = React.useState('');

  const completedTodos = todos.filter(todo => todo.completed).length;
  const totalTodos = todos.length;

  const searchedTodos = todos.filter(
    (todo) => {
      const todoText = todo.text.toLowerCase();
      const searchText = searchValue.toLowerCase();
      return todoText.includes(searchText);
    }
  );

  const getTodoIndexByText = (text) => {
    return todos.findIndex(
      (todo) => todo.text === text
    );
  }

  const completeTodo = (text) => {
    const index = getTodoIndexByText(text);
    const newTodos = [...todos];

    newTodos[index].completed = true;
    setTodos(newTodos);
  };

  const deleteTodo = (text) => {
    const index = getTodoIndexByText(text);
    const newTodos = [...todos];

    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  return (
    <React.Fragment>
      <TodoCounter
        totalTodos={totalTodos}
        completedTodos={completedTodos}/>
      <TodoSearch
        serchValue={searchValue}
        setSearchValue={setSearchValue}/>
      <TodoList>
        {searchedTodos.map(todo => (
          <TodoItem
            key={todo.text}
            text={todo.text}
            completed={todo.completed}
            onComplete={() => completeTodo(todo.text)}
            /*
            Se puede tambien proner la propiedad onComplete de la siguiente forma:
             onComplete={completeTodo}
             Y en el TodoItem poner el onClick asi:
             onClick={props.onComplete.bind(null, props.text)}
             */
            onDelete={deleteTodo}
          />
        ))}
      </TodoList>
      <CreateTodoButton/>
    </React.Fragment>
  );
}

export default App;
