# Escreva um programa com laço `while` que leia números inteiros digitados 
# pelo usuário até que ele digite o número `0` (flag de parada).
# Ao final, o programa deve exibir a soma de todos os números digitados.


# TODO: Desenvolva o acumulador com parada no 0

# from ast import While


soma = 0 
while True:
    numero = int(input("digite um numero inteiro"))
    if numero == 0:
        break
    soma += numero
print(f"A soma de todos os numeros digitados é: {soma}")


