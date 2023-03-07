n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

dic = {}
answer = ""
for i in nlist:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

for i in mlist:
    if i in dic:
        answer += str(dic[i]) + " "
        
    else:
        answer += "0 "

print(answer)