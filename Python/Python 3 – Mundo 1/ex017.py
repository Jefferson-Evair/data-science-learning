''' Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

CatetoOposto = int(input('Informe o valor do cateto oposto: '))
CatetoAdjacente = int(input('Informe o valor do cateto adjacente: '))

print(f'O valor da Hipotenusa é igual a: {hypot(CatetoOposto, CatetoAdjacente)}')
print('O valor da hipotenusa é igual a: {}'.format(hypot(CatetoOposto, CatetoAdjacente)))
