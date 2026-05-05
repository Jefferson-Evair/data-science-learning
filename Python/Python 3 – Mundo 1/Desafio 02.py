#Desafio 02 - Crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

DiaNascimento = int(input('Informe o dia do seu nascimento:'))
MesNascimento = int(input('Informe o mês do seu nascimento:'))
AnoNascimento = int(input('Informe o ano do seu nascimento:'))

print(f'A data formatada do seu nascimento é igual a: {DiaNascimento}/{MesNascimento}/{AnoNascimento}')
print('A data formatada do seu nascimento é igual a: {}/{}/{}'.format(DiaNascimento, MesNascimento,AnoNascimento))
print('A data formatada do seu nascimento é igual a:',DiaNascimento,'/',MesNascimento,'/',AnoNascimento)