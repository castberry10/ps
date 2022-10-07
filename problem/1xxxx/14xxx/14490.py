a1 , a2 = map(int, input().split(":"))

def gcd(a1, a2):#이름이 이게 맞나?
    #a1은 a2보다 크다 <라는 가정
    if a1 % a2 == 0:
        return a2
    
    return gcd(a2, a1 % a2)

if a1 >= a2:
    a = gcd(a1, a2)
else:
    a = gcd(a2, a1)
print(a1 // a,":", a2 // a, sep = "")
    