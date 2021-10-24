import numpy as np
def lu(A):
    # Get the number of rows
    n = A.shape[0]

    U = A.copy()
    L = np.eye(n, dtype=np.double)

    # Loop over rows
    for i in range(n):
        # Eliminate entries below i with row operations
        # on U and reverse the row operations to
        # manipulate L
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]

    return L, U
