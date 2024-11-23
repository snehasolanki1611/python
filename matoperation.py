def createMat(x, y, mname):
    for i in range(0, x):
        mname.append([])
    for i in range(0, x):
        for j in range(0, y):
            mname[i].append(0)
    return mname


def initializeOfMat(x, y, mat):
    for i in range(x):
        for j in range(y):
            print("Enter for matrix value in row", i + 1, "and col", j + 1)
            mat[i][j] = int(input())
    return mat


def display(x, y, mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end=" ")
        print()


def additionOfMat(x, y, mat1, mat2):
    result = []
    result = createMat(x, y, result)
    for i in range(x):
        for j in range(y):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result


def maltiplicatrionOfMat(x, y, mat1, mat2):
    result = []
    result = createMat(x, y, result)
    for i in range(x):
        for j in range(y):
            for k in range(x):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
