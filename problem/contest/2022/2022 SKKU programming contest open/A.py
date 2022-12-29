# X - 처음으로 내는 목소리 크기
# N 사람 수 
#T[i] - i번째 사람이 낼 수 있는 목소리 한계치 

# 대충 n 번째에 X * n - 1 의 형태를 가짐 

# 3 
# 0 1 2 3 4 5 6 7 8 9  - n
# 0 1 2 0 1 2 0 1 2 0  - n % N 

N, X = map(int, input().split())
T = list(map(int, input().split()))
n = 0

while True:
    # print("n - ",n,"/ n + X - 1", n + X - 1, end = '///')
    # print("T[n % N]", T[n % N])
    if n + X > T[n % N]: # 상한선이라면 
        print(n % N + 1)
        break 
    n += 1
    
