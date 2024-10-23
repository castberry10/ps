# 5 30 2 5
# 1 2 3 4 5
# -1
n, k, a, b = map(int, input().split())
data = list(map(int, input().split()))
for i in range(n):
    data[i] = data[i] * a + b
# print(data)
data.sort()
def aaaa(n, k): 
    start = 0
    end = n - 1
    answer = -1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == k:
            return k
        elif data[mid] < k:
            start = mid + 1
        else: # 정답이 가능한 경우
            if answer > 0:
                answer = min(answer, data[mid])
            else:
                answer = data[mid]
            end = mid - 1
    return answer

print(aaaa(n, k))
