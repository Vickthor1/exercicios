picanha = 15 
tradicional = 10
artesanal = 20
pão_de_gergelim = 15
queijo = 2
bacon = 3
ovo = 1
molho_especial = 5
lentilha = 15
cebola_com_batata = 15
lanche = 0
while True:
 genero = input('qual o seu genero? ')
 if genero == 'masculino':
  pronome = 'senhor'
  print('informação guardada')
  break 
 if genero == 'feminino':
  pronome = 'senhora'
  print('informação guardada!')
  break 
 if genero == 'não binario':
  pronome = 'elx'
  break
 else:
  print('não entendi')
  pass
while True:
 hamburguer = input('bem vindo ao mundo burguer,gostaria do cardapio? ')
 if hamburguer == 'sim':
  print(f'ok {pronome} , vamos providenciar...')
  break
 elif hamburguer == 'não':
  print(f'ok {pronome}, próximo!')
  exit
 elif print(f'não entendi {pronome} poderia repitir?'):
  pass

print('cardapio mundo burguer:')
print('----tipos de pão-----')
print(' tradicional = R$10')
print('  artesanal = R$20')
print('   pão de gergelim = R$15')
print('----adicionais----')
print('  picanha = R$15')
print('   queijo = R$2')
print('    bacon = R$3')
print('     ovo = R$1')
print('  molho especial = R$5')
print('----opção vegana----')
print('   lentilha = R$15')
print('    cebola com batata = R$15')

while True:
 pão = input(' escolha o tipo de pão: ')
 if pão == 'tradicional':
  lanche = lanche + tradicional
  break
 if pão == 'artesanal':
  lanche = lanche + artesanal
  break
 if pão == 'pão de gergelim':
  lanche = lanche + pão_de_gergelim
  break
 if pão == 'não':
  break
 else:
  print('poderia repetir, não entendi')
  pass

while True:
 adicional = input('gostaria de adicionar algo? ')
 if adicional == 'picanha':
  lanche =lanche + picanha
  break
 if adicional == 'queijo':
  lanche = lanche + queijo
  break
 if adicional == 'bacon':
  lanche = lanche + bacon
  break
 if adicional == 'ovo':
  lanche = lanche + ovo
  break
 if adicional == 'molho especial':
  lanche = lanche + molho_especial
  break
 if adicional == 'não':
  break
 else:
  print('Não entendi mesmo, poderia repetir? ')
  pass

while True:
 vegana = input(f'{pronome} quer algo da opção vegana? ')
 if vegana == 'lentilha':
  lanche = lanche + lentilha
  break 
 if vegana == 'cebola com batata':
  lanche = lanche + cebola_com_batata
  break
 if vegana == 'não':
  break
 else:
  print('Não entendi')
  pass

print(f'seu hamburger deu = R${lanche}')
final = input('quer finalizar a sua compra? ')
if final == 'sim':
  print('muito obrigado, até breve')
elif final == 'não':
 print('tudo bem, próximo!')