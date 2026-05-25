import React from 'react';
import {AppUI} from './AppUI';
import {useLocalStorage} from './UseLocalStorage';

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
    <AppUI
      completedTodos={completedTodos}
      totalTodos={totalTodos}
      searchValue={searchValue}
      setSearchValue={setSearchValue}
      searchedTodos={searchedTodos}
      completeTodo={completeTodo}
      deleteTodo={deleteTodo}
    />
  )
}

export default App;
