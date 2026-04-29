frase = str(input('Informe uma frase qualquer: ')).strip()
print('Quantas vezes aparece a letra "A"? Resposta: {}'.format(frase.upper().count('A')))
print('Em que posição ela aparece a primeira vez? Resposta: {}'.format(frase.upper().find('A')))
print('Em que posição ela aparece a última vez? Resposta: {}'.format(frase.upper().rfind('A')))