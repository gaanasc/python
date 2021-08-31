# Crie um sistema que dada uma nota informada pelo usuário
# Converta ela em um conceito conforme as regras da tabela:
# Conceito A: 10
# Conceito B: De 9 a 9.9
# Conceito C: De 7 a 8.9
# Conceito D: De 6 a 6.9
# Conceito F: De 5 a 5.9
# Conceito I: De 0 a 4.9

nota = float(input("Digite a sua nota de 0 a 10: "))
conceito = "Nota inválida!"

if (nota == 10):
    conceito = "A"
    # "conceito = "A"", O valor substitui o valor inicial da variável
elif (nota >= 9.0 and nota <= 9.9):
    conceito = "B"
elif (nota >= 7.0 and nota <= 8.9):
    conceito = "C"
elif (nota >= 6.0 and nota <= 6.9):
    conceito = "D"
elif (nota >= 5.0 and nota <= 5.9):
    conceito = "F"
elif (nota >= 0.0 and nota <= 4.9):
    conceito = "I"
else:
    print("Você informou uma nota inválida!")


print("O seu conceito é: ", conceito)