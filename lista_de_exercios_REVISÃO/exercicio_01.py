#1. Calculadora de Frete de E-commerce 

# Uma loja virtual precisa de um sistema para calcular o valor do frete.
# Crie uma função que receba a distância em quilômetros e o tipo de
# cliente ("Padrão" ou "VIP"). 
# A regra é: R0, 50 𝑝𝑜𝑟 𝑘𝑚 𝑟𝑜𝑑𝑎𝑑𝑜. 
# 𝑆𝑒 𝑎 𝑑𝑖𝑠𝑡â𝑛𝑐𝑖𝑎 𝑓𝑜𝑟 𝑚𝑎𝑖𝑜𝑟 𝑞𝑢𝑒 100𝑘𝑚, ℎá 𝑢𝑚𝑎 𝑡𝑎𝑥𝑎 𝑓𝑖𝑥𝑎 𝑎𝑑𝑖𝑐𝑖𝑜𝑛𝑎𝑙 𝑑𝑒 𝑅 15,00.
# Clientes VIP recebem 20% de desconto no valor final do frete. 
# Peça para o usuário inserir os dados e exiba o resultado utilizando a função criada.



#Distancia = input("digite a distancia em km da moradia:")
#cliente = input("digite o seu tipo de cliente (padrão ou vip):")
#valor = (Distancia * 0.50)
#while True:
#    M=valor > 100
#    if M + 15:
#        print=("o valor do frete sera: {M}")
#    if cliente == "vip":
#        print=("o valor do frete sera {valor} - 20% de desconto")

Distancia = float(input("digite a distancia em km da moradia:"))
cliente = input("digite o seu tipo de cliente (padrão ou vip):")
def frete(distancia, cliente):
    valor = distancia * 0.50
    if distancia > 100:
        valor = valor + 15.00
    if cliente .lower() == "vip":
        valor = float(valor - (valor * 0.20))
    return valor
resultado = frete(Distancia, cliente)
print(f"o valor do frete sera: R$ {resultado:.2f}")
