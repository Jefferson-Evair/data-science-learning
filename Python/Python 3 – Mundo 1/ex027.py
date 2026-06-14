'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Informe o seu nome completo:')).upper().split()

primeironome = nome[0]
ultimonome = nome[len(nome) -1 ]

print(f'Primeiro nome: {primeironome}')
print(f'Último nome: {ultimonome}')