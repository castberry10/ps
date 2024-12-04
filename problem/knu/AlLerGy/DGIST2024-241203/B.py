a = int(input())
b = int(input())
c = int(input())

a = str(bin(a))[2:]
b = str(bin(b))[2:]
c = str(bin(c))[2:]

def len4444(string_n): # 반환, 인수 모두 string
    if len(string_n) < 4:
        string_n = ("0" * (4 - len(string_n))) + string_n
    return string_n
a = len4444(a)[-4:]
b = len4444(b)[-4:]
c = len4444(c)[-4:]

answer = "0b" + a + b + c
print(len4444(str(int(answer, 2))))
