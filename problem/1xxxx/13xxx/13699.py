n = int(input())

# t(0)=1
# t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)
# 이 정의에 따르면,

# t(1)=t(0)*t(0)=1
# t(2)=t(0)*t(1)+t(1)*t(0)=2
# t(3)=t(0)*t(2)+t(1)*t(1)+t(2)*t(0)=5

data = [0] * (n + 3)
data[1] = data[0] = 1
data[2] = 2
data[3] = 5

for i in range(4, n+1):#       j 0   i4 j0 -1 
    for j in range(i): # 4 -> t(0) * t(3) + t(1) * t(2)
        data[i] += data[j] * data[i - j -1]
print(data[n])
    