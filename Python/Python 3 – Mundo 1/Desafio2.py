# Desafio 2 Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = int(input('Informe o dia do seu nascimento:'))
mes = int(input('Infome o mês do seu nascimento:'))
ano = int(input('Informe o ano do seu nascimento:'))

print('A data formatada do seu nascimento é igual a : {}/{}/{}'.format(dia,mes,ano))