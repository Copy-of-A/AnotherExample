import random
from math import sqrt

while True:
    try:
        n = int(input("Input the size of a matrix: "))
    except ValueError:
        print("Invalid input. Try one more time.")
        continue
    else:
        print("Correct input.")
        break

matrix = [[round(random.random() * (1 + 1) - 1, 4) for x in range(n)] for y in range(n)]


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print("%.4f" % m[i][j], end='   ')
        print()


S = 0
print_matrix(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        S += matrix[i][j]
S /= pow(n, 2)
print("Middle value: %.4f" % S)

D = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        D += pow(matrix[i][j] - S, 2)
D /= (pow(n, 2) - 1)
print("Dispersion: %.4f" % D)
st_deviation = sqrt(D)
print("Standart deviation: %.4f" % st_deviation)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if abs(matrix[i][j]) > st_deviation:
            matrix[i][j] = S

print_matrix(matrix)