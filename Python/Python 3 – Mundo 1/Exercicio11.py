# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m²

altura = float(input('Informe a altura da parede:'))
largura = float(input('Informe a largura da parede:'))

print('A área da sua parede é de {} m²'.format(altura * largura))
print('A quantidade de tinta necessária para pintar a parede é {} litros'.format((altura * largura) / 2 ))