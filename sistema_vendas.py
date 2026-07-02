estoque_produtos = { # { == dicionario
    1 : {"Nome" : "Camisa do Brasil", "Preço" : 400.00, "Quantidade" : 500},
    2 : {"Nome" : "Camisa do Cabo verde", "Preço" : 130.00, "Quantidade" : 250},
    3 : {"Nome" : "Camisa da Espanha", "Preço" : 350.00, "Quantidade" : 430}
}

carrinho = []

while True:
    print("*"*30)
    print("Seja bem vindo a minha loja")
    print("[1] Visualizar item ao carrinho.")
    print("[2] Adicionar item ao carrinho")
    print("[3] Visualizar carrinho.")
    print("[4] Finalizar compra.")
    print("[0] Sair do sistema.")

    opcao = int(input ("Escolha uma opção: "))

    if opcao == 1:
        print("Visualizando Estoque!")
        print("ID    |    NOMES                | VALOR     | QUANTIDADE")
        for chave, valor in estoque_produtos.items():
            print(f"{chave}  |  {valor}")


    elif opcao == 2:
        print("Adicionando items ao carrinho.")
        id_produto = int(input("Qual produto deseja comprar? "))
        if id_produto in estoque_produtos:
            qtd_produto = int(input("Quantas unidades você deseja? "))
            if qtd_produto <= 0:
                print("Quantidade inválida!")
            elif qtd_produto <= estoque_produtos[id_produto] ["Quantidade"]:
                carrinho.append(estoque_produtos[id_produto])
                estoque_produtos [id_produto]["Quantidade"] -= qtd_produto


    elif opcao == 3:
        print("Visualizar carrinho.")
    elif opcao == 4:
        print("Finalizar compra.")
    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida")






