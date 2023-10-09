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
    pass

#função de agrupamento - get 
def agrupar():
    pass

#função de agrupamento - get
def pesquisar():
    pass

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
                
