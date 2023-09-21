lista_de_compras = []

def listar_compras():
    print("Itens na lista de compras:")
    for i, item in enumerate(lista_de_compras, start=1):
        print(f"{i}. {item}")

while True:
    print("\nOpções:")
    print("1. Adicionar item à lista")
    print("2. Apagar item da lista")
    print("3. Editar item na lista")
    print("4. Listar itens da lista")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        item = input("Digite o item a ser adicionado à lista: ")
        lista_de_compras.append(item)
        print(f"{item} foi adicionado à lista.")

    elif escolha == "2":
        listar_compras()
        indice = int(input("Digite o número do item a ser apagado: ")) - 1
        if 0 <= indice < len(lista_de_compras):
            item_removido = lista_de_compras.pop(indice)
            print(f"{item_removido} foi removido da lista.")
        else:
            print("Número de item inválido.")

    elif escolha == "3":
        listar_compras()
        indice = int(input("Digite o número do item a ser editado: ")) - 1
        if 0 <= indice < len(lista_de_compras):
            novo_item = input("Digite o novo valor: ")
            lista_de_compras[indice] = novo_item
            print("Item editado com sucesso.")
        else:
            print("Número de item inválido.")

    elif escolha == "4":
        listar_compras()

    elif escolha == "5":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")