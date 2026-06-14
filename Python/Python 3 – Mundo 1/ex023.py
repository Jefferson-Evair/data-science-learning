''' Faça um progrma que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo: 1834
Unidade: 4 Dezena: 3 Centena:8 Milhar:1
'''

num = int(input('Informe um número inteiro entre 0 e 9999:'))
num_text = str(num)

#Fatiando a String
print('unidade = {}'.format(num_text[3]))
print('dezena  = {}'.format(num_text[2]))
print('centena = {}'.format(num_text[1]))
print('milhar  = {}'.format(num_text[0]))

#Usando matemágica
print(f'unidade = {num // 1    % 10}')
print(f'dezena  = {num // 10   % 10}')
print(f'centena = {num // 100  % 10}')
print(f'milhar  = {num // 1000 % 10}')