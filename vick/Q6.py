'''6. Crie uma função que lê o ano de nascimento de uma pessoa e o ano atual. 
Calcule e mostre qual é: a idade da pessoa em anos, a idade da pessoa 
em meses, a idade da pessoa em dias e a idade da pessoa em semanas
Atividades Obrigatórias
Entregar os arquivos compactados em um único arquivo pelo AVA.
ATENÇÃO: utilizar compactadores open source'''

def calcular_idade_ano(ano_nascimento,ano_atual):
    x = ano_atual - ano_nascimento
    return x
def calcular_idade_mes(mes_nascimento,mes_atual):
    x = mes_atual - mes_nascimento
    return x
def calcular_idade_dia(dia_nascimento,dia_atual):
    x = dia_atual - dia_nascimento
    return x
ano_nascimento = int(input("Que ano você nasceu? "))
ano_atual = int(input("Que ano você esta? "))
mes_nascimento = int(input("Que mes você nasceu? "))
mes_atual = int(input("Que mes você esta? "))
dia_nascimento = int(input("Que dia você nasceu? "))
dia_atual = int(input("Que dia você esta? "))
a = calcular_idade_ano(ano_nascimento,ano_atual)
c = calcular_idade_mes(mes_nascimento,mes_atual)
d = calcular_idade_dia(dia_nascimento,dia_atual)

print("você está com ",a," anos!","fazem ",a," anos,",c," mesês,",d," dias, que você nasceu!")