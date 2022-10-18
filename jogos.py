import forca
import adivinhacao

from titulos import Titulos

def escolha_jogo() -> None:
    Titulos.montar_titulo('', 1)

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("\nJogando forca\n")
        forca.jogar()
    elif(jogo == 2):
        print("\nJogando adivinhação\n")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()