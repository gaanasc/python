listas = [[]] #uma lista de lista

while True:
    print("1-Cadastrar pessoa")
    print("2-Lista Cadastros")
    print("3-Procurar Pessoa Especifica")
    op = int(input('Escolha uma opção: '))#Escolha da opcao
    if op == 1:
        nova = [] # cria uma lista para adicionar o id, nome e idade da pessoa
        id = input("Id da pessoa: ")
        nome = input("Digite o nome da pessoa: ")
        idade = input("Idade da pessoa: ")
        print('')
        nova.append(id)
        nova.append(nome)
        nova.append(idade)
        listas.append(nova)#Adiciona a lista criada com o cadastro da pessoa dentro da lista

    elif op == 2:        
        for mostrar in listas:
            try:
                print("Nome: %s - Idade: %s - ID: %s"%(mostrar[1],mostrar[2],mostrar[0]))
                print('')
            except:
                print("Essa pessoa não possui algum dos valores a seguir: Nome, Idade, ID")
                print('')

    elif op == 3:
        id = input("Digite o id da pessoa desejada: ")
        for mostrar in listas:
            if id in mostrar:
                try:
                    print('')
                    print('segue a lista')
                    print('')
                    print("Nome: %s - Idade: %s - ID: %s"%(mostrar[1],mostrar[2],mostrar[0]))
                    print('')
                except:
                    print("Essa pessoa não possui algum dos valores a seguir: Nome, Idade, ID")
                    print('')