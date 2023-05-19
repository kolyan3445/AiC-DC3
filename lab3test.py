#Формируется матрица F следующим образом: если в В количество чисел, меньших К в нечетных столбцах в области 3 больше,
# чем сумма чисел в четных строках в области 2, то поменять в Е симметрично области 3 и 2 местами,
# иначе В и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F– K*AT .
# Выводятся по мере формирования А, F и все матричные операции последовательно.

# B C    2
# E D  1   3
#        4

import random


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()


def swap_symmetric(matrix, area1, area2):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[area1 + i][area1 + j], matrix[area2 + i][area2 + j] = matrix[area2 + i][area2 + j], matrix[area1 + i][area1 + j]


def swap_asymmetric(matrix1, matrix2):
    matrix1[:], matrix2[:] = matrix2[:], matrix1[:]


try:
    K = int(input("Введите множитель К: "))
    n = int(input("Введите N, больше 5 для создания квадратной матрицы: "))

    while n < 5:
        n = int(input("Число меньше 5. Введите число больше 5 "))

    del_n = n // 2
    fixik = del_n
    if n % 2 != 0:
        fixik += 1

    matrix_A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
    print("\nМатрица A:")
    print_matrix(matrix_A)

    matrix_F = [row.copy() for row in matrix_A]
    print("\nМатрица F:")
    print_matrix(matrix_F)

    matrix_C = [row[fixik:] for row in matrix_F[:del_n]]
    print('\nПодматрица C:')
    print_matrix(matrix_C)

    matrix_B = [row[:del_n] for row in matrix_F[:del_n]]
    matrix_D = [row[:del_n] for row in matrix_F[del_n:]]
    matrix_E = [row[fixik:] for row in matrix_F[fixik:]]

    sum_area2 = sum(matrix_C[0][1:del_n-1])
    sum_area3 = sum(matrix_C[del_n-1][1:del_n-1])

    if sum_area3 > sum_area2:
        print("В В количество чисел, меньших К в нечетных столбцах в области 3 больше.")
        print("Симметрично меняем местами область 3 и 2 в Е.")
        swap_symmetric(matrix_E, 1, 1)
        print('\n Модифицированная подматрица E:')
        print_matrix(matrix_E)
    else:
        print("Сумма чисел в области 3 меньше или равна сумме чисел в области 2.")
        print("Меняем подматрицы В и Е асимметрично.")
        swap_asymmetric(matrix_B, matrix_E)

    matrix_F = matrix_A.copy()
    for i in range(del_n):
        for j in range(del_n):
            matrix_F[i][j] = matrix_B[i][j]
    for i in range(fixik, n):
        for j in range(fixik, n):
            matrix_F[i][j] = matrix_E[i - fixik][j - fixik]

    print('\nИзменённая матрица F:')
    print_matrix(matrix_F)

    matrix_AF = [[sum(K * matrix_A[i][k] * matrix_F[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    print('\nРезультат (K*A)*F:')
    print_matrix(matrix_AF)

    matrix_A_transp = [[matrix_A[j][i] for i in range(n)] for j in range(n)]

    matrix_KAT = [[K * matrix_A_transp[i][j] for j in range(n)] for i in range(n)]
    print('\nРезультат K*A^T:')
    print_matrix(matrix_KAT)

    matrix_res = [[matrix_AF[i][j] - matrix_KAT[i][j] for j in range(n)] for i in range(n)]
    print("\nРезультат (K*A)*F - K*A^T:")
    print_matrix(matrix_res)

except ValueError:
    print("Вводимое значение не является числом. Пожалуйста, введите число.")
