def fatInterativo(n):
    resultado = 1
    for i in range(1,n+1):
        resultado *= i
    return resultado
a = int(input("Coloque aqui o fatorial: "))
resposta = fatInterativo(a)
print(resposta)