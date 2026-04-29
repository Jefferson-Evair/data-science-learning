"""Crie um programa que leia o nome completo de uma pessoa e mostre:
    1. O nome com todas as letras maiúsculas;
    2. O nome com todas minúsculas;
    3. Quantas letras ao todo (sem condiderar espaços);
    4. Quantas letras tem o primeiro nome. 
"""

nome = input(str('Por favor, informe o seu nome completo:'))
divisao = nome.split()
print('O seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Ao todo, seu nome possui: {} letras.'.format(len(nome.strip()) - nome.count(' ')))
print('Seu primeiro nome possui: {} letras.'.format(len(divisao[0])))
print('Seu primeiro nome possui: {} letras.'.format(nome.find(' ')))
print('Seu primeiro nome possui: {} letras.'.format(len(divisao[0])))