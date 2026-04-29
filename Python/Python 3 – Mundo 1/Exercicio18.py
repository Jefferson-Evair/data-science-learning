# Faça um programa que leia um ângulo qualquer e mostre na tela o calor do seno, cosseno e tangente de ângulo. 

from math import cos, sin, tan

angulo = float(input('Informe um ângulo:'))

print('O ângulo informado foi:  {} \n' \
'O valor do cosseno é igual a:  {} \n' \
'O valor do seno é igual a:     {} \n' \
'O valor da tangente é igual a: {} \n' \
'O valor da tangente é igual a: {}'.format(angulo,cos(angulo),sin(angulo), tan(angulo), (sin(angulo)/cos(angulo))))