import React from 'react';
import {TodoCounter} from './TodoCounter';
import {TodoSearch} from './TodoSearch';
import {TodoList} from './TodoList';
import {TodoItem} from "./TodoItem";
import {CreateTodoButton} from './CreateTodoButton';

function useLocalStorage(itemName, initialValue) {
  let parsedItem = JSON.parse(localStorage.getItem(itemName)) || initialValue;

  const [item, setItem] = React.useState(parsedItem);

  const saveItem = (newItem) => {
    localStorage.setItem(itemName, JSON.stringify(newItem));
    setItem(newItem);
  }

  return [item, saveItem];
}

function App() {
  const [todos, saveTodos] = useLocalStorage('TODOS_V1', []);
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
    saveTodos(newTodos);
  };

  const deleteTodo = (text) => {
    const index = getTodoIndexByText(text);
    const newTodos = [...todos];

    newTodos.splice(index, 1);
    saveTodos(newTodos);
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
