# Escreva um programa que converta uma temperatura digitada em °C para F. 

temperatura = float(input('Informe uma temperatura em graus Célcius:'))

print('A temperatura informada em graus Célcius foi {:.0f} e equivale a {:.0f} °F'.format(temperatura, ((9 * temperatura) / 5 ) + 32))