#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo". 

nome = str(input('Em qual cidade você nasceu?'))
print('O nome informado foi {}. Ele começa com Santo? {}'.format(nome, 'SANTO' in nome.upper()))

#Podemos melhorar: 

cidade = str(input('Informe em qual cidade você nasceu:')).strip()
print('A cidade começa com Santo? {}'.format('SANTO' in cidade[:5].upper()))

#Ainda pode ser mais simples e funcional

cidade = str(input('Informe o nome de uma cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')