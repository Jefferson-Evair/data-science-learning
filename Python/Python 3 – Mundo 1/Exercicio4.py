# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Informe algo pelo teclado:')

print('O tipo primitivo é: ', type(a))
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('É numérico?', a.isnumeric())
print('É maísculo?', a.isupper())
print('É minúsuculo?', a.islower())
print('Está capitalzada?', a.istitle())
print('É um espaço?', a.isspace())