# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ 1,0 = R$ 3,27. 

real = float(input('Informe quantos reais possui na carteira:'))
print('Você pode comprar até US$ {} '.format(real / 3.27))