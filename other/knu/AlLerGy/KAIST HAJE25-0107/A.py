n, d, p = map(int, input().split())
a = list(map(int, input().split()))
answer = 0
index = 0

while index < n:  
    while index < n and a[index] <= 0:
        index += 1
    if index >= n:
        break

    answer += 1  
    a[index] -= d
    
    if a[index] < 0:
        overdmg = -a[index]
        index += 1  
        if index < n:
            dmg = int(overdmg * p / 100)
            a[index] -= dmg
    elif a[index] == 0:
        index += 1
    else:
        pass

print(answer)
