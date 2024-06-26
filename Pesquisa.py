import os

# Lista de documentos e empréstimos (atenção é só uma simulação de banco de dados)
documentos = []
emprestimos = []

# Função para cadastrar um novo documento
def cadastrar_documento():
    titulo = input("Digite o título do documento: ")
    data = input("Digite a data de produção do documento: ")
    tema = input("Digite o tema do documento: ")
    contexto = input("Digite o contexto histórico do documento: ")
    descricao = input("Digite a descrição do documento: ")
    autor_nome = input("Digite o nome do autor do documento: ")
    localizacao = input("Digite a localização na biblioteca: ")

    #Aqui é feita a criação de um documento como dicionário
    documento = {
        'titulo': titulo,
        'data': data,
        'tema': tema,
        'contexto': contexto,
        'descricao': descricao,
        'autor': autor_nome,
        'localizacao': localizacao,
        'materiais_relacionados': [],
        'figura_historica': None
    }

    documentos.append(documento)
    print("Documento cadastrado com sucesso.")

#Função para realizar o empréstimo
def realizar_emprestimo():
    if not documentos:
        print("Não há documentos cadastrados para empréstimo.")
        return

    print("Selecione um documento para empréstimo:")
    for i, doc in enumerate(documentos):
        print(f"{i+1}. {doc['titulo']}")

    try:
        escolha = int(input("Digite o número correspondente ao documento: ")) - 1
        documento_emprestimo = documentos[escolha]
        periodo_emprestimo = input("Digite o período de empréstimo: ")
        nome_evento = input("Digite o nome do evento/exposição: ")
        responsavel = input("Digite o responsável pelo evento: ")
        tema_evento = input("Digite o tema do evento: ")

        emprestimo = {
            'documento': documento_emprestimo,
            'periodo_emprestimo': periodo_emprestimo,
            'nome_evento': nome_evento,
            'responsavel': responsavel,
            'tema_evento': tema_evento
        }

        emprestimos.append(emprestimo)
        print("Empréstimo registrado com sucesso.")
    except IndexError:
        print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Valor inválido. Tente novamente.")

#Função para listar os documentos cadastrados
def listar_documentos():
    if not documentos:
        print("Não há documentos cadastrados.")
        return

    for doc in documentos:
        print(f"Título: {doc['titulo']}")
        print(f"Autor: {doc['autor']}")
        print(f"Data de Produção: {doc['data']}")
        print(f"Tema: {doc['tema']}")
        print("-----")

#Função para salvar os documentos em um arquivo
def salvar_documentos():
    with open('documentos.txt', 'w') as f:
        for doc in documentos:
            f.write(f"Título: {doc['titulo']}\n")
            f.write(f"Autor: {doc['autor']}\n")
            f.write(f"Data de Produção: {doc['data']}\n")
            f.write(f"Tema: {doc['tema']}\n")
            f.write("-----\n")

#Função principal
def main():
    while True:
        print("\n### Menu ###")
        print("1. Cadastrar novo documento")
        print("2. Realizar empréstimo")
        print("3. Listar documentos cadastrados")
        print("4. Salvar e sair")

        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            cadastrar_documento()
        elif opcao == '2':
            realizar_empréstimo()
        elif opcao == '3':
            listar_documentos()
        elif opcao == '4':
            salvar_documentos()
            print("Saindooo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
