import json

def init():

    mostra_cabecalho()

    # Define o caminho relativo do arquivo
    if __name__ == '__main__':
        path = 'dados/dados.json'
    else:
        path = 'exercicios/dados/dados.json'

    # Acessa o arquivo
    with open(path, 'r') as arquivo:
        dados = json.load(arquivo)

    while True:
        opcao_escolhida = input("Digite uma opção: ")
        try:
            opcao = int(opcao_escolhida)
            match opcao:
                case 1:
                    _maior_valor_mes(dados)
                case 2:
                    _menor_valor_mes(dados)
                case 3:
                    _valor_acima_media(dados)
                case _:
                    print("\n\033[91mOpção inválida, digite um número entre 1 e 3!\033[0m\n")
        except:
            if opcao_escolhida == 'sair':
                return
            else:
                print("\n\033[91mOpção inválida, digite um número entre 1 e 3 ou 'sair'!\033[0m\n")
                continue


def _menor_valor_mes(dados):
    valores = []

    for dia in dados:
        if dia['valor'] != 0.0:
            valores.append(dia["valor"])

    return print("\n\033[94m-- Maior faturamento --\n"
                 f"Dia: {valores.index(min(valores)) + 1:18.0f}\n"
                 f"Valor:   R$ {min(valores):11.2f}\n\033[0m")

def _maior_valor_mes(dados):
    valores = []

    for dia in dados:
        if dia['valor'] != 0.0:
            valores.append(dia["valor"])

    return print("\n\033[94m-- Maior faturamento --\n"
                 f"Dia: {valores.index(max(valores))+1:18.0f}\n"
                 f"Valor:   R$ {max(valores):11.2f}\n\033[0m")

def _valor_acima_media(dados):

    dias_acima_media = 0

    qtd_dias = 0
    total = 0

    for dia in dados:
        qtd_dias += 1
        total = total + dia['valor']

    media = total/qtd_dias

    for dia in dados:
        if dia['valor'] != 0:
            if dia['valor'] > media:
                dias_acima_media += 1

    return print("\n\033[94m-- Dias acima da média --\n"
                 f"Dias:                  {dias_acima_media}\n\033[0m")


def mostra_cabecalho():
    print("\n****************************************\n"
          "* Informações sobre faturamento diário *\n"
          "****************************************\n")

    print("1 - Maior valor no mês\n"
          "2 - Menor valor no mês\n"
          "3 - Número de dias com valor acima da média\n"
          "\nsair - Volta para o menu ou sai do programa\n")


if __name__ == '__main__':
    init()