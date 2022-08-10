# imports
from exercicios import fibonacci
from exercicios import percentual

def mostra_cabecalho():
      # Cabeçalho
      print("\n******************************************************\n"
            "* PROCESSO SELETIVO TARGET SISTEMAS - By: Caio Luppo *\n"
            "******************************************************\n")

      # Opções
      print("1 - Sequência de Fibonacci\n"
            "2 - Faturamento diário\n"
            "3 - Percentual de representação\n"
            "4 - Inverter caracteres de uma String\n"
            "sair - Sai do programa\n")

def escolhe_questao():

      mostra_cabecalho()

      opcoes = [1, 2, 3, 4]

      while True:
            opcao_escolhida = input("Escolha uma opção: ")
            try:
                  opcao = int(opcao_escolhida)
                  if opcao in opcoes:
                        match opcao:
                              case 1:
                                    fibonacci.init()
                                    mostra_cabecalho()
                              case 2:
                                    print("")
                              case 3:
                                    percentual.init()
                                    mostra_cabecalho()
                              case 4:
                                    print("Op4")
                  else:
                        print('\033[91m' + "Oops! Opção inválida, digite um número entre 1 e 4!" + '\033[0m')
            except:
                  if opcao_escolhida == "sair":
                        return
                  else:
                        print("Opção inválida")


if __name__ == '__main__':
    escolhe_questao()