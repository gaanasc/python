from sys import exit

produtos = {1: 'arroz', 2: 'feijao'}

def add_produto(c, n):
  produtos.update({c : n})
  resp == 0

while True:
  # print('-='*15)
  print('[1] Add Novo produto')
  print('[2] Consultar produto')
  print('[3] Deletar produto')
  print('[4] Sair')


  resp = input('Opção: ')
  if resp == '1':
    nome = input('Nome do produtos: ')
    codigo = input('Código: ')
    add_produto(codigo, nome)
  elif resp == '2':
    print('\n' , produtos)
  elif resp == '3':
    prod = input('Digite o código do produto: ')
    del(produtos[(produtos)])
  elif resp == '4':
    print("Você saiu do programa")
    exit(1)   

