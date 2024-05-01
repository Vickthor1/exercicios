'''5. Crie uma função recursiva que receba um número inteiro positivo N e 
calcule o somatório dos números de 1 a N.
Curso de Graduação em Engenharia de Software
Algoritmos'''

def projectx (N):
    for x in range(1,N):
        print(x + 1)
x = 0
N = int(input("Insira até aonde vai a conta "))

z = projectx(N)