import numpy as np

def cholesky_decomposition(A):
    """
    Realiza la descomposición de Cholesky de una matriz simétrica positiva definida A.

    :param A: Matriz simétrica positiva definida que se va a descomponer.
    :return: Matriz L tal que A = L * L^T.
    """
    n = A.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            if i == j:  # Elementos de la diagonal
                L[i, j] = np.sqrt(A[i, i] - np.dot(L[i, :j], L[i, :j]))
            else:
                L[i, j] = (A[i, j] - np.dot(L[i, :j], L[j, :j])) / L[j, j]

    return L