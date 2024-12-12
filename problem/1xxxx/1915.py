import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
for i in range(n):
    inputdata = input().rstrip()
    m_cnt = 0
    for c in inputdata:
        if c == '1':
            data[i][m_cnt] = 1
        else:
            data[i][m_cnt] = 0
        if c == '1' and i != 0 and m_cnt != 0:
            data[i][m_cnt] = min(data[i-1][m_cnt], data[i][m_cnt-1], data[i][m_cnt]) + 1
            answer = max(data[i][m_cnt], answer)
        m_cnt += 1

# for i in range(1, n):
#     for j in range(1, m):
#         if data[i][j] == 1:
#             data[i][j] = min(data[i-1][j-1], data[i-1][j], data[i][j-1]) + 1
#             answer = max(data[i][j], answer)
print(answer * answer)

# 아마 아직 못품