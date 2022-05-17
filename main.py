# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
Mediante este script se implementará el algoritmo de colas cerradas y se representará el resultado en una gráfica.
"""
import pprint

import pandas as pd
import matplotlib.pyplot as plt

def main():
    global RVisita, Qi, TServicio, Respuesta, ZReflexion

    print("Inserte N:")
    nmax = int(input())

    print("Inserte razones de visita separadas por comas:")

    RVisita_str = input().split(",")

    # Se convierte la lista de str a lista de int
    RVisita = [int(i) for i in RVisita_str]

    print("Inserte tiempos de servicios separados por comas:")
    TServicio_str = input().split(",")
    # Se convierte la lista de str a lista de int
    TServicio = [float(i) for i in TServicio_str]
    pprint.pprint(TServicio)

    dispositivos = len(RVisita)

    print("Inserte Z:")
    ZReflexion = int(input())

    # The device response time
    # Ri(N) = Si (1+Qi(N-1))
    print(dispositivos, nmax)
    Respuesta = [[float(0) for i in range(nmax)] for j in range(dispositivos)]

    pprint.pprint(Respuesta)
    # The device queue lengths Qi(n) == Ni(n) with N jobs in the network using Little's law are:
    # Qi(n) = X(n) * Vi * Ri(n)
    Qi = [[float(0) for i in range(nmax)] for j in range(dispositivos)]
    # R(n) = Sum(i=1,K)Vi * Ri(n)
    R = [float(0) for i in range(nmax)]

    # X(n) = n / Z + R(n)

    X = [float(0) for i in range(nmax)]

    # The device queue lengths Ni(n) with N jobs in the network using Little's law are:

    Xi = [[float(0) for i in range(nmax)] for j in range(dispositivos)]
    Ui = [[float(0) for i in range(nmax)] for j in range(dispositivos)]

    for users in range(1, nmax):

        sum = 0
        for i in range(dispositivos):
            print("Escribiendo en respuesta", i, users)
            Respuesta[i][users] = (TServicio[i] * (1 + Qi[i][users - 1]))
            sum += Respuesta[i][users] * RVisita[i]
        R[users] = sum
        pprint.pprint(R[users])

        for i in range(dispositivos):
            X[users] = (users / (ZReflexion + R[users]))
            Qi[i][users] = (X[i] * Respuesta[i][users] * RVisita[i])
            Xi[i][users] = (X[users] * Respuesta[i][users])
            Ui[i][users] = (X[users] * RVisita[i] * TServicio[i])
            print("funciones done", users)

    # convert all lists to dataframes
    df_R = pd.DataFrame(R)
    df_X = pd.DataFrame(X)
    df_Ri = pd.DataFrame(Respuesta)
    df_Qi = pd.DataFrame(Qi)
    df_Xi = pd.DataFrame(Xi)
    df_Ui = pd.DataFrame(Ui)

    # plot the dataframes with the titles

    df_R.plot(title="R(n)")
    plt.show()
    df_X.plot(title="X(n)")
    plt.show()
    df_Ri.plot(title="Ri(n)")
    plt.show()
    df_Qi.plot(title="Qi(n)")
    plt.show()
    df_Xi.plot(title="Xi(n)")
    plt.show()
    df_Ui.plot(title="Ui(n)")
    plt.show()

    print("Respuesta:")
    print("R:", R)
    print("X:", X)
    print("Ri:", Respuesta)
    print("Qi:", Qi)
    print("Xi:", Xi)
    print("Ui:", Ui)


if __name__ == '__main__':
    main()
