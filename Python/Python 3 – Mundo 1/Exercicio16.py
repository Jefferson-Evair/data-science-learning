# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input('informe um número qualquer:'))

print('O número informado foi {} e sua porção inteira é {}'.format(num, trunc(num)))