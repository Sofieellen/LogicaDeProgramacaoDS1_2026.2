"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

if salario_atual <= 400.00:
    percentual = 15
elif salario_atual <= 800.00:
    percentual = 12
elif salario_atual <= 1200.00:
    percentual = 10
elif salario_atual <= 2000.00:
    percentual = 7
else:
    percentual = 4

valor_reajuste = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_reajuste

print(f"\nNovo salário: R$ {novo_salario:.2f}")
print(f"Valor do reajuste ganho: R$ {valor_reajuste:.2f}")
print(f"Percentual aplicado: {percentual}%")