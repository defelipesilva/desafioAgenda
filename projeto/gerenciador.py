import funcoes

contatos = []

while True:
    print("\nAgenda de Contatos: ")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        funcoes.adicionar(contatos, nome, telefone, email)

    elif escolha == "2":
        funcoes.visualizar(contatos)

    elif escolha == "3":
        funcoes.visualizar(contatos)
        indice = int(input("Informe o identificador do contato que deseja atualizar: "))
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_email = input("Digite o novo email: ")
        funcoes.atualizar(contatos, indice, novo_nome, novo_telefone, novo_email)

    elif escolha == "4":
        funcoes.visualizar(contatos)
        indice = int(input("Informe o identificador do contato que deseja adicionar ou remover dos favoritos: "))
        funcoes.favoritar(contatos, indice)

    elif escolha == "5":
        funcoes.visualizar_favoritos(contatos)

    elif escolha == "6":
        funcoes.visualizar(contatos)
        indice = int(input("Informe o identificador do contato que deseja deletar: "))        
        funcoes.deletar(contatos, indice)

    elif escolha == "7":
        break

    

print("Programa finalizado")