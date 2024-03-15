#10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de
#20 elementos, cujos valores deverão ser compostos pelos elementosintercalados dos dois
#outros vetores.
lista1=[]

lista2=[]

num1=int(input('insira o numero aqui: '))
lista1.append(num1)
print('')

num2=int(input('insira o numero aqui: '))
lista1.append(num2)
print('')

num3=int(input('insira o numero aqui: '))
lista1.append(num3)
print('')

num4=int(input('insira o numero aqui: '))
lista1.append(num4)
print('')

num5=int(input('insira o numero aqui: '))
lista1.append(num5)
print('')

num6=int(input('insira o numero aqui: '))
lista1.append(num6)
print('')

num7=int(input('insira o numero aqui: '))
lista1.append(num7)
print('')

num8=int(input('insira o numero aqui: '))
lista1.append(num8)
print('')

num9=int(input('insira o numero aqui: '))
lista1.append(num9)
print('')

num10=int(input('insira o numero aqui: '))
lista1.append(num10)
print('')

lista1.sort()
val1 = print('Primeira coluna de valores: ',lista1)

print('')

Anum1=int(input('insira o numero aqui: '))
lista2.append(Anum1)
print('')

Anum2=int(input('insira o numero aqui: '))
lista2.append(Anum2)
print('')

Anum3=int(input('insira o numero aqui: '))
lista2.append(Anum3)
print('')

Anum4=int(input('insira o numero aqui: '))
lista2.append(Anum4)
print('')

Anum5=int(input('insira o numero aqui: '))
lista2.append(Anum5)
print('')

Anum6=int(input('insira o numero aqui: '))
lista2.append(Anum6)
print('')

Anum7=int(input('insira o numero aqui: '))
lista2.append(Anum7)
print('')

Anum8=int(input('insira o numero aqui: '))
lista2.append(Anum8)
print('')

Anum9=int(input('insira o numero aqui: '))
lista2.append(Anum9)
print('')

Anum10=int(input('insira o numero aqui: '))
lista2.append(Anum10)
print('')

lista3= lista1+lista2

lista2.sort()
lista3.sort()

val2 = print('Segunbda coluna de valores: ',Anum1,Anum2,Anum3,Anum4,Anum5,Anum6,Anum7,Anum8,Anum9,Anum10)

print('')

val3 = print('Junção das duas colunas: ',lista3)