n = int(input())
a = input()
ac = 0
nc = 0
answer = 0
for c in a:
    if c == "A":
        if ac == 0:
            ac = 1
        else:
            if nc == 1:
                answer += 1
                nc = 0
            else:
                nc = 0
    if c == "N":
        nc+= 1
print(answer)