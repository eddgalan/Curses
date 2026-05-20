import {BsCheckLg} from 'react-icons/bs'

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
