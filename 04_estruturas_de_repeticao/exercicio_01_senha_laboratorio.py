"""
EXERCÍCIO 01: Senha Fixa do Laboratório
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Repita a leitura da senha até que o usuário digite a senha correta (2002).
Para cada tentativa incorreta, imprima "Senha Invalida".
Ao acertar, imprima "Acesso Permitido" e finalize o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
from operator import truediv


senha= 2002
while True:
    numero=int(input("digite sua senha"))
    if numero==senha:
        print("senha valida")
        break
    else:
        print("senha invalida")