"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
from calendar import c
import math

# Leitura dos valores de A, B e C (geralmente informados na mesma linha)
A = float(input("Dgite o valor de A: "))
B = float(input("Dgite o valor de B: "))
C = float(input("Dgite o valor de C: "))

Delta = (B ** 2) - (4 * A * C)

if A == 0 or Delta < 0:
    print("impossivel calcular")
else:
    X1 = (-B + Delta**0.5) / (2 * A)
    X2 = (-B - Delta**0.5) / (2 * A)

    print(f"A sua primeira raiz é: {X1:.5f}")
    print(f"Sua segunda raiz é: {X2:.5f}")

