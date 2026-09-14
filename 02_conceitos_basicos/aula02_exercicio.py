# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

Valor_conta = float(input("digite o valor da conta: R$ "))
numero_pessoas = int(input("digite o numero de pessoas:"))
valor_por_pessoa = Valor_conta / numero_pessoas
print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")
