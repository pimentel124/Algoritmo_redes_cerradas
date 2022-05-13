# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
Mediante este script se implementará el algoritmo de colas cerradas y se representará el resultado en una gráfica.
"""


def main():
    print("Inserte razones de visita separadas por comas:")
    Vi = input().split(",")
    print("Inserte tiempos de servicios separados por comas:")
    Si = input().split(",")
    print("Inserte N:")
    nmax = int(input())
    print("Inserte Z:")
    Z = int(input())

    # The device response time
    # Ri(N) = Si (1+Qi(N-1))
    Ri = [0]

    # The device queue lengths Qi(n) == Ni(n) with N jobs in the network using Little's law are:
    # Qi(n) = X(n) * Vi * Ri(n)
    Qi = [0]

    # R(n) = Sum(i=1,K)Vi * Ri(n)

    # X(n) = n / Z + R(n)

    # The device queue lengths Ni(n) with N jobs in the network using Little's law are:

    Xi = [0]
    Ui = [0]

    Qi.append(0)


    counter = 1
    while counter<=nmax:
        Ni.append()









if __name__ == '__main__':
    main()


