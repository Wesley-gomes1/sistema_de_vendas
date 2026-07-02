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

    opcao = int(input("Escolha uma opção: "))

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
                item = {
                    "Qtd" : qtd_produto,
                    "Nome" : estoque_produtos [id_produto] ["Nome"],
                    "Preço" : estoque_produtos [id_produto] ["Preço"],
                    "Preço_total" : qtd_produto * estoque_produtos [id_produto] ["Preço"]
                }
                carrinho.append(estoque_produtos[id_produto])
                estoque_produtos [id_produto]["Quantidade"] -= qtd_produto

                print(item)
            else:
                print(f"quantidade indisponivel, temos apenas {estoque_produtos[id_produto]["quantidade"]} no estoque")
        else:
            print("ID informado não existe no estoque!")


    elif opcao == 3:
        if carrinho:
            print("Visualizando carrinho.")
            subtotal = 0
            for i in carrinho:
                print(f"{i["qtd"]}X {i["Nome"]} no valor de R$ {i["Preço"]}(cada)\nTotal R${i["preço_total"]}")
                subtotal += i ["preço_total"]
            print(f"Subtotal da Compra R${subtotal}")
        else:
            print("Carrinho Vazio")


    elif opcao == 4:
        print("Finalizar compra.")


    elif opcao == 0:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida")






