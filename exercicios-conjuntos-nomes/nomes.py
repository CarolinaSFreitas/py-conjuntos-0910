nome1 = set()
nome2 = set()

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*40)

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

