#Frame–Stewart
import sys
sys.setrecursionlimit(10**6)

n = int(input())

def hanoi(a):
    if a == 1:
        return 1
    k = a + 1 - round((2 * a + 1) ** 0.5)
    return (2 * hanoi(k) + 2 ** (a - k) - 1) % 9901
# 상위 k개의 디스크를 보조 기둥으로 옮기는 데 걸리는 이동 횟수. - 2 * hanoi(k)
# 남아 있는 a - k개의 디스크를 3개의 기둥만 사용하여 이동하는 경우의 최소 이동 횟수. -  2 ** (a - k) - 1
print(hanoi(n))