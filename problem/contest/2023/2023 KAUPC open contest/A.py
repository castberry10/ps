import sys
input = sys.stdin.readline
N = int(input())
ans = 0
for i in range(N):
    data = list(map(int, input().split()))
    data1 = data[:2]
    data2 = data[2:]
    data2.sort(key = lambda x : -x)
    # print(data1)
    # print(data2)
    
    ans = max(ans, max(data1) + data2[0] + data2[1])
print(ans)