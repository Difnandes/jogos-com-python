class Titulos:
    def montar_titulo(nome: str, flag: int) -> None:
        print("*********************************")
        if flag == 1:
            print("******Escolha o seu jogo!********")
        elif flag == 2:
            print(f"Bem vindo ao jogo de {nome}!")
        else:
            raise NotImplementedError('flag nao implementada')
        print("*********************************\n")