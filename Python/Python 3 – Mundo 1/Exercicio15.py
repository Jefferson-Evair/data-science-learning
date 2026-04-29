# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado. 

km = float(input('Por favor informe a quilometragem percorrida:'))
dias = int(input('Por favor informe por quantos dias o carro foi alugado:'))

print('O valor total a pagar é de R$ {}.'.format((km * 0.15 ) + (dias * 60)))