# 🧮 Calculadora Básica em Python

Uma aplicação simples de terminal desenvolvida em Python para realizar as quatro operações matemáticas fundamentais. Projeto ideal para quem está iniciando os estudos em lógica de programação.

---

## 📖 Descrição

Este projeto foi criado com fins pedagógicos para praticar os conceitos fundamentais de Python e atender ao Desafio-d0-dia 1 da Imersão Engenharia de Software: Dev na Era da IA da @Alura. 
A aplicação roda diretamente na linha de comando (terminal), interagindo com o usuário através de menus numéricos para coletar entradas, realizar o cálculo desejado e exibir o resultado formatado na tela.

---

## 🔍 Visão Geral

A calculadora aplica na prática conceitos fundamentais da programação:

- **Modularização com Funções (`def`):** Separação de responsabilidades criando uma função exclusiva para cada operação aritmética.
- **Entrada e Conversão de Dados (`input` / `float`):** Coleta de parâmetros via teclado e conversão de strings para tipos numéricos com ponto flutuante.
- **Estruturas Condicionais (`if` / `elif` / `else`):** Controle de fluxo para validação das escolhas do menu e tratamento de regras de negócio (como impedir a divisão por zero).
- **Interpolação de Strings (f-strings):** Apresentação clara e elegante dos dados de saída no terminal.

---

## 📁 Estrutura do Projeto

```text
calculadora-python/
│
├── calculadora.py      # Código-fonte principal da aplicação
└── README.md           # Documentação do projeto

```

## ⚙️ Requisitos e Instalação

### Pré-requisitos
Para executar o projeto, você precisará ter instalado em sua máquina:
Python 3.8+ instalado.
Git (opcional, para clonar o repositório).
Atenção (Usuários Windows): Durante a instalação do Python, certifique-se de marcar a opção "Add python.exe to PATH".
### Instalação Passo a Passo
1. Clone o repositório (ou baixe os arquivos em formato ZIP):
code
Bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
2. Acesse a pasta do projeto:
code
Bash
cd NOME-DO-REPOSITORIO
3. Verifique se o Python está acessível no terminal:
code
Bash
python --version
(Caso não reconheça, tente usar python3 --version).

## 🚀 Como Usar

1.Execute o script principal:
No terminal, dentro da pasta do projeto, digite:
code
Bash
python calculadora.py
(No Linux/Mac, utilize python3 calculadora.py se necessário).
2. Siga as instruções do terminal:

- Escolha o número da operação desejada (1 a 4).
- Digite o primeiro número e aperte Enter.
- Digite o segundo número e aperte Enter.
- O resultado será exibido imediatamente na tela.
## Exemplo de Uso:
```
=== CALCULADORA SIMPLES ===

Escolha uma operação:

1 - Adição (+)
2 - Subtração (-)
3 - Multiplicação (*)
4 - Divisão (/)
Digite o número da operação (1/2/3/4): 1

Digite o primeiro número: 25
Digite o segundo número: 10

Resultado: 25.0 + 10.0 = 35.0
```

## 👨‍💻 Autor

Desenvolvido por Maurício Barros

Entre em contato ou acompanhe meus estudos:

LinkedIn: https://www.linkedin.com/in/mauriciodasilvabarros/

GitHub: https://github.com/opusvix