import { useSelector, useDispatch } from "react-redux";
import { add, remove, changeStatus } from "../redux/actions/actions.js";
import { useRef } from "react";

const AllList = (props) => {
  const todoList = useSelector((state) => state.todoReducer.listOftodos);
  const dispatch = useDispatch();

  const checkValue = (e, index) => {
    if (e.target.checked === false) {
      dispatch(changeStatus("Not Done", index));
    } else {
      dispatch(changeStatus("Done", index));
    }
  };

  return todoList.map((item) => {
    return (
      <div key={item.id}>
        <p>{item.status}</p>
        <input type="checkbox" onClick={(e) => checkValue(e, item.id)} />
        <p>{item.text}</p>
        <button onClick={() => dispatch(remove(item.id))}>Remove</button>
      </div>
    );
  });
};

const Todo = (props) => {
  const dispatch = useDispatch();
  const task = useRef("");

  return (
    <>
      <h1>Your Todo</h1>
      <div>
        <input type="text" ref={task} />
        <button onClick={() => dispatch(add(task.current.value))}>Add</button>
      </div>
      <h2>My Tasks:</h2>
      <div>{AllList()}</div>
    </>
  );
};

export default Todo;
