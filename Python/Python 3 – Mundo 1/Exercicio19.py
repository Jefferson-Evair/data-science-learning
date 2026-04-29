# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 

from random import randint

print('O aluno sorteado foi: {}'.format(randint(1,4)))