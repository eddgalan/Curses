import {TodoCounter} from '../TodoCounter';
import {TodoSearch} from '../TodoSearch';
import {TodoList} from '../TodoList';
import {TodoItem} from "../TodoItem";
import {CreateTodoButton} from '../CreateTodoButton';
import React from 'react';

function AppUI({
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