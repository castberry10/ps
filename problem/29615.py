# 첫 번째 줄에 대기 명단에 적힌 수의 개수
# N과 민규 친구의 수 M이 공백으로 구분되어 주어진다.
# 두 번째 줄에 대기 명단에 적힌 N개의 정수가 주어진다.
# 세 번째 줄에 민규 친구의 대기 번호를 나타내는 m개의 정수가 주어진다.
# 5 2              ->       2
# 1 2 3 4 5
# 3 4

n, m = map(int, input().split())
ndata = list(map(int, input().split()))
mdata = set(map(int, input().split()))
ndata_r = reversed(ndata)
cnt = 0
answer = 0
for i in range(n):
    if cnt >= m:
        break
    if ndata[i] in mdata:
        cnt += 1
    else:
        for j in range(n-1, 0, -1):
            # print('j:', j)
            if ndata[j] in mdata:
                ndata[i], ndata[j] = ndata[j], ndata[i]
                answer += 1
                # print(answer, ndata[i], ndata[j], i, j)
                cnt += 1
                break
print(answer)
