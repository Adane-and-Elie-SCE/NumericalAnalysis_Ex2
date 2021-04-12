#Adane Adgo 315721969
#Elie Bracha 204795900

# github: https://github.com/Adane-and-Elie-SCE/NumericalAnalysis_Ex2.git

def determinant_calc(mat):
    if len(mat) == 2:
        ans = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        return ans

    minor = [[0 for i in range(len(mat) - 1)] for j in range(len(mat) - 1)]
    determinant = 0

    for k in range(len(mat)):
        i, j = 0, 0
        while i < len(mat):
            if i != k:
                minor[j] = mat[i][1:]
                j += 1
            i += 1
        determinant += ((-1) ** k) * mat[k][0] * determinant_calc(minor)
    return determinant


def elementary_delete(mat, tag):
    i, j = tag
    ans = [[int(i == j) for j in range(len(mat))] for i in range(len(mat))]
    ans[i][j] = -1 * (mat[i][j] / mat[j][j])
    return ans


def elementary_switch_rows(mat, tag):
    ans = [[int(i == j) for j in range(len(mat))] for i in range(len(mat))]
    ans[tag[0]], ans[tag[1]] = ans[tag[1]], ans[tag[0]]
    return ans


def elementary_mul_row(mat, index, scalar):
    e = [[int(i == j) for j in range(len(mat))] for i in range(len(mat))]
    mat[index][index] = scalar
    return mat


def matrix_pivoting(mat, index):
    size = len(mat)
    max_value = mat[index][index]
    max_index = index

    for i in range(index + 1, size):
        if mat[i][index] > max_value:
            max_value = mat[i][index]
            max_index = i

    return matrix_mul(elementary_switch_rows(mat, [index, max_index]), mat)


def fix_approximation(mat):
    epsilon = 2 ** (-26)
    for i in range(len(mat)):
        for j in range(len(mat)):
            if abs(mat[i][j]) < epsilon:
                mat[i][j] = 0
    return mat


def matrix_mul(a, b):
    size = len(a)
    ans = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                ans[i][j] += a[i][k] * b[k][j]
    return fix_approximation(ans)


def matrix_vector_mul(mat, b):
    size = len(mat)
    ans = [0 for i in range(size)]

    for i in range(size):
        for j in range(size):
            ans[i] += mat[i][j] * b[j]
    return ans


def print_matrix(mat):
    for row in mat:
        print(row)
    print()


def print_vector(v):
    size = len(v)
    for i in range(size):
        print('[' + str(v[i]) + ']')


def inverse_by_gauss(mat):
    if not determinant_calc(mat):
        print('no inverse')

    size = len(mat)
    temp = mat
    ans = [[int(i == j) for j in range(size)] for i in range(size)]

    # below diagonal
    for j in range(0, size - 1):

        for i in range(j + 1, size):
            e = elementary_delete(temp, [i, j])
            temp = matrix_mul(e, temp)
            ans = matrix_mul(e, ans)

    # above diagonal
    for j in range(size - 1, -1, -1):

        for i in range(j - 1, -1, -1):
            e = elementary_delete(temp, [i, j])
            temp = matrix_mul(e, temp)
            ans = matrix_mul(e, ans)

    # final step
    for i in range(size):
        for j in range(size):
            ans[i][j] /= temp[i][i]

    return ans


def lu_decomposition(mat):
    size = len(mat)
    u = mat
    l = [[int(i == j) for j in range(size)] for i in range(size)]

    # below diagonal
    for j in range(0, size):
        for i in range(j + 1, size):
            e = elementary_delete(u, [i, j])
            u = matrix_mul(e, u)
            e[i][j] = -1 * e[i][j]
            l = matrix_mul(l, e)

    print("Triangle Matrix L:")
    print_matrix(l)
    print("Triangle Matrix U:")
    print_matrix(u)


def driver(mat, v = None):
    if len(mat) < 4:
        print('Example 1 Gauss Elimination: \n')
        print("Matrix A:")
        print_matrix(mat)
        print("Vector b:")
        print_vector(v)
        print()
        print("X = A^(-1) * b:")
        print_vector(matrix_vector_mul(inverse_by_gauss(mat), b))
    elif len(mat) >= 4:
        print('\nExample 2 LU decomposition: \n')
        print("Matrix C:")
        print_matrix(mat)
        lu_decomposition(mat)


A = [[-1.41, 2, 0], [0, 2, -1.41], [1, -1.41, 1]]
b = [1, 1, 1]
C = [[3, -7, -2, 2], [-3, 5, 1, 0], [6, -4, 0, -5], [-9, 5, -5, 12]]

driver(A, b)
driver(C)
