def adicionar(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionada com sucesso!")
    return

def visualizar(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✅" if contato["favorito"] else "❌"
        print(f"{indice}. [{status}] {contato["nome"]}")
    return 

def atualizar(contatos, indice, novo_nome, novo_telefone, novo_email):
    indice_ajuste = indice - 1
    if indice_ajuste >= 0 and indice_ajuste < len(contatos):
        contatos[indice_ajuste]["nome"] = novo_nome
        contatos[indice_ajuste]["telefone"] = novo_telefone
        contatos[indice_ajuste]["email"] = novo_email
        print(f"Contato {indice} atualizada para {novo_nome}")
    else:
        print("Contato não encontrada")    
    return

def favoritar(contatos, indice):
    indice_ajuste = indice - 1
    if indice_ajuste >= 0 and indice_ajuste < len(contatos) and contatos[indice_ajuste]["favorito"] == False:
        contatos[indice_ajuste]["favorito"] = True
        print(f"Contato {indice_ajuste} adicionado aos favoritos")
    elif indice_ajuste >= 0 and indice_ajuste < len(contatos) and contatos[indice_ajuste]["favorito"] == True:
        contatos[indice_ajuste]["favorito"] = False
        print(f"Contato {indice_ajuste} removido dos favoritos")
    else:
        print("Contato não encontrada")
    return

def visualizar_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✅" if contato["favorito"] else "❌"
        if contato["favorito"] == True:
            print(f"{indice}. [{status}] {contato["nome"]}")
    return 

def deletar(contatos, indice):
    indice_ajuste = indice - 1
    if indice_ajuste >= 0 and indice_ajuste < len(contatos):
        del contatos[indice_ajuste]
        print(f"Contato {indice_ajuste} deletado")
    else:
        print("Contato não encontrada")
    return