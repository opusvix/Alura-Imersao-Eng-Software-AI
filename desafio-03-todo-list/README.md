# 📝 Desafio 3: Lista de Tarefas (To-Do List) com Google Antigravity

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-green.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)]()
[![Alura](https://img.shields.io/badge/Alura-Imersão_Eng_Software_&_IA-blueviolet.svg)](https://www.alura.com.br/)

Projeto prático desenvolvido durante a **Imersão Engenharia de Software & IA da Alura**, utilizando o **Google Antigravity** como assistente e ambiente de desenvolvimento inteligente com engenharia de software assistida por inteligência artificial.

Repositório Oficial: [https://github.com/opusvix/desafio1-Alura-Imersao-Eng-Software-AI](https://github.com/opusvix/desafio1-Alura-Imersao-Eng-Software-AI)

---

## 📖 Descrição

Esta aplicação é uma **Lista de Tarefas (To-Do List)** intuitiva, responsiva e moderna. O objetivo principal do desafio foi experimentar o ciclo completo de desenvolvimento de software em parceria com IA:
1. **Compreensão e especificação** de requisitos funcionais simples.
2. **Desenvolvimento guiado** com arquitetura clara e tecnologias simples e acessíveis para iniciantes.
3. **Iteração e evolução**: solicitação de refinamento de interface com feedback visual entre tarefas pendentes e concluídas.
4. **Validação contínua**: implementação e execução de testes automatizados para assegurar a qualidade e estabilidade da aplicação.

---

## 🔍 Visão Geral

A aplicação entrega uma interface gráfica limpa, estilizada com tons modernos (*dark mode*), com as seguintes funcionalidades essenciais:

- **➕ Adicionar Tarefas:** Campo interativo para digitação de novas atividades com validação contra campos em branco.
- **✅ Marcar como Concluída / Pendente:** Alternância rápida com feedback imediato de estilo (tachado, badge de status e cor diferenciada).
- **🗑️ Remover Tarefas:** Exclusão individual de tarefas que não são mais necessárias.
- **📊 Painel de Métricas e Filtros:** Contadores em tempo real (Total, Pendentes e Concluídas) e abas de filtragem para organizar a visualização.
- **🧪 Cobertura de Testes Automatizados:** Suíte com 9 testes unitários cobrindo o backend Flask e as operações da API REST.

---

## 📁 Estrutura do Projeto

O projeto foi estruturado seguindo o princípio da separação de responsabilidades (SoC - *Separation of Concerns*), garantindo facilidade de entendimento e manutenção:

```text
desafio3-todo-list/
├── app.py                     # Servidor backend em Flask e API RESTful
├── requirements.txt           # Dependências do projeto (Flask)
├── README.md                  # Documentação completa do projeto
├── templates/
│   └── index.html             # Estrutura HTML semântica da aplicação
├── static/
│   ├── css/
│   │   └── style.css          # Estilização visual, tema escuro e diferenciação de estados
│   └── js/
│       └── app.js             # Lógica cliente: consumo da API, manipulação do DOM e filtros
└── tests/
    └── test_app.py            # Testes automatizados com unittest para todas as funcionalidades
```

---

## ⚙️ Requisitos e Instalação passo a passo

### Pré-requisitos
- **Python 3.10 ou superior** instalado na sua máquina ([Download Python](https://www.python.org/downloads/)).
- Gerenciador de pacotes `pip` (geralmente instalado junto ao Python).
- Navegador web moderno (Chrome, Edge, Firefox, Safari).

### Passo 1: Clonar ou acessar o repositório
Abra o terminal e faça o clone do repositório:
```bash
git clone https://github.com/opusvix/desafio1-Alura-Imersao-Eng-Software-AI.git
cd desafio1-Alura-Imersao-Eng-Software-AI
```
*(Caso esteja executando diretamente na pasta do desafio 3, entre no diretório correspondente).*

### Passo 2: (Opcional, mas recomendado) Criar um Ambiente Virtual
No Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
No Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar as Dependências
Com o ambiente ativado, instale o Flask via `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🚀 Como Usar

### 1. Iniciar a Aplicação
No terminal, execute o comando:
```bash
python app.py
```
Você verá uma saída similar a:
```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 2. Acessar a Interface Visual
Abra seu navegador e acesse:
```text
http://127.0.0.1:5000
```

### 3. Experimentar as Funcionalidades
1. **Adicione uma tarefa:** Digite por exemplo `"Estudar Inteligência Artificial"` e clique em **+ Adicionar** (ou pressione `Enter`).
2. **Conclua a tarefa:** Clique no círculo de seleção à esquerda da tarefa. Note que ela ficará com o texto riscado, badge verde `"CONCLUÍDA"` e opacidade suavizada.
3. **Filtre suas tarefas:** Use os botões no topo para ver apenas **Pendentes**, **Concluídas** ou **Todas**.
4. **Remova a tarefa:** Clique no ícone de lixeira (🗑️) para excluir a tarefa da lista.

### 4. Executar os Testes Automatizados
Para verificar a integridade da aplicação e garantir que todas as funções continuam operando normalmente:
```bash
python -m unittest discover -s tests -v
```

Saída esperada:
```text
test_add_task_success (test_app.TestTodoListApp.test_add_task_success) ... ok
test_add_task_validation_empty (test_app.TestTodoListApp.test_add_task_validation_empty) ... ok
test_delete_task_not_found (test_app.TestTodoListApp.test_delete_task_not_found) ... ok
test_delete_task_success (test_app.TestTodoListApp.test_delete_task_success) ... ok
test_full_lifecycle_workflow (test_app.TestTodoListApp.test_full_lifecycle_workflow) ... ok
test_get_empty_tasks (test_app.TestTodoListApp.test_get_empty_tasks) ... ok
test_index_page_loads (test_app.TestTodoListApp.test_index_page_loads) ... ok
test_toggle_task_completion (test_app.TestTodoListApp.test_toggle_task_completion) ... ok
test_toggle_task_not_found (test_app.TestTodoListApp.test_toggle_task_not_found) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.058s

OK
```

---

## 💡 Aprendizados com o Google Antigravity
Como aluno de Inteligência Artificial e Engenharia de Software, o desenvolvimento deste desafio permitiu vivenciar:
- **Pair Programming com IA:** O Antigravity atuou como um parceiro técnico acelerando a criação da estrutura inicial e auxiliando na implementação de melhorias sob demanda.
- **Refatoração com Foco em UX:** A implementação da distinção visual das tarefas demonstrou como pequenas mudanças em CSS e manipulação de classes no JavaScript impactam diretamente a usabilidade do usuário.
- **Garantia de Qualidade com Testes:** A criação de testes unitários automatizados assegura que futuras alterações ou novas funcionalidades não quebrem o comportamento esperado do sistema.
