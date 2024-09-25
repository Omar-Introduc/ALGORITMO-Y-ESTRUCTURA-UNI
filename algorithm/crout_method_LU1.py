import numpy as np

def crout_method_LU1(A):
    """
    Factoriza la matriz A en el producto de matrices L y U usando el método de Crout.

    :param A: Matriz cuadrada que se va a factorizar.
    :return: Matrices L y U.
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.eye(n)  # U inicializada como la matriz identidad

    for j in range(n):
        for i in range(j, n):
            L[i, j] = A[i, j] - np.dot(L[i, :j], U[:j, j])

        for i in range(j + 1, n):
            U[j, i] = (A[j, i] - np.dot(L[j, :j], U[:j, i])) / L[j, j]

    return L, U
