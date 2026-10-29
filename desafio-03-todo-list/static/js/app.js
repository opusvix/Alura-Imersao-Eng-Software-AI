/**
 * To-Do List Application Logic
 * Desafio 3 - Alura Imersão Engenharia de Software e IA
 */

document.addEventListener("DOMContentLoaded", () => {
    // Referências aos elementos do DOM
    const taskForm = document.getElementById("task-form");
    const taskInput = document.getElementById("task-input");
    const taskList = document.getElementById("task-list");
    const emptyState = document.getElementById("empty-state");
    const errorMessage = document.getElementById("error-message");
    const filterButtons = document.querySelectorAll(".filter-btn");

    const statTotal = document.getElementById("stat-total").querySelector("strong");
    const statPending = document.getElementById("stat-pending").querySelector("strong");
    const statCompleted = document.getElementById("stat-completed").querySelector("strong");

    // Estado da aplicação
    let tasks = [];
    let currentFilter = "all";

    // 1. Carregar tarefas do backend na inicialização
    fetchTasks();

    // 2. Manipular envio do formulário (Adicionar Tarefa)
    taskForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const title = taskInput.value.trim();

        if (!title) {
            showError("Por favor, digite uma descrição para a tarefa.");
            return;
        }

        clearError();
        await addTask(title);
        taskInput.value = "";
        taskInput.focus();
    });

    // 3. Manipular filtros (Todas, Pendentes, Concluídas)
    filterButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            filterButtons.forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");
            currentFilter = btn.dataset.filter;
            renderTasks();
        });
    });

    // --- Funções de Comunicação com a API ---

    async function fetchTasks() {
        try {
            const response = await fetch("/api/tasks");
            if (!response.ok) throw new Error("Erro ao carregar tarefas.");
            const data = await response.json();
            tasks = data.tasks || [];
            renderTasks();
        } catch (err) {
            console.error(err);
            showError("Não foi possível carregar a lista de tarefas.");
        }
    }

    async function addTask(title) {
        try {
            const response = await fetch("/api/tasks", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ title }),
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.error || "Erro ao adicionar tarefa.");
            }

            const newTask = await response.json();
            tasks.push(newTask);
            renderTasks();
        } catch (err) {
            console.error(err);
            showError(err.message);
        }
    }

    async function toggleTask(id) {
        try {
            const response = await fetch(`/api/tasks/${id}`, {
                method: "PATCH",
            });

            if (!response.ok) throw new Error("Erro ao atualizar o status da tarefa.");

            const updatedTask = await response.json();
            const index = tasks.findIndex((t) => t.id === id);
            if (index !== -1) {
                tasks[index] = updatedTask;
                renderTasks();
            }
        } catch (err) {
            console.error(err);
            showError("Erro ao alterar status da tarefa.");
        }
    }

    async function deleteTask(id) {
        try {
            const response = await fetch(`/api/tasks/${id}`, {
                method: "DELETE",
            });

            if (!response.ok) throw new Error("Erro ao excluir a tarefa.");

            tasks = tasks.filter((t) => t.id !== id);
            renderTasks();
        } catch (err) {
            console.error(err);
            showError("Erro ao remover tarefa.");
        }
    }

    // --- Renderização da Interface Visual ---

    function renderTasks() {
        // Atualiza contadores
        const totalCount = tasks.length;
        const completedCount = tasks.filter((t) => t.completed).length;
        const pendingCount = totalCount - completedCount;

        statTotal.textContent = totalCount;
        statPending.textContent = pendingCount;
        statCompleted.textContent = completedCount;

        // Filtra as tarefas
        const filteredTasks = tasks.filter((task) => {
            if (currentFilter === "pending") return !task.completed;
            if (currentFilter === "completed") return task.completed;
            return true;
        });

        // Limpa a lista atual
        taskList.innerHTML = "";

        // Controla exibição do estado vazio
        if (filteredTasks.length === 0) {
            emptyState.classList.remove("hidden");
        } else {
            emptyState.classList.add("hidden");
        }

        // Renderiza cada item de tarefa
        filteredTasks.forEach((task) => {
            const li = document.createElement("li");
            li.className = `task-item ${task.completed ? "completed" : ""}`;
            li.dataset.id = task.id;

            // Elementos visuais
            const leftContainer = document.createElement("div");
            leftContainer.className = "task-left";

            // Botão de alternar conclusão (Checkmark)
            const toggleBtn = document.createElement("button");
            toggleBtn.className = "toggle-btn";
            toggleBtn.title = task.completed ? "Marcar como pendente" : "Marcar como concluída";
            toggleBtn.innerHTML = task.completed ? "✓" : "";
            toggleBtn.addEventListener("click", () => toggleTask(task.id));

            // Texto da tarefa
            const taskText = document.createElement("span");
            taskText.className = "task-title";
            taskText.textContent = task.title;

            // Tag/Badge de status (Melhoria Visual)
            const badge = document.createElement("span");
            badge.className = "task-status-badge";
            badge.textContent = task.completed ? "Concluída" : "Pendente";

            leftContainer.appendChild(toggleBtn);
            leftContainer.appendChild(taskText);
            leftContainer.appendChild(badge);

            // Botão de Excluir
            const deleteBtn = document.createElement("button");
            deleteBtn.className = "delete-btn";
            deleteBtn.title = "Excluir tarefa";
            deleteBtn.innerHTML = "🗑️";
            deleteBtn.addEventListener("click", () => deleteTask(task.id));

            li.appendChild(leftContainer);
            li.appendChild(deleteBtn);

            taskList.appendChild(li);
        });
    }

    function showError(msg) {
        errorMessage.textContent = msg;
    }

    function clearError() {
        errorMessage.textContent = "";
    }
});
