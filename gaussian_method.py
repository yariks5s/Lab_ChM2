import math
import time

import numpy as np

def gaussian_elimination(A, b):
    time_start = time.time()
    n = len(A)  # Розмірність матриці A
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)  # Об'єднуємо матрицю A та вектор b в матрицю Ab
    P = np.eye(3)
    repr_matrixe(A, b)
    for i in range(n-1):  # Проходимо по всіх стовпцях матриці A (крім останнього)
        # Знаходимо максимальний елемент за модулем у стовпці i
        max_row = i
        for j in range(i+1, n):
            if abs(Ab[j, i]) > abs(Ab[max_row, i]):
                max_row = j
                print("P matrix:")
                P[[i, max_row]] = P[[max_row, i]]
                print(f"We need to change rows from {i+1} to {max_row+1}")
                repr_matrix(P)

        # Міняємо місцями рядки i та max_row
        Ab[[i, max_row]] = Ab[[max_row, i]]

        Ab1 = A
        # Елімінуємо невідомі
        for j in range(i+1, n):
            M = Ab[j, i] / Ab[i, i]  # Знаходимо множник

            Ab[j, i:] -= M * Ab[i, i:]  # Віднімаємо множиником помножені елементи рядка i з рядком j

        temp = Ab[:3, :3]
        mat = np.linalg.solve(Ab1, temp)
        repr_matrix(mat)
        repr_matrix(Ab)
    # Обчислюємо розв'язки системи рівнянь методом зворотного ходу
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, n] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    time_end = time.time()
    return x, time_start - time_end


def repr_matrixe(A, b):
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

def repr_matrix(A):
    count = 0
    for row in A:
        print("(", end="")
        for entry in row:
            entry = round(entry, 2)
            print(entry, end=" ")
        print(")\n", end="")
    print("\n")
