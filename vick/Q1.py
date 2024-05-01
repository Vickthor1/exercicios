'''1. Crie uma função chamada comprimentoMenor que recebe duas strings 
como parâmetros e retorna True se o comprimento da primeira string for 
menor do que o da segunda string, e False caso contrário.'''

def comprimentoMenor(a,b):
    if a> b:
        return False
    else:
        return True

a = str(input(" "))
b = str(input(" "))
x =comprimentoMenor(a,b)

print(x)