''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. '''

PrecoAtual = float(input('Informe o valor atual do produto: '))
PrecoDesconto = PrecoAtual * 0.95

print('O valor do produto com desconto de 5% é igual a R$ {}'.format(PrecoDesconto))