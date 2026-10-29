"""
Aplicação To-Do List - Desafio 3 Alura Imersão Engenharia de Software e IA.
Desenvolvido com Flask e boas práticas de arquitetura.
"""

from flask import Flask, jsonify, render_template, request

def create_app(initial_tasks=None):
    app = Flask(__name__)

    # Armazenamento em memória para as tarefas
    # Estrutura de cada tarefa: {"id": int, "title": str, "completed": bool}
    tasks = [] if initial_tasks is None else list(initial_tasks)
    next_id = [len(tasks) + 1]

    @app.route("/")
    def index():
        """Renderiza a interface visual da lista de tarefas."""
        return render_template("index.html")

    @app.route("/api/tasks", methods=["GET"])
    def get_tasks():
        """Retorna todas as tarefas cadastradas."""
        return jsonify({"tasks": tasks, "total": len(tasks)}), 200

    @app.route("/api/tasks", methods=["POST"])
    def add_task():
        """Adiciona uma nova tarefa."""
        data = request.get_json(silent=True) or {}
        title = data.get("title", "").strip()

        if not title:
            return jsonify({"error": "O título da tarefa não pode estar vazio."}), 400

        task = {
            "id": next_id[0],
            "title": title,
            "completed": False
        }
        next_id[0] += 1
        tasks.append(task)
        return jsonify(task), 201

    @app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
    def toggle_task(task_id):
        """Alterna ou define o status de conclusão da tarefa."""
        for task in tasks:
            if task["id"] == task_id:
                data = request.get_json(silent=True) or {}
                if "completed" in data:
                    task["completed"] = bool(data["completed"])
                else:
                    task["completed"] = not task["completed"]
                return jsonify(task), 200

        return jsonify({"error": "Tarefa não encontrada."}), 404

    @app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        """Remove uma tarefa pelo seu identificador."""
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                removed_task = tasks.pop(i)
                return jsonify({"message": "Tarefa removida com sucesso.", "task": removed_task}), 200

        return jsonify({"error": "Tarefa não encontrada."}), 404

    # Rota utilitária para testes/reinício de tarefas
    @app.route("/api/tasks/clear", methods=["POST"])
    def clear_tasks():
        tasks.clear()
        next_id[0] = 1
        return jsonify({"message": "Todas as tarefas foram limpas."}), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
