import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

size = n

treesize = 1 
while treesize < size:
    treesize *= 2
treesize *= 2

segment_tree = [0] * (treesize + 1)

for i in range(n):
    segment_tree[treesize//2 + i] = int(input())

def build_tree(i):
    while i > 1:
        segment_tree[i//2] += segment_tree[i]
        i -= 1 
        
def get_sum(start, end):
    value_sum = 0
    start += treesize // 2
    end += treesize // 2
    while start <= end:
        if start % 2 == 1: # 시작이 오른쪽 자식이라면
            value_sum += segment_tree[start]
            start += 1
        if end % 2 == 0:
            value_sum += segment_tree[end]
            end -= 1
        start = start // 2
        end = end // 2
    return value_sum 
    
def change_value(index, value):
    index += treesize // 2
    diff = value - segment_tree[index]
    while index > 0:
        segment_tree[index] += diff
        index = index // 2

build_tree(treesize - 1)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1: # 값 갱신
        change_value(b - 1, c)
    if a == 2: # 값 구하기
        start = b - 1 
        end = c - 1
        print(get_sum(start, end))
