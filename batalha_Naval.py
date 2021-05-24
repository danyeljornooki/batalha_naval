from tabuleiro import tabuleiro
from Local_Navio import linha_navio1, navio_coluna1, linha_navio2, navio_coluna2
from Local_Navio import linha_navio3, navio_coluna3, linha_navio4, navio_coluna4
from Local_Navio import linha_navio5, navio_coluna5

print('=====Batalha Naval=====')
print("Objetivo: Escreva um número de 0 a 9\n"
      "para decidir a linha e a coluna aonde\n"
      "ira ataca; serão 30 turno para tentar\n"
      "acertar pelo menos 3 navios de guerra\n"
      "caso erre mais que 3 ira perder o jogo.")

print('=' * 40)
start = input('Deseja começar a jogar sim(s) ou não(n)?\n')
validar = False
while not validar:

    if start == 's':
        def mapa(local):
            for linha in local:
                print(''.join(linha))
        print("===Começando o jogo===")
        pontos = 0
        mapa(tabuleiro)

        for turno in range(30):
            Escolha_linha = int(input("Escolha um linha para atacar:"))
            while Escolha_linha > 9 or Escolha_linha < 0:
                print('escolha novamente')
                Escolha_linha = int(input("Escolha um linha para atacar:"))
            Escolha_coluna = int(input("Escolha um coluna para atacar:"))

            while Escolha_coluna > 9 or Escolha_coluna < 0:
                print('escolha novamente')
                Escolha_coluna = int(input("Escolha um coluna para atacar:"))
            print('=' * 40)

            if Escolha_linha == linha_navio1 and Escolha_coluna == navio_coluna1:
                print('Turno ', turno + 1)
                tabuleiro[Escolha_linha][Escolha_coluna] = " O "
                print(f'pontos: ', pontos)
                print('Boa acertou!')
                mapa(tabuleiro)
                pontos += 1

            elif Escolha_linha == linha_navio2 and Escolha_coluna == navio_coluna2:
                print('Turno ', turno + 1)
                tabuleiro[Escolha_linha][Escolha_coluna] = " O "
                print(f'pontos: ', pontos)
                print('Boa acertou!')
                mapa(tabuleiro)
                pontos += 1

            elif Escolha_linha == linha_navio3 and Escolha_coluna == navio_coluna3:
                print('Turno ', turno + 1)
                tabuleiro[Escolha_linha][Escolha_coluna] = " O "
                print(f'pontos: ', pontos)
                print('Boa acertou!')
                mapa(tabuleiro)
                pontos += 1

            elif Escolha_linha == linha_navio4 and Escolha_coluna == navio_coluna4:
                print('Turno ', turno + 1)
                tabuleiro[Escolha_linha][Escolha_coluna] = " O "
                print(f'pontos: ', pontos)
                print('Boa acertou!')
                mapa(tabuleiro)
                pontos += 1

            elif Escolha_linha == linha_navio5 and Escolha_coluna == navio_coluna5:
                print('Turno ', turno + 1)
                tabuleiro[Escolha_linha][Escolha_coluna] = " O "
                print(f'pontos: ', pontos)
                print('Boa acertou!')
                mapa(tabuleiro)
                pontos += 1

            else:
                if (Escolha_linha < 0 or Escolha_linha > 9) or (Escolha_coluna < 0 or Escolha_coluna > 9):
                    print("Escolha um lugar válido.")
                    turno -= 1
                elif tabuleiro[Escolha_linha][Escolha_coluna] == " O ":
                    print("Você já escolheu esse lugar!.")
                    turno -= 1
                else:
                    tabuleiro[Escolha_linha][Escolha_coluna] = " O "
                print('Turno ', turno + 1)
                print(f'pontos: ', pontos)
                mapa(tabuleiro)
            if pontos == 5:
                print('Você derrubou todos os navios')
                break
            if turno >= 30:
                print('=' * 40)
                print("Acabaram os turno")
                break

        print(f'Você fez {pontos} pontos.')
        if pontos == 4:
            print(f'Você derrubou {pontos} navios, você ganhou!!')
        elif pontos <= 3:
            print('Você perdeu!!')
        print(f"A localização era:\n"
              f"Navio 1 linha:", linha_navio1, "coluna:", navio_coluna1, '\n'
              f"Navio 2 linha:", linha_navio2, "coluna:", navio_coluna2, '\n'
              f"Navio 3 linha:", linha_navio3, "coluna:", navio_coluna3, '\n'
              f"Navio 4 linha:", linha_navio4, "coluna:", navio_coluna4, '\n'
              f"Navio 5 linha:", linha_navio5, "coluna:", navio_coluna5)
        break

    elif start == 'n':
        print('Okay')
        break
    else:
        print('não entendi')
        start = input('Deseja começar a jogar sim(s) ou não(n)')
