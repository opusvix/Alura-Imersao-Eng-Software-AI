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

def porcentagem(a, b):
    # Calcula a porcentagem de 'a' sobre 'b' (a% de b)
    return (a * b) / 100


# --- 2. MENU E ENTRADA DE DADOS ---

print("=== CALCULADORA SIMPLES ===")
print("Escolha uma operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
print("5 - Porcentagem (%)")

# O usuário digita a opção desejada
opcao = input("Digite o número da operação (1/2/3/4/5): ")

# --- 3. PROCESSAMENTO E LÓGICA CONDICIONAL ---

# Verificamos se a opção digitada é válida antes de pedir os números
if opcao in ['1', '2', '3', '4', '5']:
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

    elif opcao == '5':
        resultado = porcentagem(num1, num2)
        print(f"\nResultado: {num1}% de {num2} = {resultado}")

else:
    # Caso o usuário digite algo diferente de 1 a 5
    print("\nOpção inválida! Por favor, escolha um número de 1 a 5.")
