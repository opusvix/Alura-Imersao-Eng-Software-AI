# 📊 Desafio 2: Evolução da Calculadora com IA (Cálculo de Porcentagem)

Evolução da calculadora básica através de engenharia de prompt e refatoração assistida por Inteligência Artificial, adicionando a operação de cálculo percentual.

---

## 🎯 Objetivo do Desafio
Aprender a iterar sobre um código existente em parceria com a IA:
- Formular prompts para guiar o assistente de IA na compreensão do código legado.
- Implementar com precisão uma nova funcionalidade matemática (`def porcentagem(a, b)`).
- Atualizar o menu interativo, a validação de opções e a formatação do resultado via *f-string*.

---

## 🛠️ Código Implementado (Nova Função)
```python
def porcentagem(a, b):
    # Calcula a porcentagem de 'a' sobre 'b' (a% de b)
    return (a * b) / 100
```

---

## 🚀 Como Executar

```bash
python calculadora.py
```

---

## 💻 Exemplo de Execução
```text
=== CALCULADORA SIMPLES ===
Escolha uma operação:
1 - Adição (+)
2 - Subtração (-)
3 - Multiplicação (*)
4 - Divisão (/)
5 - Porcentagem (%)
Digite o número da operação (1/2/3/4/5): 5

Digite o primeiro número: 15
Digite o segundo número: 200

Resultado: 15.0% de 200.0 = 30.0
```
