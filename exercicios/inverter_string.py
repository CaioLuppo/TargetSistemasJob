def init():
    mostra_cabecalho()
    while True:

        string_digitada = input("Digite uma string: ")
        string_invertida = ''

        for letra in string_digitada:
            string_invertida = letra + string_invertida
        print(f"A string invertida é: {string_invertida}")

        if input("\nRepetir? (S/n): ") in ['N', 'n']:
            break
        print("")

    pass

def mostra_cabecalho():
    print("\n******************\n"
          "* Inverter string *\n"
          "*******************\n")

if __name__ == '__main__':
    init()