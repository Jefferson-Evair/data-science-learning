# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 

num = float(input('Informe um medida em metros:'))

print('A medida informada em metros foi {} '.format(num))
print('Centímetros: {}'.format(num * 100))
print('Milímetros: {}'.format(num * 1000))