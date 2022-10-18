import random
from typing import List

from titulos import Titulos
from desenho import Desenho


def jogar() -> None:
    Titulos.montar_titulo('Forca', 2)
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            Desenho.desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        Desenho.imprime_mensagem_vencedor()
    else:
        Desenho.imprime_mensagem_perdedor(palavra_secreta)

def marca_chute_correto(chute: str, letras_acertadas: List[str], palavra_secreta: str) -> None:
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def pede_chute() -> str:
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra: str) -> List[str]:
    return ["_" for letra in palavra]

def carrega_palavra_secreta() -> str:
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

if(__name__ == "__main__"):
    jogar()
