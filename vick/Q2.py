'''2. Escreva uma função que receba uma lista ordenada como parâmetro e 
retorne uma nova lista contendo apenas os números ímpares, e outra lista 
com os números pares da lista original. 
Considere: Lista [1,2,3, ... , 10000]'''
Lista = []
Impar=[]
Par=[]
def infinito(x,Lista): 
    for x in range(1,1000):
        x = (x)
        Lista.append(x)
    return Lista
x = 0
a = infinito(x,Lista)
for c in Lista:
  if c % 2 == 0:
    Impar.append(c)
  else:
    Par.append(c)

print(a)
print(Impar)
print(Par)
