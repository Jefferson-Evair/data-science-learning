# Python Python 3 – Mundo 1 [40 Horas] 

## Introdução ao Mundo da Programação
### Aula 1- Seja um programador
- Visão geral do que é ser um programador

## Primeiros passos com o Python
### Aula 2 – Para que serve o Python?
### Aula 3 – Instalando o Python3 e o IDLE
### Aula 4 – Primeiros comandos em Python3
- Desafio 01 - Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acodordo com o valor digitado.
- Solução:
``` 
nome = input('Informe seu nome: ')
print('Seja bem-vindo',nome)

nome = input('Informe seu nome: ')
print('Seja bem-vindo {}'.format(nome))

nome = input('Informe seu nome: ')
print(f'Seja bem-vindo {nome}')
``` 
- Desafio 02 - Crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada. 
- Solução:
```
DiaNascimento = int(input('Informe o dia do seu nascimento:'))
MesNascimento = int(input('Informe o mês do seu nascimento:'))
AnoNascimento = int(input('Informe o ano do seu nascimento:'))

print(f'A data formatada do seu nascimento é igual a: {DiaNascimento}/{MesNascimento}/{AnoNascimento}')
print('A data formatada do seu nascimento é igual a: {}/{}/{}'.format(DiaNascimento, MesNascimento,AnoNascimento))
print('A data formatada do seu nascimento é igual a:',DiaNascimento,'/',MesNascimento,'/',AnoNascimento)

```
- Desafio 03 - Crie um script python que leia dois números e tente mostrar a soma entre eles. 
- Solução:
```
numero1 = int(input('Informe o primeiro número inteiro:'))
numero2 = int(input('Informe o segundo número inteiro:'))
soma = numero1 + numero2

print(f'O resultado da soma é {soma}')
print('O resultado da soma é {}'.format(soma))
print('O resultado da soma é', soma)
```
### Aula 5 – Instalando o PyCharm e o QPython3
> Achei melhor seguir com o VsCode, pois uso bastante no trabalho. Mas o PyCharm me causou uma boa impressão. 
- Exercício 001 - Crie um programa que escreva "Olá, Mundo!" na tela. 
- Solução: 
```
print(f'Olá, mundo!')
print('Olá Mundo!')
```
- Exercício 002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
- Solução:
```
nome = input('Informe o seu nome: ')
print(f'Olá, {nome}. Seja bem vindo(a)')
print('Olá, {}. Seja bem vindo(a)'.format(nome))
print('Olá,',nome,'. Seja bem vindo(a)')
```
## Tratando dados e fazendo contas
### Aula 6 – Tipos Primitivos e Saída de Dados
Nessa aula, vimos como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). Além disso, vimos como fazer as primeiras operações com a função ```print()``` do Python.
- Desafio 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sonbre ele. 
- Solução: 
```
InfoTeclado = input('Digite algo para saber o seu tipo primitivo:')

print(f'O tipo primitivo do valor informado é:{type(InfoTeclado)}')

print(f'É número? {InfoTeclado.isnumeric()}')
print(f'É alfanumérico? {InfoTeclado.isalnum()}')
print('É letra? {}'.format(InfoTeclado.isalpha()) )
```
- Exercício 003 - Crie um programa que leia dois números e mostre a soma entre eles. 
- Solução:
```
num1 = int(input('Informe o primeiro número inteiro: '))
num2 = int(input('Informe o segundo número inteiro:  '))
soma = num1 + num2

print(f'O resultado da soma é igual a {soma}')
print('O resultado da soma é igual a {}'.format(soma))
```
- Exercício 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
- Solução:
```
InfoTeclado = input('Digite algo para descobrir o tipo primitivo:')

print(f'O tipo primitivo é: {type(InfoTeclado)}')
print(f'Tem apenas espaços? {InfoTeclado.isspace()}')

print('É número? {}'.format(InfoTeclado.isnumeric()))
print('É alfanumérico? {}'.format(InfoTeclado.isalnum()))
```
### Aula 7 – Operadores Aritméticos
```
+  Adição
-  Subtração
*  Multiplicação
** Potênciação
/  Divisão
// Divisão inteira
%  Resto de uma Divisão ou Móduço
=  Igual a atribuição
== Igualdade (Operador relacional de igualdade)

Ordem de precedência dos operadores em uma expreção:

() 
**
* ou / ou // ou %
+ ou Subtração
```
- Exercício 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessos e e seu antecessor. 
- Solução:
```
numero = int(input('Informe um número inteiro:'))
sucessor = numero + 1
antecessor = numero - 1

print(f'O número informado foi {numero} e o seu sucessor é {sucessor} e o antecessor é {antecessor}')
```
- Exercício 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. 
- Solução:
```
numero = int(input('Informe um número:'))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)

print(f'{raiz}')
```
- Exercício 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. 
- Solução:
```
numero = int(input('Informe um número:'))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)

print(f'{raiz}') 
```
- Exercício 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média. 
- Solução:
```
PrimeiraNota= float(input('Informe a primeira nota:'))
SegundaNota = float(input('Informe a segunda nota:'))
Media = (PrimeiraNota + SegundaNota) / 2

print(f'A média entre as duas notas é igual a {Media}')
print('A média entre as duas notas é igual a {}'.format((PrimeiraNota + SegundaNota) / 2))
```
- Exercício 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
- Solução:
```
ValorMetros = float(input('Informe um valor em metros: '))
ValorCentrimetros = ValorMetros * 100
ValorMilimetros = ValorMetros * 1000

print(f'O valor informado foi {ValorMetros}, o valor correspondente em centímetros é igual a {ValorCentrimetros} e em milimetros é igual a {ValorMilimetros}')
```

