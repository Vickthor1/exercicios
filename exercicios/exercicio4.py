#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram
#lidas. Imprima as consoantes.

texto = str(input('Digite o texto aqui '))

#isso formata o texto pra minusculo
texto.lower()

#remove espaços linhas e simbolos
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")

#remove os acentos e cedilhas do texto
texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")
texto = texto.replace("ç","c")

vogais = 0

consoantes = 0

#retira as vogais das consoantes
consoante = texto

consoante = consoante.replace("a"," ")
consoante = consoante.replace("e"," ")
consoante = consoante.replace("i"," ")
consoante = consoante.replace("o"," ")
consoante = consoante.replace("u"," ")

#retira ac consoantes das vogais
vogaiss = texto

vogaiss = vogaiss.replace("b"," ")
vogaiss = vogaiss.replace("c"," ")
vogaiss = vogaiss.replace("d"," ")
vogaiss = vogaiss.replace("f"," ")
vogaiss = vogaiss.replace("g"," ")
vogaiss = vogaiss.replace("h"," ")
vogaiss = vogaiss.replace("j"," ")
vogaiss = vogaiss.replace("k"," ")
vogaiss = vogaiss.replace("l"," ")
vogaiss = vogaiss.replace("m"," ")
vogaiss = vogaiss.replace("n"," ")
vogaiss = vogaiss.replace("p"," ")
vogaiss = vogaiss.replace("q"," ")
vogaiss = vogaiss.replace("r"," ")
vogaiss = vogaiss.replace("s"," ")
vogaiss = vogaiss.replace("t"," ")
vogaiss = vogaiss.replace("v"," ")
vogaiss = vogaiss.replace("w"," ")
vogaiss = vogaiss.replace("x"," ")
vogaiss = vogaiss.replace("y"," ")
vogaiss = vogaiss.replace("z"," ")

#aqui que a conta acontece
for caracter in texto:
    if caracter in 'aeiou':
        vogais = vogais + 1
    
    else:
        consoantes = consoantes + 1
        
print('Vogais usadas: ',vogaiss)        
print('Consoantes usadas: ',consoante)
print('Vogais: ',vogais) 
print('Consoantes: ', consoantes)
print('Total de letras: ', (vogais+consoantes))