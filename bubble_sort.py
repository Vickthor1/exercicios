#O bubblesort, ele vai trocando o lugar do elemento, pegando o maior número e jogando ele para direita, até seu devido lugar...
def Bubble_Sort(lista):
    for troca in range(len(lista)-1,0,-1):
        #repete a troca até finalizar a função dela
        for i in range(troca):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
            #print foi usado para demonstrar o bubble sendo usado
            print()
            print(lista)

lista = [54,26,93,17,77,31,44,55,20]
Bubble_Sort(lista)
print()
print("Finalizada:",lista)
