print('escolha um produto da nossa loja')
produto = input('diga o produto que deseja: ')
preco = float(input('digite o preço do produto: '))
desconto = preco * 0.4
total = preco - desconto
print(f'o produto era R${preco} com o desconto de 40% o produto ficou por R${total}')