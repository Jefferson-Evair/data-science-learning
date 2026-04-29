"""Faça um programa que leia uma frase pelo teclado e mostre:
    
    > Quantas vezes aparece a letra "A";
    > Em que posição ela aparece a primeira vez;
    > Em que posição ela aparece a última vez. 

"""

frase = str(input('Informe uma frase qualquer: ')).strip()
print('Quantas vezes aparece a letra "A"? Resposta: {}'.format(frase.upper().count('A')))
print('Em que posição ela aparece a primeira vez? Resposta: {}'.format(frase.upper().find('A')+1))
print('Em que posição ela aparece a última vez? Resposta: {}'.format(frase.upper().rfind('A')+1))