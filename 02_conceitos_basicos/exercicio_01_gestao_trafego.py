"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_investido = float(input("Digite o valor total investido na campanha (em R$): "))
total_cliques = int(input("Digite o número total de cliques obtidos: "))
cpc_medio = valor_investido / total_cliques
print(f"O Custo Por Clique (CPC) médio da campanha é: R$ {cpc_medio:.2f}")