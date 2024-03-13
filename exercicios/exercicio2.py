#2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
import random
lista = []
numero1 = random.randrange(1, 9)
numero2 = random.randrange(1, 9)
numero3 = random.randrange(1, 9)
numero4 = random.randrange(1, 9)
numero5 = random.randrange(1, 9)
numero6 = random.randrange(1, 9)
numero7 = random.randrange(1, 9)
numero8 = random.randrange(1, 9)
numero9 = random.randrange(1, 9)
numero10 = random.randrange(1, 9)

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.append(numero4)
lista.append(numero5)
lista.append(numero6)
lista.append(numero7)
lista.append(numero8)
lista.append(numero9)
lista.append(numero10)

lista.sort(reverse=True)

print(lista)