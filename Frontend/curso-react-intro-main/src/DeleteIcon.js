import {BsTrashFill} from "react-icons/bs";
import './DeleteIcon.css';

function DeleteIcon({onDelete, text}) {
  return (
    <span
      className="Icon Icon-delete"
      onClick={onDelete.bind(null, text)}
    >
        <BsTrashFill/>
      </span>
  );
}

export {DeleteIcon};