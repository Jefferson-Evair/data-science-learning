'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Informe uma frase qualquer:')).upper()

print('A frase informada foi: {}'.format(frase))
print('A letra "A" aparece {} vez(es)'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))

#Sem rfind('A')
primeiroA = frase.find('A') + 1
ultimoA = len(frase) - frase[::-1].find('A')

print(f'{primeiroA}')
print(f'{ultimoA}')