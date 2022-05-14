# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
Mediante este script se implementará el algoritmo de colas cerradas y se representará el resultado en una gráfica.
"""
from typing import List


def main():
    global RVisita, Qi, TServicio, Respuesta, ZReflexion

    print("Inserte razones de visita separadas por comas:")

    RVisita = input().split(",")
    print("Inserte tiempos de servicios separados por comas:")
    TServicio = input().split(",")
    dispositivos = len(RVisita)

    print("Inserte N:")
    nmax = int(input())
    print("Inserte Z:")
    ZReflexion = int(input())

    # The device response time
    # Ri(N) = Si (1+Qi(N-1))
    Respuesta = [len(RVisita)][0]

    # The device queue lengths Qi(n) == Ni(n) with N jobs in the network using Little's law are:
    # Qi(n) = X(n) * Vi * Ri(n)
    Qi = [len(RVisita)][0]

    # R(n) = Sum(i=1,K)Vi * Ri(n)
    R = [0]

    # X(n) = n / Z + R(n)

    X = [0]

    # The device queue lengths Ni(n) with N jobs in the network using Little's law are:

    Xi = [len(RVisita)][0]
    Ui = [len(RVisita)][0]

    for i in range(dispositivos):
        Qi[i].append(0)
    users = 0

    users += 1

    for users in range(nmax):

        for i in range(dispositivos):
            Respuesta[i].append(TServicio[i] * (1 + Qi[i][users - 1]))

        sum = 0
        for i in range(dispositivos):
            sum += Respuesta[i] * RVisita[i]
        R.append(sum)

        X.append(users / (ZReflexion + R[len(R)]))

        for i in range(dispositivos):
            Qi[i].append(X[i] * Respuesta[i][0] * RVisita[i])


if __name__ == '__main__':
    main()
