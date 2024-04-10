def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)

a = int(input("coloque aqui o número: "))
resposta = fat(a)

print(resposta)