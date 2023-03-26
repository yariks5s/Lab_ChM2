from gaussian_method import gaussian_elimination
from jacobi_iteration_method import jacobi, jacobi_method
import numpy as np

def repr_vector(v, time):
    print(" ".join(map(str, v)))
    print("Time: " + str(time))

# A = np.array([[10.0, 1.0, -1.0],
#               [1.0, 10.0, -1.0],
#               [1.0, 1.0, 5.0]])
#
# b = np.array([11.0, 10.0, 7.0])

def inputs():
    print("Please, write your matrix:")
    A = np.zeros((3, 3), dtype=float)
    b = np.zeros(3, dtype=float)
    # take user input for each element in the matrix
    for i in range(3):
        for j in range(3):
            element = float(input(f"Enter element ({i + 1},{j + 1}): "))
            A[i][j] = element  # set the element in the matrix
        b[i] = float(input(f"Enter element ({i + 1}) for the right side: "))
    return A, b

A, b = inputs()

det_A = np.linalg.det(A)
print("\nВизначник матриці A:")
print(det_A)

cond_A = np.linalg.cond(A)
print("\nЧисло обумовленості матриці A:")
print(cond_A)

print("\nGaussian elimination:")
x, time2 = gaussian_elimination(A, b)
repr_vector(x, time2)

print("Jacobi method:")
y, time0 = jacobi(A, b)
repr_vector(y, time0)
