def init():
    mostra_cabeçalho()
    while True:
        valores = {
            'SP' : 67836.43,
            'RJ' : 36678.66,
            'MG' : 29229.88,
            'ES' : 27165.48,
            'Outros' : 19849.53
        }

        total = 0
        for estado in valores:
            total += valores[estado]

        for estado in valores:
            percentual = (100*valores[estado])/total
            print(f'{estado}: {percentual:.2f}%')

        if input("\nRepetir? (S/n): ") in ['N', 'n']:
            break
        print("")

def mostra_cabeçalho():
    print("\n"
          "*******************************\n"
          "* Percentual de representação *\n"
          "*******************************\n")

if __name__ == '__main__':
    init()