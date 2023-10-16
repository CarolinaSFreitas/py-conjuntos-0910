nome1 = set()
nome2 = set()

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*40)


def inclusao():
    titulo("Inclusão dos Nomes para Análise")

    while True:
        aux1 = input("1º Nome: ")
        #strip() retira os espaços no inicio e final da string
        if " " in aux1.strip():
            break
        else:
            print("Por favor, digite um nome completo :S")

    while True:
        aux2 = input("2º Nome: ")
        #strip() retira os espaços no inicio e final da string
        if " " in aux2.strip():
            break
        else:
            print("Por favor, digite um nome completo :S")


    #desta forma nao precisa o global, porque a inclusao só pode ocorrer no conjunto (nome1) ja declarado 
   #for letra in aux1:
    #    nome1.add(letra)

    aux1 = aux1.lower().replace(" ", "")        #converte p minuscula e tira os espaços dos nomes q podem vir no conjunto de intersec
    aux2 = aux2.lower().replace(" ", "")        #converte p minuscula e tira os espaços dos nomes q podem vir no conjunto de intersec

    global nome1
    global nome2
    nome1 = set(aux1)
    nome2 = set(aux2)
    print("Ok! Nomes cadastrados com sucesso :)")


def interseccao():
    titulo("Intersecção das Letras dos Nomes")

    #outra opçao: intersect = nome1 & nome2
    intersect = nome1.intersection(nome2)

    #converte em lista (e já ordena)
    lista = sorted(list(intersect))

    #outras formas:
    #lista.sort()            #classifica a própria lista
    #lista2 = sorted(lista)  #mantem a lista original e cria outra classificada

    print(f"Letras Comuns: {lista}")


def diferenca():
    titulo("Diferença de Letras Entre os Nomes")

    #so1 = nome1 & nome2
    so1 = nome1.difference(nome2)
    so2 = nome2.difference(nome1)

    #converte em lista (e já ordena)
    lista1 = sorted(list(so1))
    lista2 = sorted(list(so2))

    print(f"Só existe no 1º nome: {lista1}")
    print(f"Só existe no 2º nome: {lista2}")


def uniao():
    titulo("União das Letras dos Nomes")

    # uniao = nome1 | nome2
    uniao = nome1.union(nome2)
    
    #converte em lista (e já ordena)
    lista = sorted(list(uniao))

    print(f"Todas as Letras dos Nomes: {lista}")


def alfabeto():
    titulo("Letras do Alfabeto Ausentes nos Nomes")

    alfabeto = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    #outra forma: ausentes = alfabeto - (nome1 | nome2)
    ausentes = alfabeto.difference(nome1.union(nome2))

    #converte em lista (e já ordena)
    lista = sorted(list(ausentes))

    print(F"Letras Ausentes nos Nomes: {lista}")

#--------------------------------------------------------------------programa principal
while True:
    titulo("Conjuntos: Manipulação de Letras de Nomes")
    print("1. Inclusão dos Nomes")
    print("2. Intersecção das Letras")
    print("3. Diferença das Letras")
    print("4. União das Letras")
    print("5. Letras do Alfabeto Ausentes")
    print("6. Sair")

    opcao = int(input("Opção: "))
    if opcao == 1:
        inclusao()
    elif opcao == 2:
        interseccao()
    elif opcao == 3:
        diferenca()
    elif opcao == 4:
        uniao()
    elif opcao == 5:
        alfabeto()
    else:
        break

