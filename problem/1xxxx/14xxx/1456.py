# 어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.
# 두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.
# 1 ≤ A ≤ B ≤ 10^14
a, b = map(int, input().split())
data = [True] * (int(b ** 0.5) + 1)
data[0], data[1] = False, False 

for i in range(2, int(b ** 0.5) + 1):
    if data[i] == False:
        continue
    else:
        for j in range(2 * i, int(b ** 0.5) + 1, i):
            data[j] = False
answer = 0
for i in range(2, int(b ** 0.5) + 1):
    if data[i] == False:
        continue
    else:
        temp = i
        temp = temp * i
        while True:
            if temp > b:
                break
            if a <= temp:
                answer += 1
            temp = temp * i
print(answer)

## 
    # if i * i > int(b ** 0.5) + 1:
    #     break
    # 가 9 ~ 10줄에 있으면 더 빠르긴하다 