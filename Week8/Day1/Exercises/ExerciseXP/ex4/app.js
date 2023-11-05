import { TodoList } from "./todo.js";

const myTodoList = new TodoList();

myTodoList.addTask("Task 1");
myTodoList.addTask("Task 2");
myTodoList.markTaskComplete(0);
myTodoList.listTasks();
