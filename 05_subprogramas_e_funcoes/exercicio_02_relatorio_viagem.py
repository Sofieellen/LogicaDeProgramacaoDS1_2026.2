### 🔹 Exercício 02: Modularizando Relatório de Viagem Técnica para Recife
#Crie duas funções separadas:
#1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_diesel)`: Retorna o valor gasto com combustível para a viagem.
#2. `calcular_custo_alimentacao(qtd_monitores, dias_viagem, diaria_refeicao)`: Retorna o custo total de alimentação da equipe.

#No programa principal, solicite os dados necessários, execute as duas funções e imprima o custo operacional consolidado da viagem técnica.

def calcular_custo_transporte(distancia_km, consumo_kml, preco_litro):
    return (distancia_km / consumo_kml) * preco_litro


def calcular_custo_alimentacao(qtd_pessoas, dias, diaria):
    return qtd_pessoas * dias * diaria


def ler_numero(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem).replace(",", "."))
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")


if __name__ == "__main__":
    print("=== RELATÓRIO DE VIAGEM TÉCNICA PARA RECIFE ===\n")

    distancia = ler_numero("Distância total (km): ")
    consumo = ler_numero("Consumo do veículo (km/l): ")
    preco = ler_numero("Preço do litro do diesel (R$): ")
    monitores = int(ler_numero("Quantidade de monitores: ", int))
    dias = int(ler_numero("Duração da viagem (dias): ", int))
    diaria = ler_numero("Diária de refeição por pessoa (R$): ")

    transporte = calcular_custo_transporte(distancia, consumo, preco)
    alimentacao = calcular_custo_alimentacao(monitores, dias, diaria)

    print("\n" + "=" * 45)
    print("RESUMO DOS CUSTOS DA VIAGEM")
    print("=" * 45)
    print(f"Transporte:  R$ {transporte:,.2f}")
    print(f"Alimentação: R$ {alimentacao:,.2f}")
    print("-" * 45)
    print(f"TOTAL:       R$ {transporte + alimentacao:,.2f}")
    print("=" * 45)