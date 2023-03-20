import numpy as np
import math
import time

def gaussian_elimination(A, b):
    A1 = A
    start = time.time()
    n = len(A1)
    # Forward elimination
    for i in range(n-1):
        # Find the row with the largest pivot element
        repr_matrix(A1, b)
        max_row = i
        for j in range(i+1, n):
            if abs(A1[j][i]) > abs(A1[max_row][i]):
                max_row = j
        if i != max_row:
            print(f"We changed main row to {max_row+1}")
        # Swap the current row with the row with the largest pivot element
        A1[[i, max_row]] = A1[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]
        # Perform elimination on the current column
        for j in range(i+1, n):
            factor = A1[j][i] / A1[i][i]
            A1[j, i + 1:] -= factor * A1[i, i + 1:]
            A1[j, i] = 0
            b[j] -= factor * b[i]
            repr_matrix(A1, b)

    # Back substitution
    x = np.zeros(n)
    x[n-1] = b[n-1] / A1[n - 1, n - 1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A1[i, i + 1:], x[i + 1:])) / A1[i, i]
    end = time.time()
    return x, end - start

def repr_matrix(A, b):
    count = 0
    for row in A:
        print("(", end="")
        for entry in row:
            entry = round(entry, 2)
            print(entry, end=" ")
        print(")", end="")
        print(f"({b[count]})\n", end="")
        count += 1
    print("\n")
