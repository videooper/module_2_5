# Домашняя работа по уроку "Функции в Python.Функция с параметром"
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_new = []
        matrix_new.append(value)
        for j in range (m-1):
            matrix_new.append(value)
        matrix.append(matrix_new)
    return matrix

result1 = get_matrix(2, 2, 10)

result2 = get_matrix(3, 5, 42)

result3 = get_matrix(4, 2, 13)


print(result1)

print(result2)

print(result3)




