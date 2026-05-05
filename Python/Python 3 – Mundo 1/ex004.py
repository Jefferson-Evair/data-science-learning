# Exercício 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

InfoTeclado = input('Digite algo para descobrir o tipo primitivo:')

print(f'O tipo primitivo é: {type(InfoTeclado)}')
print(f'Tem apenas espaços? {InfoTeclado.isspace()}')

print('É número? {}'.format(InfoTeclado.isnumeric()))
print('É alfanumérico? {}'.format(InfoTeclado.isalnum()))