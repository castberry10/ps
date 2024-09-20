import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007
facMatrix = [[1, 1],[1, 0]]
def matrix22_multiplication(A, B):
    data = [[0,0], [0,0]]
    for row in range(2):
        for col in range(2):
            temp = 0 
            for i in range(2):
                temp += A[row][i] * B[i][col]
            data[row][col] = temp % p 
    return data

def divide_conquer(A,n):
    if n==1:
        return A
    elif n % 2:
        return matrix22_multiplication(divide_conquer(A,n-1),A)
    else:
        return divide_conquer(matrix22_multiplication(A , A ), n//2)

answerMatrix = divide_conquer(facMatrix, n)
print(answerMatrix[0][1])