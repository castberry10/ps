#오일러 피 함수 구현
import math
N = int(input())
answer = N

for p in range(2, int(math.sqrt(N)) + 1):
    if N % p == 0:
        answer = answer - (answer / p)
        while N % p == 0: #현재의 소인수로 계속나눠서 현재의 소인수가 없게? 하기
            N /= p

if N > 1: # N이 1보다 크면 N은 처음 데이터의 남아있는 소인수
    answer = answer - (answer / N)

print(int(answer)) # 실수를 내림해 정수로 변환