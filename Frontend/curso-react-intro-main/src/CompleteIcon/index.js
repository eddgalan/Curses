import {BsCheckLg} from 'react-icons/bs';
import './style.css';

function CompleteIcon({onComplete, completed}) {
  return (
    <span
      className={`Icon Icon-check ${completed ? 'Icon-check--active' : ''}`}
      onClick={onComplete}
    >
      <BsCheckLg />
    </span>)
}

export { CompleteIcon };
