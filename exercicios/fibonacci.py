def init():

    _mostra_cabeçalho()

    while True:
        opcao = input("Entrada: ")
        try:
            numero_escolhido = int(opcao)
            _verifica_existencia(numero_escolhido)
        except:
            if opcao == 'sair':
                print('')
                return
            else:
                print("Opção inválida.")
                continue


def _mostra_cabeçalho():

    # Banner
    print("**************************\n"
          "* Sequência de Fibonacci *\n"
          "**************************\n")

    # Descrição
    print("Digite um número e direi se pertence ou não à sequência! Se quiser voltar ao menu, digite 'sair'.")

def _verifica_existencia(numero_escolhido):

    posicao1 = 0
    posicao2 = 1
    resultado = 0

    for contador in range(0, numero_escolhido+1):
        if numero_escolhido in [0, 1]:
            return print(f"\033[92mO número existe na sequência e está na {str(numero_escolhido)}º posição! \033[0m")
        resultado = posicao1 + posicao2
        posicao1 = posicao2
        posicao2 = resultado
        if resultado == numero_escolhido:
            return print(f"\033[92mO número existe na sequência e está na {str(contador+3)}º posição! \033[0m")

    return print("\033[91mO número informado não existe na sequência! \033[0m")

if __name__ == '__main__':
    init()