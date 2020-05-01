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


def lista_de_caracteres(conjunto: str) -> str:
    """
        Funcao que pegar conjunto de caracteres.
    """

    #conjunto = str(input("{}".format(string_do_programa)))
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

    entrada = open("entrada.txt", "r")
    arquivo_entrada = entrada.readlines()
    arquivo_entrada = [i.replace("\n", "") for i in arquivo_entrada]
    # primeira linha do arquivo txt
    linha_atual = 0
    # linha 1 pega o numero de estados
    num_estados = int(arquivo_entrada[linha_atual])
    # percorre as linhas do arquivo txt
    linha_atual += 1
    # linha 2 pega o numero de estados
    lista_com_caracteres = lista_de_caracteres(arquivo_entrada[linha_atual])
    linha_atual += 1
    # linha 3 pega o numero de estados iniciais
    estados_iniciais = arquivo_entrada[linha_atual]
    linha_atual += 1
    # linha 4 pega o numero de estados de aceitacao
    estados_aceitacao = lista_de_caracteres(arquivo_entrada[linha_atual])
    linha_atual += 1
    # linha 5 pega o numero de transicoes da maquina
    num_transicoes = int(arquivo_entrada[linha_atual])

    automato_finito = {}
    # para cada operacao de transicao
    for transicao in range(num_transicoes):
        linha_atual += 1
        operacao = str(arquivo_entrada[linha_atual])
        #                    estado   +   simbolo terminal ->   outro estado
        automato_finito[str(operacao[0]) + str(operacao[2])] = str(operacao[4])

    linha_atual += 1
    # pega o numero de cadeias de entrada
    cadeias_entrada = int(arquivo_entrada[linha_atual])
    # cria a saida do programa em txt
    saida = open("saida do programa.txt", "w")
    # para cada cadeia de entrada
    for entrada in range(cadeias_entrada):
        linha_atual += 1
        entrada_input = str(arquivo_entrada[linha_atual])
        # estado q0
        estado_atual = list(automato_finito.keys())[0][0]
        # para cada indice da entrada (letra)
        for i in range(len(entrada_input)):
            # se o indice for vazio
            if entrada_input[i] == '-':
                estado_atual = '-'
            else:
                # o estado atual é o resultado de onde aponta o estado anterior com sua transicao
                # foi desenvolvido com o dicionario, a chave aponta para um valor
                # o estado anterior é a chave e o estado atual é o valor
                estado_atual = automato_finito[estado_atual +
                                               str(entrada_input[i])]
        # para cada estado de aceitacao
        for aceitar in estados_aceitacao:
            # se o estado atual for um estado de aceitacao, printa-se aceita
            if estado_atual == aceitar:
                print("aceita")
                saida.write("aceita\n")
            # caso contrario printa rejeita
            else:
                print("rejeita")
                saida.write("rejeita\n")
    # fecha o arquivo de saida
    saida.close()


# inicia o programa
if __name__ == "__main__":
    main()
