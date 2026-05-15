import React from 'react';
import { TodoCounter } from './TodoCounter';
import { TodoSearch } from './TodoSearch';
import { TodoList } from './TodoList';
import { TodoItem } from "./TodoItem";
import { CreateTodoButton } from './CreateTodoButton';

const defaultTodos = [
  { text: 'Estudiar React', completed: true },
  { text: 'Llorar con mis amigos', completed: false},
  { text: 'Hacer ejercicio', completed: false},
  { text: 'Dormir', completed: false},
  { text: 'Comer', completed: true},
];

function App() {
  return (
    <React.Fragment>
      <TodoCounter totalTodos={3} completedTodos={2}/>
      <TodoSearch />
      <TodoList>
        { defaultTodos.map(todo => (
          <TodoItem
            key={ todo.text }
            text={ todo.text }
            completed={ todo.completed }
          />
        ))}
      </TodoList>
      <CreateTodoButton />
    </React.Fragment>
  );
}

export default App;
