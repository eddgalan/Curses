import {TodoCounter} from '../TodoCounter';
import {TodoSearch} from '../TodoSearch';
import {TodoList} from '../TodoList';
import {TodoItem} from "../TodoItem";
import {CreateTodoButton} from '../CreateTodoButton';
import React from 'react';

function AppUI({
                 loading,
                 error,
                 completedTodos,
                 totalTodos,
                 searchValue,
                 setSearchValue,
                 searchedTodos,
                 completeTodo,
                 deleteTodo
 }) {
  return (
    <React.Fragment>
      <TodoCounter
        totalTodos={totalTodos}
        completedTodos={completedTodos}/>
      <TodoSearch
        serchValue={searchValue}
        setSearchValue={setSearchValue}/>
      <TodoList>
        {loading && <p>Cargando...</p>}
        {error && <p>Ocurrio un error</p>}
        {(!loading && searchedTodos.length === 0) && <p>Crea tu primer ToDo</p>}

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

export {AppUI};