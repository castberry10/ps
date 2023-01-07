N,T,C,P =map(int, input().split())
# 7 3 2 750 -> 3000
# 여름일
# 자라는 데 걸리는 일 수 
# 칸 수
# 가격 
N -= 1

print( (N // T) * C * P )
