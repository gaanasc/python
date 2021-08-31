print ("::: MENU :::")
print ("1 - Logar no sistema")
print ("2 - Sair do sistema")
print ("3 - Recuperar senha")

opcao = int(input("Digite uma das opções do menu: "))

while (opcao < 1 or opcao > 3):
    print ("Opção inválida, digite uma das opções do menu!")
    print ("1 - Logar no sistema")
    print ("2 - Sair do sistema")
    print ("3 - Recuperar senha")
    opcao = int(input("Digite uma das opções do menu: "))
