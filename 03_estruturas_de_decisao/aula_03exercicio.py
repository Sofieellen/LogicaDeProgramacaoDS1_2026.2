# TODO: Implemente o menu utilizando match-case ou elif
opcao = float(input("Digite o numero da opção desejada (1 - livro, 2 - emprestimo, ou 3 - devolução): "))
# Desenvolva a estrutura de seleção aqui
match opcao:
    case 1:
        print("a opção escolhida foi consultar livro.")
    case 2:
        print("a opção escolhida foi realizar emprestimo.")
    case 3:
        print("a opção escolhida foi devolução do livro.")
    case _: 
        print("Opção inválida!")