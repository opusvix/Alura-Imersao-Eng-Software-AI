# ========================================================
# DESAFIO 1: CALCULADORA BÁSICA EM PYTHON
# Imersão Engenharia de Software: Dev na Era da IA - Alura
# ========================================================

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

def main():
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
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("\nErro: Entrada inválida! Por favor, digite apenas números válidos.")
            return

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
        print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")


if __name__ == "__main__":
    main()
