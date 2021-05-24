from tabuleiro import tabuleiro
from random import randint


def linha_aleatoria(local):
    return randint(0, len(local) - 1)


def coluna_aleatoria(local):
    return randint(0, len(local[0]) - 1)


linha_navio1 = linha_aleatoria(tabuleiro)
navio_coluna1 = coluna_aleatoria(tabuleiro)

linha_navio2 = linha_aleatoria(tabuleiro)
navio_coluna2 = coluna_aleatoria(tabuleiro)

linha_navio3 = linha_aleatoria(tabuleiro)
navio_coluna3 = coluna_aleatoria(tabuleiro)

linha_navio4 = linha_aleatoria(tabuleiro)
navio_coluna4 = coluna_aleatoria(tabuleiro)

linha_navio5 = linha_aleatoria(tabuleiro)
navio_coluna5 = coluna_aleatoria(tabuleiro)
