import time
import operator
import pandas as pd
import numpy as np
import math


def jacobi(A, B, epsilon=1e-10, max_iter=1000):
    start = time.time()
    n = A.shape[0]
    X = np.zeros(n)

    for i in range(B.shape[0]):
        sum = 0
        for j in range(B.shape[0]):
            if i != j:
                sum += abs(A[i][j])
        if abs(A[i][i]) <= sum:
            print("Method failed")
            raise Exception("Method failed")
    for k in range(max_iter):
        X_prev = np.copy(X)
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i][j] * X_prev[j]
            X[i] = (B[i] - s) / A[i][i]
            if k == 0 and i == 0:
                cubic_norm(X - X_prev)
            repr_vector(X)

        if np.linalg.norm(X - X_prev, ord=3) < epsilon:
            cubic_norm(X - X_prev)
            end = time.time()
            return X, end - start
    end = time.time()
    return X, end - start



def jacobi_method(A, B, epsilon=1e-10, max_iter=1000):
    start = time.time()
    x1 = 0
    x2 = 0
    x3 = 0
    for i in range(B.shape[0]):
        if not condition(B, i):
            print("Method failed")
            return
    for i in range(max_iter):
        x1_new = (1 / A[0][0]) * (B[0] - A[0][1] * x2 - A[0][2] * x3)
        x2_new = (1 / A[1][1]) * (B[1] - A[1][0] * x1 - A[1][2] * x3)
        x3_new = (1 / A[2][2]) * (B[2] - A[2][0] * x1 - A[2][1] * x2)
        if np.linalg.norm(x1_new - x1) < epsilon or np.linalg.norm(x2_new - x2) < epsilon or np.linalg.norm(
                x3_new - x3) < epsilon:
            end = time.time()
            return [x1_new, x2_new, x3_new], end - start
        x1 = x1_new
        x2 = x2_new
        x3 = x3_new

    end = time.time()
    return [x1, x2, x3], end - start


def repr_matrix(A, b):
    for row in A:
        count = 0
        print("(", end="")
        for entry in row:
            entry = round(entry, 2)
            print(entry, end=" ")
        print(")", end="")
        print(f"({b[count]})\n", end="")
        count += 1
    print("\n")


def repr_vector(v):
    for entry in v:
        print(f'x{np.where(v == entry)[0][0] + 1}: ', end="")
        print(entry, end=" ")
    print("\n")

def stop_condition(a0, a1, epsiilon):
    if np.linalg.norm(a1 - a0) < epsiilon:
        return True
    else:
        return False

def cubic_norm(v):
    for item in v:
        item = abs(item)
    norm = max(v)
    print(f"Cubic norm: {norm}")
    return norm
