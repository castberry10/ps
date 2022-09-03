import sys
# testMap = [[1],[1]]
# for i in range(len(testMap)):           
#     for j in range(len(testMap[i])):     
#         print(testMap[i][j], end=' ')
#     print()
    
# ls = [[1,1,1,2],[3,3,3,4]]

# print(ls[0][1])
n = input()
n, m = map(int, input().split())
map1 = [list(map(int, input().split())) for _ in range(n)]
a = int(sys.stdin.readline())
print(map1)

visitMap = [[0 for _ in range(10)] for _ in range(10)]