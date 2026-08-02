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
        li.className = "task-item";
        if (task.done) li.classList.add("done");

        li.innerHTML = `
            <button class="check-circle" aria-label="toggle"></button>
            <span class="task-title">${task.title}</span>
            <button class="delete-btn" aria-label="delete">
                <svg viewBox="0 0 24 24" width="18" height="18">
                    <path d="M3 6h18M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2m2 0v14a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V6h12z"
                          fill="none" stroke="currentColor" stroke-width="1.8"
                          stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </button>
        `;

        // клик по кружочку — переключить done
        li.querySelector(".check-circle").addEventListener("click", () => toggleTask(task.id));

        // клик по мусорке — удалить с анимацией
        li.querySelector(".delete-btn").addEventListener("click", () => removeTask(task.id, li));

        list.appendChild(li);
    });
}

// переключить статус задачи
async function toggleTask(id) {
    await fetch(`${API_URL}/tasks/${id}`, { method: "PUT" });
    loadTasks();
}

// удалить задачу с анимацией исчезновения
function removeTask(id, li) {
    li.classList.add("removing");
    setTimeout(async () => {
        await fetch(`${API_URL}/tasks/${id}`, { method: "DELETE" });
        loadTasks();
    }, 280);
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