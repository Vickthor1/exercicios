#6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
#média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
import random
media = 7


juliana = random.randrange(1,10)
Pedro = random.randrange(1,10)
Victor = 10
Elias = random.randrange(1,10)


print('a média é',media,'e as notas foram: ')

if juliana>=7:
 print(juliana,' está acima da média')
else:
    print(juliana,'Você está abaixo da média')
if Pedro >=7:
 print(Pedro ,' está acima da média')
else:
    print(Pedro,'Você está abaixo da média')
if Victor >=7:
 print(Victor,' está acima da média')
else:
    print(Victor,'Você está abaixo da média')
if Elias >=7:
 print(Elias,' está acima da média')
else:
    print(Elias,'Você está abaixo da média')