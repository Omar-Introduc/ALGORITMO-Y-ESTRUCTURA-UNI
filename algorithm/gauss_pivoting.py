import numpy as np

def gauss_elimination_with_pivoting(A, b):
    """
    Resuelve el sistema de ecuaciones Ax = b usando el método de eliminación de Gauss con pivoteo parcial.

    :param A: Matriz de coeficientes.
    :param b: Vector de términos independientes.
    :return: Solución x del sistema Ax = b.
    """
    n = len(b)
    
    # Combinar A y b para trabajar con una sola matriz
    Ab = np.hstack([A, b.reshape(-1, 1)])

    # Eliminación de Gauss con pivoteo
    for i in range(n):
        # Pivoteo parcial
        max_index = np.argmax(np.abs(Ab[i:n, i])) + i
        if Ab[max_index, i] == 0:
            raise ValueError("El sistema no tiene solución única.")
        
        # Intercambiar filas
        Ab[[i, max_index]] = Ab[[max_index, i]]

        # Eliminación
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]

    return x