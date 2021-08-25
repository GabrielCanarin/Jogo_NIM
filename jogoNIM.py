def regras():
    print("\n Informe o número de peças inicial e o número máximo de peças que é possível retirar em uma rodada.\n A cada rodada você escolhe quantas peças quer tirar, apos isso é a vez do computador.\n Quem tirar a ultima peça vence a partida!\n")

def computador_escolhe_jogada(n,m):
    if n < m:
        return n
    else:
        v = n % (m+1)
        if v > 0:
            return v
        return m

def usuario_escolhe_jogada(n,m):
    j = 0
    while j == 0:
        j = int(input("Qual o valor da sua jogada: "))
        if j > m or j < 1 or j > n:
            print("Jogada invalida!\n")
            j = 0
    return j

def partida():
    n = int(input("Quantas peças tera o jogo? "))
    m = int(input("Quantas peças poderam ser tiradas por rodada? "))
    print("")

    comp = True
    if n % (m+1) == 0:
        comp = False
    
    if comp:
        print("Computador começa!")
    else:
        print("Você começa!")
    
    while n > 0:
        if comp:
            jogada = computador_escolhe_jogada(n,m)
            comp = False
            print("O computador tirou", jogada ,"peça/as.")
        else:
            jogada = usuario_escolhe_jogada(n,m)
            comp = True
            print("Você retirou ", jogada, "peça/as.")

        n = n - jogada
        print("Restam", n,"peça/as.\n")

    if comp:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def campeonato():
    usuario = 0
    computador = 0

    for _ in range(3):
        vencedor = partida()
        if vencedor == 1 :
            usuario = usuario + 1
        else:
            computador = computador + 1
    print("Placar: Você: ", usuario, "X", computador, "Computador: ")

tipo_de_partida = 0

while tipo_de_partida == 0:
    print("\nBem-vindo ao jogo do NIM! Escolha: \n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    print("3 - para regras\n")

    tipo_de_partida = int(input())

    if tipo_de_partida == 1:
        print("\nPartida isolada")
        partida()
        tipo_de_partida = 0
    elif tipo_de_partida == 2:
        print("\nCampeonato")
        campeonato()
        tipo_de_partida = 0
    elif tipo_de_partida == 3:
        regras()
        tipo_de_partida = 0
    else:
        print("\nOpção invalida")
        tipo_de_partida = 0
    