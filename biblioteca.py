import random
print('---Cadastro da Biblioteca---')
usuarios = ['adm']
senhas = ["12345"]

def mascarar_senha(senhas):
    return "*" * len(senhas)

def registro():
    while True:
        print("Se deseja adicionar um novo usuário digite 1")
        print("Se deseja fazer login 2")
        print("Se deseja acessar a lista de usuários 3")
        print("Se deseja sair digite 4")
        escolha = input("Digite sua escolha: ")
        print("")

        if escolha == "1":
            print('-Adicionar usuário-')
            nome = str(input('Nome do Usuário: '))
            print("")
            usuarios.append(nome)
            
            senha = str(input('Senha Usuário: '))
            print("")
            senhas.append(senha)
            print("Cadastro finalizado. Usuários cadastrados!")
            print("")
            x = int(input("Deseja sair? 1-Sim/2-Não "))
            if x == 1:
                break
            if x == 2:
                pass
        
        elif escolha == "2":
            nome = str(input("Digite o Nome do usuário: "))
            print("")
            if nome in usuarios:
                try:
                    senha = str(input("Digite a senha do usuário:"))
                    print("")
                    print("Deseja sair? 1-Sim/2-Não")
                    resp = int(input(" "))
                    if resp == 1:
                        break
                    if resp == 2:
                        pass
                except:
                    print("Senha de usuário incorreta")
                    print("")
                    continue
                
            else:
                print('Usuário não encontrado!')
            pass
        elif escolha == "3":
            print("Usuários:")
            for user in usuarios:
                print(user)
            
            print("")    
            print("Deseja sair? 1-Sim/2-Não")
            resp = int(input(" "))
            if resp == 1:
                break
            if resp == 2:
                pass
            
        if escolha == "4":
            print('Até brave!')
            break
        
        else:
            print("")
            print("Opção inválida. Tente novamente.")
            pass
        

registro()

for i in range(len(usuarios)):
    print("usuário: ",usuarios[i]," / Senha: ",mascarar_senha(str(senhas[i])))
