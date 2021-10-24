import numpy as np

n, m = map(int, input().split())

extended_maxtix = []
for _ in range(n):
    extended_maxtix.append(list(map(int, input().split())))
extended_maxtix = np.array(extended_maxtix, dtype=np.float64).reshape((n, m + 1))

matrix_rank = np.linalg.matrix_rank(extended_maxtix[:, :m])
extended_maxtix_rank = np.linalg.matrix_rank(extended_maxtix)

if matrix_rank != extended_maxtix_rank:
    print("NO")
elif matrix_rank == extended_maxtix_rank and matrix_rank < m:
    print("INF")
elif matrix_rank == extended_maxtix_rank and matrix_rank == m:
    print("YES")
    for j in range(m - 1):
        extended_maxtix[j] = extended_maxtix[j] / extended_maxtix[j, j]
        for i in range(j + 1, n):
            extended_maxtix[i] = extended_maxtix[i] - extended_maxtix[j] * extended_maxtix[i, j]

    answers_array = np.zeros(m)
    for j in range(1, m + 1):
        current_right_value = extended_maxtix[n - j, m]
        for i in range(1, j):
            current_right_value -= extended_maxtix[n - j, m - i] * answers_array[m - i]
        answers_array[m - j] = current_right_value / extended_maxtix[n - j, m - j]
    print(*answers_array)
