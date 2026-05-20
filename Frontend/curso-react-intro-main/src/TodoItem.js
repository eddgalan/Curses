import './TodoItem.css';
import {CompleteIcon} from './CompleteIcon';
import {DeleteIcon} from './DeleteIcon';

function TodoItem(props) {
  return (
    <li className="TodoItem">
      <CompleteIcon onComplete={props.onComplete} completed={props.completed} />
      <p className={`TodoItem-p ${props.completed ? 'TodoItem-p--complete' : ''}`}>
        {props.text}
      </p>
      <DeleteIcon onDelete={props.onDelete} text={props.text} />
    </li>
  );
}

export { TodoItem };
