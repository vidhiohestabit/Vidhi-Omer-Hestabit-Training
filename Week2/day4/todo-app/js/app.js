import { getTodos, saveTodos } from "./storage.js";
import { renderTodos } from "./ui.js";
import { debounce, throttle, groupBy } from "./utils.js";

const todoInput = document.getElementById("todoInput");
const addBtn = document.getElementById("addBtn");
const searchInput = document.getElementById("searchInput");

const pendingList = document.getElementById("pendingList");
const completedList = document.getElementById("completedList");

let todos = getTodos().map(todo => ({
  ...todo,
  id: String(todo.id)
}));

function renderGroupedTodos(data = todos) {

  const grouped = groupBy(data, "completed");

  const pending = grouped.false || [];
  const completed = grouped.true || [];

  renderTodos(pending, pendingList);
  renderTodos(completed, completedList);
}

renderGroupedTodos();


// ADD TODO
addBtn.addEventListener("click", () => {

  const text = todoInput.value.trim();
  if (!text) return;

  const newTodo = {
    id: Date.now().toString(),
    text,
    completed: false
  };

  todos = [...todos, newTodo];

  saveTodos(todos);
  renderGroupedTodos();

  todoInput.value = "";
});


// DELETE + EDIT + TOGGLE
document.addEventListener("click", (e) => {

  const button = e.target.closest("button");
  if (!button) return;

  const id = button.dataset.id;

  // DELETE
  if (button.classList.contains("delete")) {
    todos = todos.filter(todo => todo.id !== id);
  }

  // EDIT
  if (button.classList.contains("edit")) {

    const todoToEdit = todos.find(todo => todo.id === id);
    if (!todoToEdit) return;

    const updatedText = prompt("Edit Todo:", todoToEdit.text);

    if (updatedText !== null && updatedText.trim() !== "") {
      todos = todos.map(todo =>
        todo.id === id
          ? { ...todo, text: updatedText.trim() }
          : todo
      );
    }
    else {
      todoToEdit.text=[];
    }
  }

  // TOGGLE COMPLETE
  if (button.classList.contains("toggle")) {

    todos = todos.map(todo =>
      todo.id === id
        ? { ...todo, completed: !todo.completed }
        : todo
    );
  }

  saveTodos(todos);
  renderGroupedTodos();
});


// SEARCH
searchInput.addEventListener(
  "input",
  debounce((e) => {

    const value = e.target.value.toLowerCase();

    const filtered = todos.filter(todo =>
      todo.text.toLowerCase().includes(value)
    );

    renderGroupedTodos(filtered);

  }, 300)
);

//throttle

window.addEventListener(
  "scroll",
  throttle(() => {
    console.log("User is scrolling...");
  }, 500)
);