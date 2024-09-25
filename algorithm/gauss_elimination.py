def gauss_elimination(A, b):
    """
    Realiza la eliminación de Gauss para resolver el sistema de ecuaciones Ax = b.

    :param A: Matriz de coeficientes.
    :param b: Vector de términos independientes.
    :return: Solución del sistema de ecuaciones.
    """
    n = len(b)
    
    # Convertir A y b a matrices numpy para facilitar operaciones
    import numpy as np
    A = np.array(A, float)
    b = np.array(b, float)

    # Aplicar eliminación de Gauss
    for i in range(n):
        # Pivotear: encontrar el máximo en la columna i
        max_row = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Hacer ceros debajo de la fila actual
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

    return x