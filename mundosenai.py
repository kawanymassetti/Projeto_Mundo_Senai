estoque = {}

while True:
    print("\n===== CONTROLE DE ESTOQUE INDUSTRIAL =====")
    print("1 - Cadastrar produto")
    print("2 - Consultar estoque")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade inicial: "))

        estoque[nome] = quantidade
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- ESTOQUE ATUAL ---")

        for produto, quantidade in estoque.items():
            print(produto, "-", quantidade, "unidades")

        if not estoque:
            print("Estoque vazio!")

    elif opcao == "3":
        nome = input("Nome do produto: ")

        if nome in estoque:
            quantidade = int(input("Quantidade de entrada: "))
            estoque[nome] += quantidade
            print("Entrada registrada!")
        else:
            print("Produto não encontrado!")

    elif opcao == "4":
        nome = input("Nome do produto: ")

        if nome in estoque:
            quantidade = int(input("Quantidade de saída: "))

            if quantidade <= estoque[nome]:
                estoque[nome] -= quantidade
                print("Saída registrada!")
            else:
                print("Quantidade insuficiente no estoque!")
        else:
            print("Produto não encontrado!")

    elif opcao == "5":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")