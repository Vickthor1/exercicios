'''O professor Bill Gates está com problemas na gestão de suas classes, e ele não consegue
corrigir e entregar as notas de seus alunos a tempo. Elon Musk, um de seus alunos decidiu
ajudá-lo criando um programa para resolver esse problema, porém ele não sabe
programar, assim pediu sua ajuda para essa tarefa! Crie uma função que recebe um vetor
de respostas do aluno e um gabarito(questões de múltipla escolha de A até E), que
retorne a nota do aluno de 0 a 10.'''

'''Usando a função do item anterior, elabore um programa que é inserido as
respostas das provas de 3 alunos, onde o gabarito da prova é “A-A-B-D-E-A-C-C-A-D”,
logo após é mostrado as notas que esses alunos obtiveram.'''
def calcular_notas(respostas):
    gabarito = ['A','A','B','D','E','A','C',"C","A","D"]
    questao = len(gabarito)
    nota_total=10
    nota=0
    for i in range(questao):
        if respostas[i] == gabarito[i]:
            nota += nota_total/questao
    return nota
n = 3
questao = 10
alunos = []
notas = []

for i in range(3):
    aluno = f'ALUNO {i+1}'
    alunos.append(aluno)

    respostas = []

    print(f'\n{aluno}:\n')
    for i in range(questao):
        resposta = input(f'Digite a resposta {i+1}: ')
        respostas.append(resposta)

    nota = calcular_notas(respostas)
    notas.append(nota)

print('\nNOTAS:')
for i in range(n):
    print(f'{alunos[i]} - {notas[i]:.1f}')
print('\n')
