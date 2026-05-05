''' Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta aproximadamente uma área de 2m². '''

largura = float(input('Informe a largura da parede:'))
altura = float(input('Informe a altura da parede:'))

print(f'A parede possui {largura * altura} m²')
print(f'Você precisará de {(largura * altura) / 2} litros de tinta.')