from linecache import clearcache
from wsgiref.types import InputStream

estoque_produtos = { # { == dicionario
    1 : {"Nome" : "Camisa do Brasil", "Preço" : 400.00, "Quantidade" : 500},
    2 : {"Nome" : "Camisa do Cabo verde", "Preço" : 130.00, "Quantidade" : 250},
    3 : {"Nome" : "Camisa da Espanha", "Preço" : 350.00, "Quantidade" : 430}
}

carrinho = []
subtotal = 0

while True:
    print("*"*30)
    print("Seja bem vindo a minha loja")
    print("[1] Visualizar estoque ao carrinho.")
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

            for i in carrinho:
                print(f"{i["Qtd"]} X {i["Nome"]} no valor de R$ {i["Preço"]}(cada) \n Total R${i["preço_total"]}")
                if subtotal !=  i ["Preço_total"]:
                 subtotal += i ["preço_total"]
            print(f"Subtotal da Compra R${subtotal}")
        else:
            print("Carrinho Vazio!")


    elif opcao == 4:
        print("finalizando compra!")
        if not carrinho:
            print("O seu carrinho ainda está vazio. Não é possivel finalizar a compra")
        else:
            desconto = 0
            cupom = input("Digite um cupom de desconto ou caso não tenha um, pressione enter.")
            if cupom == "DEV10":
                desconto = subtotal * 0.1
                print("Cupom válido: Você obteve 10% de desconto")
            elif cupom == "DEV20" and subtotal > 500:
                desconto = subtotal * 0.2
                print("Cupom Válido: Você obteve 20% de desconto")
            elif len (cupom) == 0: # Lene conta os caracteres
                print("Nenhum cupom foi adicionado")
            else:
                print("Cupom Inválido. Nenhum desconto foi adicionado")
            print("-----RESUMO DO PEDIDO -----")
            print(f" Subtotal da compra : R$ {subtotal: .2f}")
            print(f" Desconto : R$ {subtotal: .2f}")
            print(f" Valor final : R$ {subtotal - desconto : .2f}")
            print("-"*30)
            carrinho.clear()


    elif opcao == 0:
        print("Saindo do sistema...")
        break

    else:
            print("Opção inválida")



















