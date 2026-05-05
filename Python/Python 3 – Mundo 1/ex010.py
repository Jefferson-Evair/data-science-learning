''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
    Assumi a cotação de R$ 4,99 no dia 01/05/2026 '''

carteira = float(input('Inrforme quantos reais possui na carteira:'))

print('Pela cotação atual, você pode comprar {}'.format(carteira / 4.99))