- Exercício 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 
- Solução:
```
Numero = int(input('Informe um número inteiro:'))

print(f'{Numero} x  1 = {Numero * 1 }')
print(f'{Numero} x  2 = {Numero * 2 }')
print(f'{Numero} x  3 = {Numero * 3 }')
print(f'{Numero} x  4 = {Numero * 4 }')
print(f'{Numero} x  5 = {Numero * 5 }')
print(f'{Numero} x  6 = {Numero * 6 }')
print(f'{Numero} x  7 = {Numero * 7 }')
print(f'{Numero} x  8 = {Numero * 8 }')
print(f'{Numero} x  9 = {Numero * 9 }')
print(f'{Numero} x 10 = {Numero * 10}')
``` 
- Exercício 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Assumi a cotação de R$ 4,99 no dia 01/05/2026. 
- Solução:
```
carteira = float(input('Inrforme quantos reais possui na carteira:'))

print('Pela cotação atual, você pode comprar {}'.format(carteira / 4.99))
```
- Exercício 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,sabendo que cada litro de tinta, pinta aproximadamente uma área de 2m².
- Solução:
```
largura = float(input('Informe a largura da parede:'))
altura = float(input('Informe a altura da parede:'))

print(f'A parede possui {largura * altura} m²')
print(f'Você precisará de {(largura * altura) / 2} litros de tinta.')
```
- Exercício 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
- Solução:
```
PrecoAtual = float(input('Informe o valor atual do produto: '))
PrecoDesconto = PrecoAtual * 0.95

print('O valor do produto com desconto de 5% é igual a R$ {}'.format(PrecoDesconto))
```
- Exercício 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
- Solução:
```
SalarioAtual = float(input('Informe o salário atual:'))

print(f'O novo salário com 15% de aumento é R$ {SalarioAtual + (SalarioAtual * 0.15)}')
```
- Exercício 014 - Escreva um programa que leia converta uma temperatura digitada em graus Celsius e converta em Grau Fahrenheit.
- Solução:
```
GrausCelsius = float(input('Informe uma temperatura em Graus Celsius °C:'))
Fahrenheit = (GrausCelsius * 1.8) + 32

print(f'A temperatura correspondente na escala Fahrenheit é igual a: {Fahrenheit}')
```
- Exercício 015 - Escreva um progrma que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
- Solução:
```
kmPercorrido = float(input('Informe quantos quilometros foram percorridos: '))
DiasAluguel = int(input('Informe por quantos dias o carro foi alugado: '))

print('O valor total a pagar é igual a {}'.format((DiasAluguel * 60) + (kmPercorrido * 0.15)))
```
## Usando módulos do Python
### Aula 8 - Utilizando Módulos
- Sintáxe para importar um módulo completo: import bebida
- Sintáxe para importar funcionalidades específicas: from doce import pudim

