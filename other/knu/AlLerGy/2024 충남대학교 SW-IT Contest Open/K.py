T = int(input())
def solve():
    n = int(input())
    data = list(map(int ,input().split()))
    index = 0
    while True:
        if n == 1:
            if data[0] > 1:
                print('NO')
                return
            else:
                print('YES')
                return
                
        if index == n - 1:
            if data == 0:
                print("YES")
                return
            else:
                print("NO")
                return
        if data[index] <= data[index + 1]:
            data[index+1] -= data[index]
            data[index] = 0
            index += 1
        else:
            data[index] -= data[index + 1] + 1
            data[index + 1] = 0
            if index == n - 2 and sum(data) == 0:
                print("YES")
                return
            else:
                print("NO")
                return
for i in range(T):
    solve()