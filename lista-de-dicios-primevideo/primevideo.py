import requests
url_api = "http://localhost:3000/filmes"

def titulo(msg, simbolo="-"):
    print()
    print(msg)
    print(simbolo*40)

#função de inclusão - post
def incluir():
    titulo("Inclusão de Filmes")

    titulo_filme = input("Título do Filme: ")
    genero = input ("Gênero........: ")
    duracao = int(input("Duração (min)..: "))
    preco = float(input("Preço R$........: "))
    datalan = input("Lançamento(d/m/a)........: ")

    partes = datalan.split("/")
    dataformatada = partes[2] + "-" + partes[1] + "-" + partes[0]

    dicionario = {"titulo": titulo_filme, "genero": genero, "duracao": duracao, "preco": preco, "datalan": dataformatada}

    response = requests.post(url_api, json=dicionario)
    if response.status_code == 201:
        filme_incluido = response.json()
        codigo = filme_incluido["id"]
        print(f"Ok! :) Filme cadastrado com o código {codigo}")
    else:
        print("Erro... Não foi possível incluir o filme :(")

#função de listagem - get
def listar():
    titulo("Listagem de Filmes")

    response = requests.get(url_api)
    
    if response.status_code == 200:
        filmes = response.json()
        for filme in filmes:
            print(f"ID: {filme['id']}")
            print(f"Título: {filme['titulo']}")
            print(f"Gênero: {filme['genero']}")
            print(f"Duração: {filme['duracao']} min")
            print(f"Preço: R$ {filme['preco']}")
            datalan = filme['datalan'].split("-")
            dataformatada = datalan[2] + "/" + datalan[1] + "/" + datalan[0]
            print(f"Lançamento: {dataformatada}")
            print("-*" * 20)
    else:
        print("Erro... Não foi possível listar os filmes :(")

#função de agrupamento por gênero - get 
def agrupar():
    titulo("Agrupamento de Filmes por Gênero")

    response = requests.get(url_api)

    if response.status_code == 200:
        filmes = response.json()
        generos_filmes = {}  # dicio q armazena os filmes agrupados por gênero

        for filme in filmes:
            genero = filme['genero']

            # verifica genero
            if genero in generos_filmes:
                generos_filmes[genero].append(filme)
            else:
                generos_filmes[genero] = [filme]

        # exibe os filmes agrupados por genero
        for genero, filmes_do_genero in generos_filmes.items():
            titulo(f"Filmes do Gênero: {genero}")
            for filme in filmes_do_genero:
                print(f"ID: {filme['id']}")
                print(f"Título: {filme['titulo']}")
                print(f"Duração: {filme['duracao']} min")
                print(f"Preço: R$ {filme['preco']}")
                datalan = filme['datalan'].split("-")
                dataformatada = datalan[2] + "/" + datalan[1] + "/" + datalan[0]
                print(f"Lançamento: {dataformatada}")
                print("-" * 40)
    else:
        print("Erro... Não foi possível listar os filmes por gênero :(")


#função de pesquisa por palavra chave = titulo - get
def pesquisar():
    titulo("Pesquisa por Título e/ou Gênero")

    palavra_chave = input("Digite a palavra-chave (Título ou Gênero): ")

    response = requests.get(url_api)

    if response.status_code == 200:
        filmes = response.json()
        resultados = []  # lista p armazenar os filmes correspondentes a pesquisa

        for filme in filmes:
            if (palavra_chave.lower() in filme['titulo'].lower()) or (palavra_chave.lower() in filme['genero'].lower()):
                resultados.append(filme)

        if resultados:
            print(f"Resultados da pesquisa para '{palavra_chave}':")
            for filme in resultados:
                print(f"ID: {filme['id']}")
                print(f"Título: {filme['titulo']}")
                print(f"Gênero: {filme['genero']}")
                print(f"Duração: {filme['duracao']} min")
                print(f"Preço: R$ {filme['preco']}")
                datalan = filme['datalan'].split("-")
                dataformatada = datalan[2] + "/" + datalan[1] + "/" + datalan[0]
                print(f"Lançamento: {dataformatada}")
                print("-" * 40)
        else:
            print(f"Nenhum filme encontrado com a palavra-chave '{palavra_chave}'.")
    else:
        print("Erro... Não foi possível encontrar os filmes :(")


# -------------------------------------------------- Programa Principal
while True:
    titulo("Cadastro de Filmes - PrimeVideo")
    print("1. Inclusão de Filmes")
    print("2. Listagem de Filmes")
    print("3. Agrupar por Gênero")
    print("4. Pesquisar por Palavras Chave") #exercício 
    print("5. Finalizar")
    
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        agrupar()
    elif opcao == 4:
        pesquisar()
    else:
        break   
                
