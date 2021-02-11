
#Jogo do NIM, uma das atividades do curso de introdução à ciência da computação da USP. 
#Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. 
#Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. 
#Quem tirar as últimas peças possíveis ganha o jogo.

#Existe uma lógica para sempre vencer no jogo, e o objetivo desse código é implementá-lo de forma que
#o computador sempre vença.

def computador_escolhe_jogada(n,m):
    jogada = 1
    melhorJogada = m
    while jogada <= m:
        if multiplo(n-jogada,m+1):
            melhorJogada = jogada
        jogada += 1
    return melhorJogada
    

def usuario_escolhe_jogada(n,m):
    jogada = 0
    jogadaValida = False
    while jogadaValida == False:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada <=m and jogada>0:
            jogadaValida = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")
    return jogada

def multiplo(valorAvaliado,valorBase):
    if valorAvaliado % valorBase == 0:
        return True
    else:
        return False

def partida():
    print("Você escolheu jogar uma partida isolada!")
    n_input = int(input("Quantas peças? "))
    m_input = int(input("Limite de peças por jogada? "))
    n = n_input
    usuarioComeca = vezUsuario = multiplo(n_input, m_input+1)
    if usuarioComeca:
        print("Você começa!")
        print("")
    else:
        print("Computador começa!")
        print("")

    while n>0:
        if vezUsuario:
            jogadaUsu = usuario_escolhe_jogada(n,m_input)
            print("Você tirou",jogadaUsu,"peça(s)")
            n = n - jogadaUsu
            print("Agora restam",n,"peças no tabuleiro.")
            vezUsuario = False
        else:
            jogadaPc = computador_escolhe_jogada(n,m_input)
            print("O computador tirou",jogadaPc,"peça(s)")
            n = n - jogadaPc
            print("Agora restam",n,"peças no tabuleiro.")
            vezUsuario = True

    if n==0 and vezUsuario == True:
        print("O computador ganhou!")
    else:
        print("Você ganhou!")

def campeonato():
    print("Você escolheu um campeonato!")
    rodada = 0
    while rodada != 3:
        print("**** Rodada,",rodada+1,"****")
        partida()
        rodada += 1
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    opcao = int(input("2 - para jogar um campeonato" ))
    if opcao == 1:
        partida()
    else:
        campeonato()

main()
