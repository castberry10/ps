import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

size = n

treesize = 1 
while treesize < size:
    treesize *= 2
treesize *= 2

segment_tree = [0] * treesize
lazy = [0] * treesize
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
    
def update_range(start, end, value):
    pass

def apply_lazy(start, end, index):
    pass

build_tree(treesize - 1)
for i in range(m + k):
    data = input().rstrip()
    if data[0] == '1':
        pass
    if data[0] == '2':
        pass 
    # a, b, c = map(int, input().split())
    # if a == 1: # 값 갱신
    #     change_value(b - 1, c)
    # if a == 2: # 값 구하기
    #     start = b - 1 
    #     end = c - 1
    #     print(get_sum(start, end))
