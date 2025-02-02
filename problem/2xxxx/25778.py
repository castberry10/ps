import sys
input = sys.stdin.readline
n = int(input())
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
    start += treesize // 2 - 1
    end += treesize // 2 - 1
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
    
def add_value(index, value):
    index += treesize // 2 -1 
    while index > 0:
        segment_tree[index] += value
        index = index // 2

build_tree(treesize - 1)
m = int(input())
for i in range(m):
    a, b, c = input().split()
    b, c = int(b), int(c)
    if a == 'R':
        print(get_sum(b, c))
    if a == 'U':
        add_value(b, c)