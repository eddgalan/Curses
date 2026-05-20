import {BsTrashFill} from "react-icons/bs";

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