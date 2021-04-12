def determinant_calc(mat):

    if len(mat) == 2: 
        ans = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        return ans
            
    minor = [[0 for i in range(len(mat)-1)] for j in range(len(mat) - 1)]
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
    e = [[int(i == j) for j in range(len(mat))] for i in range(len(mat))]
    e[tag[0]], e[tag[1]] = e[tag[1]], e[tag[0]]
    return e


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
    epsilon = 2 ** (-30)
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
    return ans


def matrix_vector_mul(mat, b):
    size = len(mat)
    ans = [0 for i in range(size)]

    for i in range(size):
        for j in range(size):
            ans[i] += mat[i][j]*b[j]
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

    size = len(mat)
    temp = mat
    ans = [[int(i == j) for j in range(size)] for i in range(size) ]

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

def inverse_by_lu(mat):



b = [1, 1, 1]
A = [[-1.41, 2, 0], [1, -1.41, 1], [0, 2, -1.41]]











