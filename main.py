"""
Mediante este script se implementará el algoritmo de colas cerradas y se representará
el resultado en una gráfica.
"""


def test():
    N = 10 + 1
    Z = 8
    Vi = [1, 1, 1]
    Si = [0, 0, 0]
    Num_disp = len(Vi)
    MVA(N, Z, Num_disp, Vi, Si)


def MVA(N, Z, Num_disp, Vi, Si):
    """
    Función encargada de calcular los resultados
    :param N: Número de trabajos
    :param Z: Tiempo de reflexión
    :param Num_disp: Cantidad de dispositivos
    :param Vi: Razones de Visita
    :param Si: Tiempos de servicio
    """
    Ni = []
    Ri = []
    Xi = []
    X0 = 0.0
    _list_X0 = []
    _list_R = []

    # Se imprime la cabecera de la tabla
    print_cabecera(Num_disp)

    for i in range(Num_disp):
        Ni.append(0.0)
        Ri.append(0.0)
        Xi.append(0.0)

    n = 0
    for n in range(N):
        for i in range(Num_disp):
            Ri[i] = Si[i] * (1 + Ni[i])
        R = sum([a * b for a, b in zip(Ri, Vi)])
        _list_R.append(R)

        X0 = (n / (R + Z))
        _list_X0.append(X0)

        Ui = [((a * b) * X0) for a, b in zip(Si, Vi)]

        for i in range(Num_disp):
            Ni[i] = X0 * Vi[i] * Ri[i]
            Xi[i] = X0 * Vi[i]
        if n > 0:
            print_filaTabla(X0, Xi, Ni, Ri, Ui, R, n, Num_disp)


def print_cabecera(Num_disp):
    print("Trabajos\t",

          "X\t", end="")
    for i in range(Num_disp):
        print(
            "X_", i + 1, "\t", end="")
    for i in range(Num_disp):
        print(
            "N_", i + 1, "\t", end="")
    for i in range(Num_disp):
        print(
            "R_", i + 1, "\t", end="")
    for i in range(Num_disp):
        print(
            "U_", i + 1, "\t", end="")
    print(
        "R\t")


def print_filaTabla(X0, Xi, Ni, Ri, Ui, R, n, Num_disp):
    print(n, "\t", round(X0, 3), "\t", end="")
    for i in range(Num_disp):
        print(round(Xi[i], 3), "\t", end="")

    for i in range(Num_disp):
        print(round(Ni[i], 3), "\t", end="")

    for i in range(Num_disp):
        print(round(Ri[i], 3), "\t", end="")

    for i in range(Num_disp):
        print(round(Ui[i], 3), "\t", end="")
    print(round(R, 3))


if __name__ == '__main__':
    test()
