class Desenho:
    def desenha_forca(erros: int) -> None:
        print("  _______     ")
        print(" |/      |    ")

        if(erros == 1):
            print (" |      (_)   ")
            print (" |            ")
            print (" |            ")
            print (" |            ")

        if(erros == 2):
            print (" |      (_)   ")
            print (" |      \     ")
            print (" |            ")
            print (" |            ")

        if(erros == 3):
            print (" |      (_)   ")
            print (" |      \|    ")
            print (" |            ")
            print (" |            ")

        if(erros == 4):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |            ")
            print (" |            ")

        if(erros == 5):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |            ")

        if(erros == 6):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |      /     ")

        if (erros == 7):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    def imprime_mensagem_vencedor() -> None:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


    def imprime_mensagem_perdedor(palavra_secreta: str) -> None:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|    X       X  | /   ")
        print(" |   XXX     XXX   |/     ")
        print(" |    X       X   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")