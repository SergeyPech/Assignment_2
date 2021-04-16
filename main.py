#name:sergey pechyoni
#ID:320734304
#

import math


def printMat(mat):
    size = int(math.sqrt(len(mat)))
    for i in range(0, size):
        for j in range (0, size):
            print(mat[i*size+j], end=" ")
        print(" ")


def oMatrix(size):#creating unit matrix
    arr=[0]*size*size
    for i in range (0,size):
        arr[i+i*size]=1
    #printMat(arr)
    return arr

def matrixMul(mat1, mat2):#matrix multiplication
    size = int(math.sqrt(len(mat1)))
    arr = [0] * size * size
    for i in range(0, size):
        for j in range(0, size):
            for k in range(0, size):
                arr[(j*size)+i] = arr[(j*size)+i] + mat1[(j*size)+k] * mat2[(k*size)+i]
    return arr

def matrixSol(mat,vec):#linear equestions matrix solution
    size = int(math.sqrt(len(mat)))
    for i in range(0, size):#upper ranking the matrix:
        pivot = mat[i + (size * i)]
        for j in range(i + 1, size):
            temp = oMatrix(size)
            temp[j * size + i] = mat[j * size + i] / pivot * -1
            vec = matrixMul(temp, vec)
            mat = matrixMul(temp, mat)
    #print(mat[size*size-1])
    #print(vec[size*size-size])
    for i in range(size-1,-1,-1):#solving the equations:
        for j in range (size-1,i,-1):
            vec[size*i] = vec[size*i]-mat[size*i+j]*vec[size*j]
            mat[size * i + j] = 0
        vec[size*i]=vec[size*i]/mat[size*i+i]
    printMat(vec)



def matrixLU(mat):
    size = int(math.sqrt(len(mat)))
    L=oMatrix(size)
    for i in range (0,size):
        pivot=mat[i+(size*i)]
        for j in range (i+1,size):
            temp = oMatrix(size)
            temp[j*size+i] = mat[j*size+i]/pivot*-1
            mat=matrixMul(temp,mat)
            L = matrixMul(L, temp)
            L[j*size+i]=L[j*size+i]*-1
    print("LU Decomposition:")
    print("L matrix:")
    printMat(L)
    print("U matrix:")
    printMat(mat)
    #printMat(matrixMul(L,mat))


if __name__ == '__main__':
    vec =[3,0,0,2,0,0,4,0,0]
    mat=[2,3,2,1,4,2,1,2,3,3,3,3,2,1,1,2]
    sizeOfMat = int(math.sqrt(len(mat)))
    if sizeOfMat>3:
        matrixLU(mat)
    else:
        matrixSol(mat,vec)
