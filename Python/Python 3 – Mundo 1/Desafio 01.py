#Desafio 01: Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

nome = input('Informe seu nome: ')
print('Seja bem-vindo',nome)

nome = input('Informe seu nome: ')
print('Seja bem-vindo {}'.format(nome))

nome = input('Informe seu nome: ')
print(f'Seja bem-vindo {nome}')