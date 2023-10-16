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

    global nome1
    global nome2
    nome1 = set(aux1.lower())
    nome2 = set(aux2.lower())
    print("Ok! Nomes cadastrados com sucesso :)")


def interseccao():
    titulo("Intersecção das Letras dos Nomes")

    intersect = nome1.intersection(nome2)
    print("")






def diferenca():
    pass


def uniao():
    pass


def alfabeto():
    pass

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

