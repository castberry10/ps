global answer

answer = 0
n = int(input())

def play(a):
    global answer
    if a == 1:
        return
    a2 = a // 2
    if a % 2 == 1:
        answer += a2 * (a2 + 1)
        play(a2)
        play(a2 + 1)
    else:
        answer += a2 * a2
        play(a2)
        play(a2)
    return

play(n)
print(answer)