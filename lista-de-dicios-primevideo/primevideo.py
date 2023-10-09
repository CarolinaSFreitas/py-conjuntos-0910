import requests
url_api = "http://localhost:3000/filmes"

def titulo(msg, simbolo="-"):
    print()
    print(msg)
    print(simbolo*40)

#1. função de inclusão - post
def incluir():
    titulo("Inclusão de Filmes")

    titulo_filme = input("Título do Filme........: ")
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

#2. função de listagem - get
def listar():
    titulo("Listagem de Filmes")

    response = requests.get(url_api)
    
    print("Cód. Título do Filme.........: Gênero.........: Tempo..: Preço...: Lançamento")

    if response.status_code == 200:
        filmes = response.json()
        for filme in filmes:
            print(f"{int(filme['id']):4d}", end=" ")
            print(f"{filme['titulo']:25}", end=" ")
            print(f"{filme['genero']:15}", end=" ")
            print(f"{int(filme['duracao']):4d}m", end=" ")
            print(f"{float(filme['preco']):9.2f}", end="    ")
            print(f" {filme['datalan'][:10]}")
    else:
        print("Erro... Não foi possível listar os filmes :(")

#3. função de agrupamento por gênero - get 
def agrupar():
    titulo("Agrupamento de Filmes por Gênero")

    response = requests.get(url_api)

    if response.status_code == 400:
        print("Erro... Não foi possível consultar a API :( )")
        return

    filmes = response.json()

    generos = []
    numeros = []

    for filme in filmes:
        if filme['genero'] in generos:
            posicao = generos.index(filme['genero'])
            numeros[posicao] += 1
        else:
            generos.append(filme['genero'])
            numeros.append(1)

    for gen, num in zip(generos, numeros):
        print(f"{gen}: {num}")

#4. função de pesquisa por palavra chave = titulo - get
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
                print()
                print("-*" * 20)
                print(f"Título........: {filme['titulo']}")
                print(f"Gênero........: {filme['genero']}")
                print(f"Duração.......: {filme['duracao']} min")
                print(f"Preço........: R$ {filme['preco']}")
                print(f"Lançamento.......:{filme['datalan'][:10]}")
                print("-*" * 20)
                print()
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
                
