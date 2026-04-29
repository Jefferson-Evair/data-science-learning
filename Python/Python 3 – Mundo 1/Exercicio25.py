#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome. 

nome = str(input('Por favor, informe seu nome completo:')).strip()
print('Seu nome contem Silva? {}'.format('SILVA' in nome.upper()))