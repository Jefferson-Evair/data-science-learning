#Desafio 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sonbre ele.

InfoTeclado = input('Digite algo para saber o seu tipo primitivo:')

print(f'O tipo primitivo do valor informado é:{type(InfoTeclado)}')

print(f'É número? {InfoTeclado.isnumeric()}')
print(f'É alfanumérico? {InfoTeclado.isalnum()}')
print('É letra? {}'.format(InfoTeclado.isalpha()) )