'''
o administrador vai fazer o registro de livros que vão ser emprestados
e livros que vão ser devolvidos, pelos professores e alunos

'''
nome = 'Michael Douglas'
livros_fisicos = ['peter pan','um diario de um banana','scott pilgrim vol.3']
livros_virtuais = ['cidades de papel','venom','fisica quantica avançada']
livro_emprestado = []
usuario_aluno = True

def Adm():
    if usuario_aluno == True:
        while True:
            print('Seja bem vindo',nome,'Qual tarefa deseja Executar?')
            print('1.Devolução de livro')
            print('2.Emprestimo de livro')
            print('3.sair')
            registro = int(input(" "))
            if registro == 1:
                print("-Devolução-")
                devolucao = True
                emprestimo = False
                break
            if registro == 2:
                print("-Emprestimo-")
                emprestimo = True
                devolucao = False
                break
            if registro == 3:
                print('Muito obrigado pela preferencia, volte sempre!')
                emprestimo = False
                devolucao = False
            else:
                print('Digite apenas os caracteres presentes nas opções!')
                pass
        while devolucao:
                    livro_emprestado.append('deadpool vs wolverine')
                    print('no seu registro consta o livro',livro_emprestado,
                          'com prazo de 10 dias para sua devolução')
                    print('Para efetuar a devolução,'
                          'vá a unidade com o livro e informe seu registro'
                          'no ato da devolução')
                    break
        while emprestimo:
                    print('como será a forma de emprestimo?')
                    print('1.livros fisicos')
                    print('2.livros virtuais')
                    forma_emprestimo = int(input(''))
                    if forma_emprestimo == 1:
                        print(f"livros fisicos : ",'1-',livros_fisicos[0],',','2-',livros_fisicos[1],',','3-',livros_fisicos[2])
                        nome_do_livro = int(input("Digite o numero do livro"))
                        if nome_do_livro == 1:
                            livro_emprestado.append(livros_fisicos[0])
                            print(livro_emprestado)
                            break
                        if nome_do_livro == 2:
                            livro_emprestado.append(livros_fisicos[1])
                            print(livro_emprestado)
                            break
                        if nome_do_livro == 3:
                            livro_emprestado.append(livros_fisicos[2])
                            print(livro_emprestado)
                            break
                        else:
                            print('Não listado')
                            pass
                    if forma_emprestimo == 2:
                        print(f"livros virtuais disponiveis",livros_virtuais)
                        nome_do_livro = int(input("Digite o numero do livro"))
                        if nome_do_livro == 1:
                            livro_emprestado.append(livros_virtuais[0])
                            print(livro_emprestado)
                            break
                        if nome_do_livro == 2:
                            livro_emprestado.append(livros_virtuais[1])
                            print(livro_emprestado)
                            break
                        if nome_do_livro == 3:
                            livro_emprestado.append(livros_virtuais[2])
                            print(livro_emprestado)
                            break
                        else:
                            print('Não listado')
                            pass
                        break
                    
Adm()