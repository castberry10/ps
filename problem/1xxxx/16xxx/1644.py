def primef():
    limit = 4000000  
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(limit + 1) if is_prime[i]]

n = int(input())

primelist = primef()
answer = 0
start, end, data = 0, 0, 0  

while start < len(primelist):  
    if data == n:
        answer += 1
        data -= primelist[start] 
        start += 1
    elif data < n:
        if end < len(primelist):  
            data += primelist[end]
            end += 1
        else:
            break  
    else:
        data -= primelist[start]
        start += 1

print(answer)
