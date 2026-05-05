''' Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc 

num = float(input('Informe um número qualquer e descubra sua porção inteira: '))

print(f'A porção inteira do número {num} é igual a {trunc(num)}')
print('A porção inteira do número {} é igual a {}'.format(num, trunc(num)))