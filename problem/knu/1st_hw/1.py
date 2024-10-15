n = int(input())
ls = [0]
ls += list(map(int, input().split()))
s = int(input())
sumls = [0] * (n + 1)

answer = []

for i in range(n):
    sumls[i + 1] = sumls[i] + ls[i + 1]
# 누적합 배열 생성 O(n) 이후 접근은 O(1)

# 슬라이드 인덱스 n - s + 1회만큼 반복 
for i in range(n - s + 1):  
    temp = sumls[i + s] - sumls[i] # 누적합 연산으로 O(1)
    if temp / s == temp // s: # 평균이 정수면 정답 배열에 저장 
        answer.append(temp // s)
    else:
        pass

if len(answer) == 0: # 만약 answer 배열이 비어있다면 
    print(-1)
else:
    for i in answer:
        print(i)