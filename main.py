
def determinantCalc(mat):

    if len(mat) == 2: 
        ans =  mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        return ans
            
    minor = [ [0 for i in range(len(mat)-1) ] for j in range(len(mat) - 1)]
    determinant = 0

    for k in range(len(mat)):  
        i, j = 0, 0
        while i < len(mat):
            if i != k:
                minor[j] = mat[i][1:]
                j += 1
            i += 1
        determinant +=  ((-1) ** k) * mat[k][0] * determinantCalc(minor)
    return determinant

def elementaryDelete(mat, tag):

    i, j = tag
    ans = mat(len(mat), 1)
    ans[i][j] = -1 * (mat[i][j] / mat[j][j])
    return ans

def elementarySwitchRows(mat, tag):
    mat[tag[0]], mat[tag[1]] = mat[tag[1]], mat[tag[0]]

def elementaryMulRow(mat, index, scalar):
    mat[index] = [scalar * j for j in mat[index]]

def pivoting(mat, index):

    size = len(math)
    max = mat[coloumn][coloumn]
    maxIndex = index

    for i in range(index + 1, size):
        if mat[i][index] > max:
            maxIndex = i
    mat[index][index], mat[maxIndex][index] = mat[maxIndex][index], mat[index][index]
            
def matrixMul(A, B):
    size = len(A)
    ans = [ [0 for i in range(size)] for j in range(size) ]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                ans[i][j] += A[i][k] * B[k][j]
    return ans



def inverse(mat):

    size = len(mat)
    temp = mat
    ans = [[ int(i == j) for j in range(size)] for i in range(size) ]


    # below diagonal
    for j in range(0, size - 1):
        temp = pivoting(temp)
        for i in range(j + 1, size):
            e = elementaryDelete(temp, [i,j])
            temp = matrixMul(e,temp)
            ans = matrixMul(e,ans)

     # above diagnol
    for j in range(size - 1, 0, -1):
        temp = pivoting(temp)
        for i in range(j - 1, -1, -1):
            e = elementaryDelete(temp, [i,j])
            temp = matrixMul(e,temp)
            ans = matrixMul(e,ans)

     # final step
    for i in range(len(ans)):
        p = temp[i][i]
        for j in range(len(ans)):
            temp[i][j] /= p
            ans[i][j] /= p

        return ans


def solve(mat, b):
    if detCalc(mat) == 0:
        inverse = Inverse(mat)
    else:
        inverse = LU(mat)



A = [[5,2,1,4,6], [9,4,2,5,2], [11,5,7,3,9], [5,6,6,7,2], [7,5,9,3,3]]
B = [[1,2,3], [4,5,6], [7,8,9]]



print(detCalc(A))








