#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 

num = int(input('Informe um número inteiro: '))
u =  num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade do número informado é: {}'.format(u))
print('A dezena do número informado é: {}'.format(d))
print('A centena do número informado é: {}'.format(c))
print('A milhar do número informado é: {}'.format(m))