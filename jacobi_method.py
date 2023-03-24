import numpy as np


def jacobi_rotation(A):
    # Отримання розміру матриці
    n = A.shape[0]

    # Ініціалізація матриць Q та R
    Q = np.eye(n)
    R = np.copy(A)

    # Ітерації методу обертань Якобі
    for i in range(n):
        for j in range(i+1, n):
            # Обчислення параметрів c та s
            a = R[i,i]
            b = R[j,i]
            c = a / np.sqrt(a**2 + b**2)
            s = -b / np.sqrt(a**2 + b**2)

            # Матриця обертання
            J = np.eye(n)
            J[i,i] = c
            J[j,j] = c
            J[i,j] = s
            J[j,i] = -s

            # Оновлення матриць Q та R
            R = np.dot(J, R)
            Q = np.dot(Q, J.T)
    return Q, R

def jacobi_method(A, b, tol=1e-10, max_iter=1000):
    """
    Розв'язує систему лінійних алгебраїчних рівнянь Ax = b методом обертань Якобі.

    Параметри:
    A (ndarray): Симетрична матриця розмірності (n, n)
    b (ndarray): Вектор вільних членів розмірності (n,)
    tol (float): Точність, до якої потрібно розв'язати систему
    max_iter (int): Максимальна кількість ітерацій

    Повертає:
    x (ndarray): Розв'язок системи розмірності (n,)
    """

    n = len(b)
    x = np.zeros(n)

    for i in range(max_iter):
        # Знаходимо матрицю обертань
        Q, R = jacobi_rotation(A)

        # Обчислюємо нову матрицю A
        A = np.dot(R, Q)

        # Обчислюємо новий вектор b
        b = np.dot(Q.T, b)

        # Обчислюємо новий вектор x
        x_new = np.zeros(n)
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i][j] * x[j]
            x_new[i] = s / A[i][i]
            print(x_new)
        # Перевірка збіжності
        if np.allclose(x, x_new, atol=tol):
            return

        x = x_new

    # Повертаємо останній знайдений розв'язок
    print(x)

