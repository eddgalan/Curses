import {TodoCounter} from '../TodoCounter';
import {TodoSearch} from '../TodoSearch';
import {TodoList} from '../TodoList';
import {TodoItem} from "../TodoItem";
import {CreateTodoButton} from '../CreateTodoButton';
import React from 'react';
import {TodosLoading} from "../TodosLoading";
import {TodosError} from "../TodosError";
import {TodosEmpty} from "../TodosEmpty";
import {TodoContext} from "../TodoContext";
import {Modal} from "../Modal";

function AppUI() {
  const {
    loading,
    error,
    searchedTodos,
    completeTodo,
    deleteTodo,
    openModal,
    setOpenModal,
  } = React.useContext(TodoContext);

  return (
    <React.Fragment>
      <TodoCounter />
      <TodoSearch />
      <TodoList>
        {loading && (<>
          <TodosLoading /><TodosLoading /><TodosLoading />
        </>)}
        {error && <TodosError />}
        {(!loading && searchedTodos.length === 0) && <TodosEmpty />}

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
      <CreateTodoButton setOpenModal={setOpenModal}/>

      {openModal && (
        <Modal>
          Agregar Todos
        </Modal>
      )}
    </React.Fragment>
  );
}

export {AppUI};
