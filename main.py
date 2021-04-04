

def detCalc(mat):

    if len(mat) == 2: 
        ans =  mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        return ans
            
    minor = [ [0 for i in range(len(mat)-1) ] for j in range(len(mat) - 1)]
    det = 0

    for k in range(len(mat)):  
        i, j = 0, 0
        while i < len(mat):
            if i != k:
                minor[j] = mat[i][1:]
                j += 1
            i += 1
        det +=  ((-1) ** k) * mat[k][0] * detCalc(minor)
    return det


def elementary(mat, tag):

    i, j = tag
    ans = mat(len(mat), 1)
    ans[i][j] = -1 * (mat[i][j] / mat[j][j])
    return ans


def inverse(mat):

    if detCalc(mat) == 0:
        print("No inverse!")
        return None

    temp = mat# Copy of self matrix
    ans = (len(self), 1)  # unit matrix

    # below diagonal
    for j in range(0, self.size - 1):
        for i in range(j + 1, self.size):
            e = temp.elementary([i, j])
            temp = e * temp
            ans = e * ans

     # above diagnol
    for j in range(self.size - 1, 0, -1):
        for i in range(j - 1, -1, -1):
            e = temp.elementary([i, j])
            temp = e * temp
            ans = e * ans

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








