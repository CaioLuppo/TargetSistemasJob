
# Cabeçalho
print("******************************************************\n"
      "* PROCESSO SELETIVO TARGET SISTEMAS - By: Caio Luppo *\n"
      "******************************************************\n")

# Opções
print("1 - Sequência de Fibonacci\n"
      "2 - Faturamento diário\n"
      "3 - Percentual de representação\n"
      "4 - Inverter caracteres de uma String\n")

# Código para seleção

options = [1, 2, 3, 4]

while True:
      option = int(input("Escolha uma opção: "))
      if option in options:
            match option:
                  case 1:
                        print("Op1")
                        break
                  case 2:
                        print("Op2")
                        break
                  case 3:
                        print("Op3")
                        break
                  case 4:
                        print("Op4")
                        break
      print('\033[91m'+"Oops! Opção inválida, digite um número entre 1 e 4!"+'\033[0m')