```Exemplo: O módulo math , que é um módulo bem comum, temos as seguintes funções(dentre as muitas funções existentes nesse módulo):

ceil        - Arredondamento para cima
flor        - Arredondamento para baixo
trunc       - Truncar 
pow         - potencia
sqrt        - Raíz quadrada
factorial   - factorial de um número
```
- Se por acaso, no iníco de um script seja utilizado o seguinte comando: 

``` import math

Isso signigica que estaremos importando também todas as funções existentes nesse módulo. Contudo, o ideal é que seja importado apenas as funções que de fato serão utilizadas.

Logo, o comando passaria a ter a seguinte sintáxe:

from math import ceil
```
- Exercício 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
- Solução:
```
from math import trunc 

num = float(input('Informe um número qualquer e descubra sua porção inteira: '))

print(f'A porção inteira do número {num} é igual a {trunc(num)}')
print('A porção inteira do número {} é igual a {}'.format(num, trunc(num)))
```
- Exercício 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
- Solução:
```
from math import hypot

CatetoOposto = int(input('Informe o valor do cateto oposto: '))
CatetoAdjacente = int(input('Informe o valor do cateto adjacente: '))

print(f'O valor da Hipotenusa é igual a: {hypot(CatetoOposto, CatetoAdjacente)}')
print('O valor da hipotenusa é igual a: {}'.format(hypot(CatetoOposto, CatetoAdjacente)))
```
- Exercício 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
- Solução:
```
from math import sin, cos, tan

angulo = float(input('Informe o valor de um ângulo qualquer: '))

print('O ângulo informado foi {} \n ' \
'O valor valor do seno é {} \n' \
'O valor do cosseno é {} \n' \
'O valor da tangente é {}'.format(angulo, sin(angulo), cos(angulo),tan(angulo)))
```
- Exercício 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
- Solução:
```
from random import choice

aluno1 =  input('Informe o nome do primeiro aluno: ')
aluno2 =  input('Informe o nome do segundo  aluno: ')
aluno3 =  input('Informe o nome do terceiro aluno: ')
aluno4 =  input('Informe o nome do quarto   aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido para apagar o quadro é: {}'.format(choice(lista)))
``` 
- Exercício 020 - O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
- Solução:
```
from random import shuffle, sample

aluno1 =  input('Informe o nome do primeiro aluno: ')
aluno2 =  input('Informe o nome do segundo  aluno: ')
aluno3 =  input('Informe o nome do terceiro aluno: ')
aluno4 =  input('Informe o nome do quarto   aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(f'A ordem das apresentações é a seguinte: {lista}')
print('A ordem das apresentações é a seguinte: {}'.format(sample(lista, k=4)))
```
- Exercício 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
- Solução: 
```
import pygame

# 1. Inicializar o Pygame
pygame.init()

# 2. Carregar o arquivo MP3
pygame.mixer.music.load('Sepultura - Roots Bloody Roots.mp3')

# 3. Reproduzir a música
pygame.mixer.music.play()

# Só funcionou depois que acrescentei input, deve ter mudado algo lógica da biblioteca. 
input()

pygame.event.wait()
```
### Aula 9 – Manipulando Texto
- O que é uma cadeia de Texto (cadeia de caracteres/string)? 
- Exemplo: 
```
'Curso em Vídeo Python' ou "Curso em Vídeo Python" ou '''Curso em Vídeo Python'''
```
- O que acontece na máquina? 
```
Se por acaso, atribuirmos a variável chamada `frase` uma cadeira de caracteres da seguinte forma: 

`frase` = 'Curso em Vídeo Python'

Como a máquina processa essa cadeia? 
Cada caractere recebe um índice, incluindo os espaços em brando. Ou seja, a cadeia 'Curso em Vídeo Python' possui 21 espaços alocados na memória da máquina.
```
#### Fatiamento: String `frase`

| C | u | r | s | o | _ | e | m | _ | V | í | d | e | o | _ | P | y | t | h | o | n |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| -21| -20| -19| -18| -17| -16| -15| -14| -13| -12| -11| -10| -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |


- É possível fatiar uma string utilizando o conceito de lista, que será abordado um pouco mais adiante. Por exemplo, como extrair apenas a palavra `Vídeo` da String `frase` ? 
- Solução:  
``` 
  frase[9:14] = 'Vídeo'
  
  Em Python, a regra de fatiamento [início:fim] funciona assim:

    O início é inclusivo: O caractere naquela posição entra na fatia.
    O fim é exclusivo: O Python para antes de chegar nesse índice.
  ```  
