import numpy as np

def ldt_decomposition(A):
    """
    Realiza la descomposición LDL^T de una matriz simétrica positiva definida A.

    :param A: Matriz simétrica positiva definida que se va a descomponer.
    :return: Matrices L y D.
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    D = np.zeros((n, n))

    for j in range(n):
        D[j, j] = A[j, j] - np.dot(L[j, :j], D[:j, :j] @ L[j, :j])
        L[j, j] = 1  # La diagonal de L es 1

        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - np.dot(L[i, :j], D[:j, :j] @ L[j, :j])) / D[j, j]

    return L, D
