'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras  maiúsculas e minúsculas
- Quantas letras ao todos(sem considerar espaços)
- Quantas letras tem o primeiro nome'''

nomecompleto = str(input('Informe o nome completo de uma pessoa:'))
nomefatiado = nomecompleto.split()

print(f'O nome completo informado foi: {nomecompleto}')
print('O nome completo informado foi: {}'.format(nomecompleto))
print('O nome completo informado foi:',nomecompleto)

#O nome com todas as letras maiúsculas e minúsculas
print(f'{nomecompleto.upper()}')
print(f'{nomecompleto.lower()}')

#Quantas letras ao todos(sem considerar espaços)?
print(f'Ao todo, seu nome possui {len(nomecompleto) - nomecompleto.count(' ')} letras')

#Quantas letras tem o primeiro nome?
print('Seu primeiro nome é {} e possui {} letras'.format(nomefatiado[0], len(nomefatiado[0])))