export function renderTodos(todos, listElement) {

  listElement.innerHTML = "";

  todos.forEach(todo => {

    const li = document.createElement("li");

    li.innerHTML = `
      <span style="${todo.completed ? "text-decoration: line-through" : ""}">
        ${todo.text}
      </span>

      <div>
        <button class="toggle" data-id="${todo.id}">
          ${todo.completed ? "Undo" : "Complete"}
        </button>

        <button class="edit" data-id="${todo.id}">
          Edit
        </button>

        <button class="delete" data-id="${todo.id}">
          Delete
        </button>
      </div>
    `;

    listElement.appendChild(li);

  });
}