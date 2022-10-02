
N, M = map(int, input().split())
datamap = [list(map(int, input().split())) for _ in range(N)]
dpmap = [[-1 for _ in range(M)] for _ in range(N)]
dxy = [(-1, 0), (1, 0), (0, -1), (0 , 1)]

def dp(y, x):
    if dpmap[y][x] != -1: #이미 데이터가 있다면  > ? 
        # pass
        return dpmap[y][x]
    if y == N - 1 and x == M - 1: #오른쪽 끝 설정
        # dpmap[y][x] = 1 
        return 1
    dpmap[y][x] = 0
    for i in range(4):
        dx, dy = dxy[i]
        dxx = dx + x
        dyy = dy + y
        if 0 <= dxx < M and 0 <= dyy < N: #인덱스 에러로부터 안전
            # print(1)
            if datamap[y][x] > datamap[dyy][dxx]:
                # print(0)
                dpmap[y][x] += dp(dyy, dxx)
    return dpmap[y][x]
answer = dp(0, 0 )
# print(dpmap)
# print(dpmap[0][0]) #왼쪽 끝
print(answer)