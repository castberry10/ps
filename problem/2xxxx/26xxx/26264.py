n = int(input())
s = input()
point = 0
cnt = 0
scnt = 0
bcnt = 0
while True:
    if n == cnt:
        break
    if s[point] == "s":
        scnt += 1
        point += 8
        cnt += 1
    else:
        bcnt += 1
        point += 7
        cnt += 1
if scnt > bcnt:
    print("security!")
elif scnt < bcnt:
    print("bigdata?")
else:
    print("bigdata? security!")