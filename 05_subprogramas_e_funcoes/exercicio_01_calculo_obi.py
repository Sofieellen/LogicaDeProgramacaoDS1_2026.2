"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:

def calcular_pontucao_total(fase1, fase2 , fase3):
    return fase1 + fase2 + fase3 
resultado1 = calcular_pontucao_total(80, 90, 100)
print(f"teste 1: {resultado1}")
resultado2 = calcular_pontucao_total(100, 0, 85)
print(f"Teste 2: {resultado2}")
resultado3 = calcular_pontucao_total(75.5, 82.0, 91.5)
print(f"Teste 3: {resultado3}")