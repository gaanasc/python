# Desejamos coletar duas informações de um usuário. Sua idade e se já tirou
# ou não carta de habilitação. Caso seja maior de 18 anos e tenha carta
# exiba a mensagem "Você pode dirigir!"
# Caso tenha 18 anos e tenha carta.
# Exiba a mensagem: você deve tirar a carta primeiro!
# Caso não tenha 18 anos, exiba a mensagem: Você é menor de idade!

idade = int(input("Informe a sua idade: "))
possuiCarta = input("Digite S caso você possua carta e N caso não possua: ")

if (idade >= 18): # : então
    if(possuiCarta =="S" or possuiCarta == "s"):
        print("Você pode Dirigir!")
    #pass # não if vazio, se não houver condição a mais, usar o "pass"
    else:
        print("Você ainda precisa tirar a carta de motorista!")
else:
    print("Você ainda é menor de idade!")
