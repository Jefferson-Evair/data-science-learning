# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa. 

from math import hypot

cateto_oposto = float(input('Informe o cateto oposto:'))
cateto_adjacente = float(input('Informe o cateto adjacente:'))

print('O valor da hipotenusa é igual a: {}'.format(hypot(cateto_oposto, cateto_adjacente)))