- Jeito Fácil de Pensar: 
```
  Uma dica prática para nunca mais errar o cálculo é subtrair os números: 14−9=5
    
    O resultado da subtração sempre indica quantos caracteres você terá na sua fatia. Como a palavra "Vídeo" tem 5 letras, você precisa de um intervalo que resulte em 5.

    [9:13] →13−9=4 letras (Errado)

    [9:14] →14−9=5 letras (Correto)
```
- **Outros tipos de fatiamentos:** 

1. Para fatiar uma string, saltando posições, basta acrescentarmos mais : (dois pontos) após o término. Exemplo: frase[9:21:2]
2. Quando omitimos o início, o fatiamento iniciará da posição 0 (zero). Exemplo: frase[:5]
3. Quando omitimos o término, o fatiamento acontecerá do incío até a última posição. Exemplo: frase[15:]
4. Também é possível omitir o final e ainda assim saltar posições. Exemplo: frase[9::3] 
#### Análise: String `frase`
- Talvez seja o que mais vou usar no futuro. A seguir estão alguns métodos que serão utilizados ao longo do curso:
```
 len(frase) - Comprimento de uma cadeia de caracteres; 
 frase.count('o') - Contagem de uma string;
 frase.count('o',0,13) - Contagem com fatiamento em uma string;
 frase.find('deo') - Mostra a posição dentro da cadeia de caracteres;
 'Curso' in frase - Nesse caso, retorna True 
 ``` 
> Mestre Guanabara pediu para guardar com carinho o método len( ). 

#### Transformação: String `frase`
- Mais alguns métodos que serão utilizados ao longo do curso para transformação de strings:
```
frase.replace('Python','Android') - Basicamente encontra 'Python' em 'frase' e subistitui por 'Android'. A quantidade de caracteres deve ser equivalente?
frase.upper() - Fica em caixa alta; 
frase.lower() - Fica em caixa minúsculo;
frase.capitalize() - Deixa apenas a primeira string em caixa alta, é muito confundido com `title()`.
frase.title() - Analisa quantas palavras existentes em uma cadeia, e deixa a primeira string de cada palavra em caixa alta; 
frase.strip() - Remove todos os espaços desnecessários no início e no fim de uma cadeia de caracteres;
frase.rstrip() - Remove os últimos espaços; 
frase.lstrip() - Remove os primeiros espaços;
```
> O mestre explicou que veremos mais adiante esse caso do método `replace()`, mas a princício, entendi que internamente o Python ajusta o comprimento da cadeia de caracteres. 
#### Divisão: String `frase`
- frase.split() - Por padrão, o split é realizado nos espaços, criando novas indexações nas Cadeias de caracteres; Exemplo prático:
- **Antes** de aplicar frase.split( )

| C | u | r | s | o | _ | e | m | _ | V | í | d | e | o | _ | P | y | t | h | o | n |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |

- **Depos** de aplicar frase.split( )

| C | u | r | s | o | _ | e | m | _ | V | í | d | e | o | _ | P | y | t | h | o | n |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | 3 | 4 |   | 0 | 1 |   | 0 | 1  | 2  | 3  | 4  |   | 0  | 1  | 2  | 3  | 4  | 5  |
#### Junção: String `frase`
```- '-'.join(frase) - Juntar strings ```

- Exercício 022 - Crie um programa que leia o nome completo de uma pessoa e mostre: 
- Solução:
```
O nome com todas as letras  maiúsculas e minúsculas:

nomecompleto = str(input('Informe o nome completo de uma pessoa:'))
nomefatiado = nomecompleto.split()

print(f'O nome completo informado foi: {nomecompleto}')
print('O nome completo informado foi: {}'.format(nomecompleto))
print('O nome completo informado foi:',nomecompleto)

#O nome com todas as letras maiúsculas e minúsculas
print(f'{nomecompleto.upper()}')
print(f'{nomecompleto.lower()}')

#Quantas letras ao todos(sem considerar espaços)?
print(f'Ao todo, seu nome possui {len(nomecompleto) - nomecompleto.count(' ')} letras')

#Quantas letras tem o primeiro nome?
print('Seu primeiro nome é {} e possui {} letras'.format(nomefatiado[0], len(nomefatiado[0])))
```