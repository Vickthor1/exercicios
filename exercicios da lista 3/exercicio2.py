'''Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for correta 
e false caso o contrário. Logo após elabore um “mini-sistema” de checar a senha inserida, 
onde o usuário tem 3 tentativas de senha e caso esse número seja ultrapassado o 
programa é encerrado.''' 

def verificar_senha(senha_certa,tentativa):
    if senha_certa == tentativa:
        return True
    else:
        return False

senha_certa =123

for i in range(3):
    tentativa = int(input("digite sua senha"))
    verificacao = verificar_senha(senha_certa,tentativa)
    if verificacao:
        print("Você fez teu Login com sucesso!")
        break