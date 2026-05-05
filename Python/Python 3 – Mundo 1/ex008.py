#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

ValorMetros = float(input('Informe um valor em metros: '))
ValorCentrimetros = ValorMetros * 100
ValorMilimetros = ValorMetros * 1000

print(f'O valor informado foi {ValorMetros}, o valor correspondente em centímetros é igual a {ValorCentrimetros} e em milimetros é igual a {ValorMilimetros}')