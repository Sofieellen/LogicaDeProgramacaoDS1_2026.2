"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
numero = 0
for valores in range(6):
    numerales = float(input("digite um numero: "))
    if numerales > 0 :
        numero+=numerales
        resposta = numero/6
print(f"media dos numeros digitados {resposta:.1f}")

