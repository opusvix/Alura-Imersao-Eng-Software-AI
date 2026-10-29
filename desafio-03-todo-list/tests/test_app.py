"""
Testes Automatizados para a aplicação To-Do List.
Executa verificações em todos os endpoints da API (Adicionar, Concluir, Remover e Validações).
"""

import os
import sys
import unittest

# Garante que a raiz do projeto esteja no sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app

class TestTodoListApp(unittest.TestCase):
    def setUp(self):
        """Configura uma nova instância do app antes de cada teste com dados zerados."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_index_page_loads(self):
        """Verifica se a página inicial HTML é carregada com sucesso."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Minha Lista de Tarefas", response.data)

    def test_get_empty_tasks(self):
        """Verifica se a lista começa vazia."""
        response = self.client.get("/api/tasks")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["tasks"], [])
        self.assertEqual(data["total"], 0)

    def test_add_task_success(self):
        """Testa a funcionalidade 1: Adicionar tarefa com sucesso."""
        response = self.client.post("/api/tasks", json={"title": "Estudar Inteligência Artificial"})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], "Estudar Inteligência Artificial")
        self.assertFalse(data["completed"])

    def test_add_task_validation_empty(self):
        """Verifica validação de campo vazio ou espaços em branco."""
        response = self.client.post("/api/tasks", json={"title": "   "})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_toggle_task_completion(self):
        """Testa a funcionalidade 2: Marcar e desmarcar tarefas como concluídas."""
        # Cria a tarefa
        self.client.post("/api/tasks", json={"title": "Revisar código com Antigravity"})

        # Marca como concluída
        response = self.client.patch("/api/tasks/1")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["completed"])

        # Alterna de volta para pendente
        response_toggle_back = self.client.patch("/api/tasks/1")
        self.assertEqual(response_toggle_back.status_code, 200)
        self.assertFalse(response_toggle_back.get_json()["completed"])

    def test_toggle_task_not_found(self):
        """Verifica tentativa de alterar status de tarefa inexistente."""
        response = self.client.patch("/api/tasks/999")
        self.assertEqual(response.status_code, 404)

    def test_delete_task_success(self):
        """Testa a funcionalidade 3: Remover tarefa."""
        # Adiciona tarefa
        self.client.post("/api/tasks", json={"title": "Comprar café"})

        # Remove tarefa existente
        response = self.client.delete("/api/tasks/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("removida com sucesso", response.get_json()["message"])

        # Confirma que a lista agora está vazia
        list_response = self.client.get("/api/tasks")
        self.assertEqual(list_response.get_json()["total"], 0)

    def test_delete_task_not_found(self):
        """Verifica tentativa de remover tarefa inexistente."""
        response = self.client.delete("/api/tasks/999")
        self.assertEqual(response.status_code, 404)

    def test_full_lifecycle_workflow(self):
        """Testa o fluxo completo: criar várias tarefas, concluir uma, remover outra."""
        # 1. Cria 3 tarefas
        self.client.post("/api/tasks", json={"title": "Tarefa 1"})
        self.client.post("/api/tasks", json={"title": "Tarefa 2"})
        self.client.post("/api/tasks", json={"title": "Tarefa 3"})

        # 2. Conclui a Tarefa 2
        self.client.patch("/api/tasks/2")

        # 3. Remove a Tarefa 1
        self.client.delete("/api/tasks/1")

        # 4. Verifica o estado final
        response = self.client.get("/api/tasks")
        tasks = response.get_json()["tasks"]

        self.assertEqual(len(tasks), 2)
        titles = [t["title"] for t in tasks]
        self.assertNotIn("Tarefa 1", titles)
        self.assertIn("Tarefa 2", titles)
        self.assertIn("Tarefa 3", titles)

        # Verifica status da Tarefa 2
        t2 = next(t for t in tasks if t["id"] == 2)
        self.assertTrue(t2["completed"])


if __name__ == "__main__":
    unittest.main()
