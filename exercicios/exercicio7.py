#7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação
#e os números.
import random
num1 = int(random.randrange(1,10))
num2 = int(random.randrange(1,10))
num3 = int(random.randrange(1,10))
num4 = int(random.randrange(1,10))
num5 = int(random.randrange(1,10))

print('O primeiro numero é: ',num1,'Soma',num1 + num1,num1 + num2,num1 + num3,num1 + num4,num1 + num5)
print('Multiplicação',num1 ** num1,num1 ** num2,num1 ** num3,num1 ** num4,num1 ** num5)
print('')
print('O segundo numero é: ',num2,'Soma', num2 + num1,num2 + num2,num2 + num3,num2 + num4,num2 + num5)
print('Multiplicação', num2 ** num1,num2 ** num2,num2 ** num3,num2 ** num4,num2 ** num5)
print('')
print('O terceiro numero é: ',num3,'Soma', num3 + num1,num3 + num2,num3 + num3,num3 + num4,num3 + num5)
print('Multiplicação', num3 ** num1,num3 ** num2,num3 ** num3,num3 ** num4,num3 ** num5)
print('')
print('O quarto numero é: ',num4,'Soma', num4 + num1,num4 + num2,num4 + num3,num4 + num4,num4 + num5)
print('Multiplicação', num4 ** num1,num4 ** num2,num4 ** num3,num4 ** num4,num4 ** num5)
print('')
print('O quinto numero é: ',num5,'Soma', num5 + num1,num5 + num2,num5 + num3,num5 + num4,num5 + num5)
print('Multiplicação', num5 ** num1,num5 ** num2,num5 ** num3,num5 ** num4,num5 ** num5)