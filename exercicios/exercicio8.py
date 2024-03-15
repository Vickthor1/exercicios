#8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
#seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

dicionario={
    
}

idade1= str(input('Qual a idade da Ana? '))

print('')

altura1 = str(input('Qual a altura dela? '))

print('')

idade2= str(input('Qual a idade do Pedro? '))

print('')

altura2= str(input('Qual a altura dele? '))

print('')

idade3= str(input('Qual a idade Enzo? '))

print('')

altura3= str(input('Qual a altura dele? '))

print('')

idade4= str(input('Qual a idade Julia? '))

print('')

altura4= str(input('Qual a altura dela? '))

print('')

idade5= str(input('Qual a idade da Gabriela? '))

print('')

altura5= str(input('Qual a altura dela? '))
print('')

#parte que os dados são adicionados ao dicionario

dicionario ['Gabriela idade: '+idade5+','] = 'altura: '+altura5

dicionario ['Julia idade: '+idade4+','] = 'altura: '+altura4

dicionario ['Enzo idade: '+idade3+','] = 'altura: '+altura3

dicionario ['Pedro idade: '+idade2+','] = 'altura: '+altura2

dicionario ['Ana idade: '+idade1+','] = 'altura: '+altura1

for x,y in dicionario.items():
    print(x, y)