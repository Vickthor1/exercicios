calculadora = True
while calculadora:
    print("Bem-vinda a calculadora braba")
    print("")
    print("qual tipo de operação você deseja?")
    print("1-somar")
    print("2-subtrair")
    print("3-multiplicar") 
    print("0-sair")
    escolha = input("insira aqui:")
    if escolha =="1":
        val1 = int(input("insira o primeiro valor:"))
        val2 = int(input("insira o segundo valor:"))
        print(val1 + val2)
        pass
    elif escolha =="2":
        val1 = int(input("insira o primeiro valor:"))
        val2 = int(input("insira o segundo valor:"))
        print(val1 - val2)
        pass
    if escolha =="3":
        val1 = int(input("insira o primeiro valor:"))
        val2 = int(input("insira o segundo valor:"))
        print(val1 * val2)
        pass
    if escolha =="0":
        print("Obrigado pelo uso")
        break