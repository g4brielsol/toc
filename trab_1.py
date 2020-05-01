def input_inteiro(string_do_programa: str) -> int:
    """
        Coleta um numero inteiro digitado pelo usuario.
    """

    numero = int(input("{}".format(string_do_programa)))
    return numero


def limite_inferior_superior(input_usuario: int, limite_inferior: int, limite_superior: int) -> bool:
    """
        Funcao que checa se o numero digitado pelo usuario respeita os limites
    """

    erro = False
    # se a variavel escrita pelo usuario for menor ou maior que os limites, erro é igual a True
    if (input_usuario < limite_inferior) or (input_usuario > limite_superior):
        erro = True
    return erro


def checar_espaco(string: str, posicao_inicial: int):
    """
        checa se os espacos foram colocados corretamente
    """
    # string sem o numero inicial digitado pelo usuario
    string_comeco = string[posicao_inicial:]
    erro = False
    espaco = True
    for i in range(len(string_comeco)):
        # retorna erro caso o indice correspondente ao espaco nao seja espaco
        if espaco == True:
            # espaco vira false porque na proxima iteracao nao e espaco
            espaco = False
            if string_comeco[i] != " ":
                erro = True
                return erro
            else:
                pass
        else:
            # a proxima iteracao da string deve ser espaco
            espaco = True
    return erro

# def checar_caracter(string: str, posicao_inicial: int)


def lista_de_caracteres(string_do_programa: str) -> str:
    """
        Funcao que pegar conjunto de caracteres.
    """

    conjunto = str(input("{}".format(string_do_programa)))
    # se for 10 conjuntos de simbolos
    if conjunto[:2] == '10':
        # se for 10
        dez = True
        # passa a string para checagem de espacos a partir da segunda posicao
        erro = checar_espaco(conjunto, 2)
    # se for um conjunto menor que 10 simbolos
    else:
        # se nao for 10
        dez = False
        if int(conjunto[0]) < 1 or int(conjunto[0]) > 9:
            erro = True
        else:
            # passa a string para checagem de espacos a partir da primeira posicao
            erro = checar_espaco(conjunto, 1)
    # se o usuario digitou erroneamente, digitar de novo
    if erro:
        return erro
    else:
        if dez:
            # elimina o numero 10 e todos os espacos
            caracteres = conjunto[2:].replace(" ", "")
        else:
            # elimina o numero entre 1 e 9 e todos os espacos
            caracteres = conjunto[1:].replace(" ", "")
    return caracteres


def main():
    # linha 1 pega o numero de estados
    erro = True
    # enquanto estiver errado pede novamente ao usuario
    while erro:
        num_estados = input_inteiro(
            "Digite a quantidade de estados entre 1 e 10: ")
        # checa se o numero respeita os limites. se o numero nao respeitar os limites, a funcao vai ser chamada novamente
        erro = limite_inferior_superior(num_estados, 1, 10)

    # linha 2 pega o numero de estados
    erro = True
    # enquanto estiver errado pede novamente ao usuario
    while erro:
        # pega o conjunto de simbolos terminais
        lista_com_caracteres = lista_de_caracteres(
            "Digite a quantidade de simbolos entre 1 e 10. Digite os simbolos: ")
        # checa se o numero respeita os limites. se o numero nao respeitar os limites, a funcao vai ser chamada novamente
        simbolos_terminais = lista_com_caracteres
        # se tudo ocorrer bem, sai do while
        if type(simbolos_terminais) is str:
            erro = False

    # linha 3 pega o numero de estados iniciais
    erro = True
    # enquanto estiver errado pede novamente ao usuario
    while erro:
        estados_iniciais = input_inteiro(
            "Digite a quantidade de estados iniciais entre 1 e 10: ")
        # checa se o numero respeita os limites. se o numero nao respeitar os limites, a funcao vai ser chamada novamente
        erro = limite_inferior_superior(estados_iniciais, 1, 10)

    # linha 4 pega o numero de estados de aceitacao
    erro = True
    # enquanto estiver errado pede novamente ao usuario
    while erro:
        # pega o conjunto de simbolos terminais
        aceitacao = lista_de_caracteres(
            "Digite a quantidade de estados de aceitacao entre 1 e 9 e seus elementos: ")
        # checa se o numero respeita os limites. se o numero nao respeitar os limites, a funcao vai ser chamada novamente
        estados_aceitacao = aceitacao
        # se tudo ocorrer bem, sai do while
        if type(estados_aceitacao) is str:
            erro = False

    # linha 5 pega o numero de transicoes da maquina
    erro = True
    # enquanto estiver errado pede novamente ao usuario
    while erro:
        num_transicoes = input_inteiro(
            "Digite o numero de transicoes da maquina: ")
        # checa se o numero respeita os limites. se o numero nao respeitar os limites, a funcao vai ser chamada novamente
        erro = limite_inferior_superior(num_transicoes, 1, 50)

    automato_finito = {}
    # para cada operacao de transicao
    for transicao in range(num_transicoes):
        operacao = str(input("Digite a operacao de transicao: "))
        #                    estado   +   simbolo terminal ->   outro estado
        automato_finito[str(operacao[0]) + str(operacao[2])] = str(operacao[4])

    # pega o numero de cadeias de entrada
    erro = True
    # enquanto estiver errado pede novamente ao usuario
    while erro:
        cadeias_entrada = input_inteiro(
            "Digite o numero de cadeias de entrada: ")
        # checa se o numero respeita os limites. se o numero nao respeitar os limites, a funcao vai ser chamada novamente
        erro = limite_inferior_superior(cadeias_entrada, 1, 10)

    lista_de_entradas = []
    # pegar cada cadeia de entrada
    for entrada in range(cadeias_entrada):
        entrada_input = str(input("Digite a entrada: "))
        # adiciona a a cadeia de entrada a lista
        lista_de_entradas.append(entrada_input)
    # para cada entrada da lista
    for entrada in lista_de_entradas:
        # estado atual q0
        estado_atual = '0'
        # para cada indice da cadeia de entrada
        for i in range(len(entrada)):
            # se o indice for vazio
            if entrada[i] == '-':
                estado_atual = '-'
            else:
                # estado atual é o resultado de onde aponta o estado anterior com sua transicao
                # foi desenvolvido com o dicionario, a chave aponta para um valor
                # o estado anterior é a chave e o estado atual é o valor
                estado_atual = automato_finito[estado_atual + str(entrada[i])]
        # para cada estado de aceitacao
        for aceitar in estados_aceitacao:
            # se o estado atual for um estado de aceitacao, printa-se aceita
            if estado_atual == aceitar:
                print("aceita")
            # caso contrario printa rejeita
            else:
                print("rejeita")


# inicia o programa
if __name__ == "__main__":
    main()
