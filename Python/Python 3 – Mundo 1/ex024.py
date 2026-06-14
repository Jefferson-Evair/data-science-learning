'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo" '''

nome_cidade = str(input('Informe o nome de uma cidade: '))
fatia_nome_cidade = nome_cidade.split()

print('O nome da cidade começa com Santo?: {}'.format('Santo' in fatia_nome_cidade[0]))