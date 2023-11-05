export class TodoList {
  constructor() {
    this.tasks = [];
  }

  addTask(task) {
    this.tasks.push({ task, complete: false });
  }

  markTaskComplete(index) {
    if (index >= 0 && index < this.tasks.length) {
      this.tasks[index].complete = true;
    }
  }

  listTasks() {
    console.log("Tasks:");
    this.tasks.forEach((task, index) => {
      const status = task.complete ? "Complete" : "Incomplete";
      console.log(`${index + 1}. ${task.task} - ${status}`);
    });
  }
}
