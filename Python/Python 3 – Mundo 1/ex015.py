'''Escreva um progrma que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''

kmPercorrido = float(input('Informe quantos quilometros foram percorridos: '))
DiasAluguel = int(input('Informe por quantos dias o carro foi alugado: '))

print('O valor total a pagar é igual a {}'.format((DiasAluguel * 60) + (kmPercorrido * 0.15)))