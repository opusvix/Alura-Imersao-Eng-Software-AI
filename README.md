# 🚀 Imersão Engenharia de Software: Dev na Era da IA | Alura

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-green.svg)](https://flask.palletsprojects.com/)
[![Google Antigravity](https://img.shields.io/badge/Dev_Environment-Google_Antigravity-4285F4.svg)]()
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)]()
[![Alura](https://img.shields.io/badge/Alura-Imersão_Eng_Software_&_IA-blueviolet.svg)](https://www.alura.com.br/)

Repositório central reunindo os projetos e desafios práticos desenvolvidos durante a **Imersão Engenharia de Software da Alura**. Cada desafio explora uma etapa da formação de um desenvolvedor na era da inteligência artificial: desde lógica fundamental e refatoração com IA até a criação de aplicações web completas com testes automatizados.

---

## 🧭 Sumário dos Desafios

| Desafio | Título | Foco / Tecnologias | Diretório |
| :---: | :--- | :--- | :---: |
| **01** | **Calculadora Básica em Python** | Lógica de programação, funções modulares (`def`), controle de fluxo (`if/elif/else`), tratamento de divisão por zero. | [`desafio-01-calculadora-basica/`](./desafio-01-calculadora-basica/) |
| **02** | **Evolução da Calculadora com IA** | Engenharia de prompt, iteração e refatoração de código com IA, implementação do cálculo de porcentagem (`%`). | [`desafio-02-calculadora-porcentagem/`](./desafio-02-calculadora-porcentagem/) |
| **03** | **Lista de Tarefas (To-Do List)** | Desenvolvimento de software com **Google Antigravity**, backend Flask, API RESTful, interface web moderna, feedback visual e **9 testes automatizados**. | [`desafio-03-todo-list/`](./desafio-03-todo-list/) |

---

## 📁 Estrutura do Repositório

O repositório foi organizado como um *monorepo* modular, permitindo navegar e executar cada desafio de maneira independente:

```text
desafio1-Alura-Imersao-Eng-Software-AI/
│
├── README.md                                  # Hub central de documentação da Imersão
├── .gitignore                                 # Arquivos e diretórios ignorados pelo Git
│
├── desafio-01-calculadora-basica/             # 🧮 Desafio 1
│   ├── calculadora.py                         # Código com as 4 operações aritméticas básicas
│   └── README.md                              # Documentação e instruções de execução
│
├── desafio-02-calculadora-porcentagem/        # 📊 Desafio 2
│   ├── calculadora.py                         # Código refatorado com operação de porcentagem (%)
│   └── README.md                              # Documentação e explicações dos prompts utilizados
│
└── desafio-03-todo-list/                      # 📝 Desafio 3
    ├── app.py                                 # Servidor Flask e API RESTful (rotas GET, POST, PATCH, DELETE)
    ├── requirements.txt                       # Dependências do projeto (Flask)
    ├── README.md                              # Documentação técnica detalhada do To-Do List
    ├── templates/
    │   └── index.html                         # Interface visual semântica
    ├── static/
    │   ├── css/style.css                      # Estilização com tema escuro e diferenciação visual
    │   └── js/app.js                          # Lógica de consumo da API, filtros e manipulação do DOM
    └── tests/
        └── test_app.py                        # 9 testes automatizados com unittest
```

---

## ⚡ Como Executar os Desafios

### 1. Clonar o Repositório
```bash
git clone https://github.com/opusvix/desafio1-Alura-Imersao-Eng-Software-AI.git
cd desafio1-Alura-Imersao-Eng-Software-AI
```

---

### 🧮 Executando o Desafio 1 (Calculadora Básica)
```bash
cd desafio-01-calculadora-basica
python calculadora.py
```
> Permite escolher entre Adição (+), Subtração (-), Multiplicação (*) e Divisão (/) diretamente no terminal.

---

### 📊 Executando o Desafio 2 (Calculadora com Porcentagem)
```bash
cd desafio-02-calculadora-porcentagem
python calculadora.py
```
> Inclui a operação 5 para cálculo de porcentagem (`a% de b`), implementada através de refatoração assistida por IA.

---

### 📝 Executando o Desafio 3 (To-Do List com Flask)
```bash
cd desafio-03-todo-list

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor web
python app.py
```
Acesse no seu navegador: **`http://127.0.0.1:5000`**

#### Executar os testes automatizados do Desafio 3:
```bash
python -m unittest discover -s tests -v
```

---

## 🧠 Aprendizados e Destaques

1. **Lógica e Fundamentos (Desafio 1):** Domínio de tipos de dados, modularização em funções e tratamento preventivo de falhas lógicas (*exceptions*).
2. **Engenharia de Prompt e Colaboração com IA (Desafio 2):** Compreensão de como guiar modelos de linguagem para ler código existente, respeitar convenções e adicionar novas *features* sem quebrar o ecossistema.
3. **Engenharia de Software de Ponta a Ponta (Desafio 3):** Uso do **Google Antigravity** para acelerar a concepção e implementação de uma aplicação web completa (Full Stack), refatoração de interface (UX/UI para tarefas concluídas) e validação através de Testes de Software.

---

## 👨‍💻 Autor

Desenvolvido por **Maurício Barros**

- **LinkedIn:** [linkedin.com/in/mauriciodasilvabarros](https://www.linkedin.com/in/mauriciodasilvabarros/)
- **GitHub:** [github.com/opusvix](https://github.com/opusvix)
