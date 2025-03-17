# 정보과학관 전산관 미래관 
# 신앙관 진리관 한경직기념관 
# 학생회관 형남공학관
# 0, 1, 2 ,
# 3 , 4, 5, 
# 6, 7

MOD = 1000000007
graph = [[0 for i in range(8)]for j in range(8)]

graph[0][1] = graph[0][2] = 1
graph[1][0] = graph[1][2] = graph[1][3] = 1
graph[2][0] = graph[2][1] = graph[2][3] = graph[2][5] = 1
graph[3][1] = graph[3][2] = graph[3][4] = graph[3][5] = 1
graph[4][3] = graph[4][5] = graph[4][6] = 1
graph[5][2] = graph[5][3] = graph[5][4] = graph[5][7] = 1
graph[6][4] = graph[6][7] = 1
graph[7][5] = graph[7][6] = 1


n = int(input())

def matrix_multiplication(A, B):
    data = [[0 for i in range(8)]for j in range(8)]
    for row in range(8):
        for col in range(8):
            for i in range(8):
                data[row][col] += A[row][i] * B[i][col]
            data[row][col] = data[row][col] % MOD
    return data

def divide_conquer(A, n):
    if n == 1:
        return A
    temp = divide_conquer(A, n // 2)
    temp = matrix_multiplication(temp, temp)
    if n % 2 == 1:
        return matrix_multiplication(temp, A)
    else:
        return temp

answer = divide_conquer(graph, n)
print(answer[0][0])