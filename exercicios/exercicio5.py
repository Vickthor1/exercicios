#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
#números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três
#vetores.

listaimpar = []

listapar = []

numeros = range(1,20)

for x in numeros:
    if (numeros%2) == 0:
        print("Par")
        listaimpar.append(numeros)

    else:
        print("Ímpar")
        listapar.append(num)

print('impar: ',listaimpar)
print('par: ',listapar)