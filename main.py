
import numpy as np

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


A = [[5,2,1,4,6], [9,4,2,5,2], [11,5,7,3,9], [5,6,6,7,2], [7,5,9,3,3]]
B = [[1,2,3], [4,5,6], [7,8,9]]

x = np.array(A)


print(detCalc(A))
print(int(np.ling.det(x)))







