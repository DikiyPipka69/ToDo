const API_URL = "http://127.0.0.1:8000";

const form = document.getElementById("task-form");
const titleInput = document.getElementById("task-title");
const list = document.getElementById("task-list");

// загрузить список задач с бэкенда
async function loadTasks() {
    const res = await fetch(`${API_URL}/tasks`);
    const tasks = await res.json();
    renderTasks(tasks);
}

// отрисовать задачи в списке
function renderTasks(tasks) {
    list.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        if (task.done) li.classList.add("done");
        li.innerHTML = `<span>${task.title}</span>`;
        list.appendChild(li);
    });
}

// отправить новую задачу на бэкенд
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const title = titleInput.value.trim();
    if (!title) return;

    await fetch(`${API_URL}/tasks`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: Date.now(), title, done: false })
    });

    titleInput.value = "";
    loadTasks();
});

loadTasks();

// когда добавишь роуты PUT /tasks/{id} (переключить done)
// и DELETE /tasks/{id} (удалить) — вернёмся сюда и допишем обработчики