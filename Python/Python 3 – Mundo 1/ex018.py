''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. '''

from math import sin, cos, tan

angulo = float(input('Informe o valor de um ângulo qualquer: '))

print('O ângulo informado foi {} \n ' \
'O valor valor do seno é {} \n' \
'O valor do cosseno é {} \n' \
'O valor da tangente é {}'.format(angulo, sin(angulo), cos(angulo),tan(angulo)))