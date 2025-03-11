const todoInput = document.getElementById('todo-input');
const addButton = document.getElementById('add-button');
const todoList = document.getElementById('todo-list');

addButton.addEventListener('click', addTodo);

// Load todos from local storage
let todos = JSON.parse(localStorage.getItem('todos')) || [];

// Render initial todos
renderTodos();

function addTodo() {
  const task = todoInput.value;
  if (task) {
    todos.push({ text: task, completed: false });
    localStorage.setItem('todos', JSON.stringify(todos));
    renderTodos();
    todoInput.value = '';
  }
}

function toggleComplete(index) {
  todos[index].completed = !todos[index].completed;
  localStorage.setItem('todos', JSON.stringify(todos));
  renderTodos();
}

function deleteTodo(index) {
  todos.splice(index, 1);
  localStorage.setItem('todos', JSON.stringify(todos));
  renderTodos();
}

function renderTodos() {
  todoList.innerHTML = '';
  todos.forEach((todo, index) => {
    const listItem = document.createElement('li');
    listItem.textContent = todo.text;
    if (todo.completed) {
      listItem.classList.add('completed');
    }

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', () => deleteTodo(index));

    listItem.addEventListener('click', () => toggleComplete(index));
    listItem.appendChild(deleteButton);
    todoList.appendChild(listItem);
  });
}