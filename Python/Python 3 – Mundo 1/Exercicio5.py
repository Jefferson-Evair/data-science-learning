# Faça um programa que leia um número inteiro e mostre na tela o seu sucesso e se antecessor. 

num = int(input('Informe um número inteiro:'))
ant = num -1
suc = num +1
print('O número informado foi {}, e o seu antecessor é {} e o seu sucessor é {}'.format(num, ant, suc))