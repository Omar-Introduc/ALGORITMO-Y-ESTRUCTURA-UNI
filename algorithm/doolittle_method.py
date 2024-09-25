import numpy as np


def doolittle_method(A):
    """
    Factoriza la matriz A en el producto de matrices L y U usando el método de Doolittle.

    :param A: Matriz cuadrada que se va a factorizar.
    :return: Matrices L y U.
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Calcular la matriz U
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        
        # Calcular la matriz L
        for j in range(i, n):
            if U[i, i] == 0:
                raise ValueError("La matriz es singular y no se puede factorizar.")
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    # La diagonal de L se llena con 1s
    np.fill_diagonal(L, 1)

    return L, U