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
  
  Abaixo está o código completo da calculadora, estruturado de forma simples, legível e comentado linha por linha. 

---

### Código da Calculadora em Python

```python
# --- 1. DEFINIÇÃO DAS FUNÇÕES (Operações Matemáticas) ---

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    # Verificação para evitar erro de divisão por zero
    if b == 0:
        return "Erro: não é possível dividir por zero!"
    return a / b


# --- 2. MENU E ENTRADA DE DADOS ---

print("=== CALCULADORA SIMPLES ===")
print("Escolha uma operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# O usuário digita a opção desejada
opcao = input("Digite o número da operação (1/2/3/4): ")

# --- 3. PROCESSAMENTO E LÓGICA CONDICIONAL ---

# Verificamos se a opção digitada é válida antes de pedir os números
if opcao in ['1', '2', '3', '4']:
    # Recebemos os números e convertemos para float (números com casas decimais)
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Decidimos qual operação executar com base na escolha
    if opcao == '1':
        resultado = adicao(num1, num2)
        print(f"\nResultado: {num1} + {num2} = {resultado}")

    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print(f"\nResultado: {num1} - {num2} = {resultado}")

    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"\nResultado: {num1} * {num2} = {resultado}")

    elif opcao == '4':
        resultado = divisao(num1, num2)
        print(f"\nResultado: {num1} / {num2} = {resultado}")

else:
    # Caso o usuário digite algo diferente de 1, 2, 3 ou 4
    print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")
```

---

### Explicações detalhadas

#### 1. Quais são os principais componentes do código gerado?

* **Funções (`def`)**: Pequenos blocos de código reaproveitáveis criados com a palavra `def`. Em vez de misturar a matemática no meio do programa, criamos uma função para cada operação (`adicao`, `subtracao`, etc.). Elas recebem dois valores de entrada (parâmetros `a` e `b`) e devolvem o resultado usando a palavra `return`.
* **Variáveis**: Espaços na memória do computador usados para guardar dados temporariamente. No código, usamos variáveis como `opcao`, `num1`, `num2` e `resultado`.
* **Entrada (`input()`)**: Função nativa do Python que pausa a execução e espera o usuário digitar algo pelo teclado.
* **Conversão de Tipos (`float()`):** Por padrão, tudo o que vem do `input()` é texto (*string*). O `float()` converte esse texto em um número real (com decimais), permitindo fazer contas matemáticas.
* **Estruturas Condicionais (`if`, `elif`, `else`)**: São os desvios de caminho. O programa avalia se uma condição é verdadeira ou falsa para decidir qual bloco de código deve executar.
* **Saída (`print()` e f-strings)**: A função `print()` exibe mensagens no terminal. O formato `f"Texto {variavel}"` (f-string) permite misturar texto e valores de variáveis de maneira simples.

---

#### 2. Como a aplicação recebe os números e identifica a operação escolhida?

1. **Identificando a operação:** 
   O programa primeiro usa `opcao = input(...)` para capturar a escolha do usuário como texto (`'1'`, `'2'`, `'3'` ou `'4'`). 
2. **Validando a escolha:** 
   A linha `if opcao in ['1', '2', '3', '4']:` checa se o que foi digitado pertence à lista de opções aceitas. Se o usuário digitar "abc" ou "9", o programa pula direto para o `else` final avisando que a opção é inválida.
3. **Recebendo os números:** 
   Se a opção for válida, o programa solicita os dois números com `input()` e imediatamente os envolve na função `float()`, transformando a entrada em número calculável:
   ```python
   num1 = float(input("Digite o primeiro número: "))
   ```

---
#### 3. Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?

A lógica segue três etapas fundamentais na computação: **Entrada $\rightarrow$ Processamento $\rightarrow$ Saída**.

1. **Roteamento (Decisão):**
   Através de uma cadeia de `if` / `elif` (que significa *"senão, se"*), o programa compara a variável `opcao`:
   * Se for `'1'`, ele chama a função `adicao(num1, num2)`.
   * Se for `'2'`, chama `subtracao(num1, num2)`.
   * E assim sucessivamente.

2. **Tratamento de Exceção Lógica (Divisão por zero):**
   Dentro da função `divisao`, existe uma regra de negócio essencial: computadores não conseguem dividir por zero (isso geraria um erro crítico e travaria o programa). Por isso, colocamos uma checagem preventiva:
   ```python
   if b == 0:
       return "Erro: não é possível dividir por zero!"
   ```

3. **Apresentação:**
   O valor retornado pela função chamada é armazenado na variável `resultado`. Em seguida, a f-string formata uma mensagem amigável mostrando a conta inteira ao usuário:
   ```python
   print(f"\nResultado: {num1} + {num2} = {resultado}")
   ```
   Se `num1` for 10 e `num2` for 5 na soma, a tela mostrará claramente: `Resultado: 10.0 + 5.0 = 15.0`.

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
