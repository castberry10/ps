a = input()
# c = a[0]
cnt = 0
for i in range(1, len(a)):
    if a[i-1] != a[i]:
        cnt += 1
# if cnt < 2:
#     print(cnt)
# else:
#     print(cnt-1)
if cnt < 2:
    print(cnt)
else:
    print((cnt+1)//2)
