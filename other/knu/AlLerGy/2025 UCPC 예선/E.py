import sys
input = sys.stdin.readline
n = int(input())

size = n

treesize = 1 
while treesize < size:
    treesize *= 2
treesize *= 2

segment_tree = [0] * treesize
lazy = [0] * treesize
for i in range(n):
    segment_tree[treesize//2 + i] = int(input())

def build_tree():
    for i in range(treesize // 2 - 1, 0, -1):
        segment_tree[i] = segment_tree[i * 2] + segment_tree[i * 2 + 1]

def propagate(node, start,  end):
    if lazy[node]:
        segment_tree[node] += (end - start + 1) * lazy[node]
        if start != end: 
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

def get_sum(node, start, end, left, right):
    propagate(node, start, end)
    if left > end or right < start:  
        return 0
    if left <= start and end <= right: 
        return segment_tree[node]
    mid = (start + end) // 2
    left_sum = get_sum(node * 2, start, mid, left, right)
    right_sum = get_sum(node * 2 + 1, mid + 1, end, left, right)
    return left_sum + right_sum

def update_range(node, start, end, left, right, value):
    propagate(node, start, end)
    if left > end or right < start: 
        return
    if left <= start and end <= right:
        segment_tree[node] += (end - start + 1) * value
        if start != end:
            lazy[node * 2] += value
            lazy[node * 2 + 1] += value
        return
    mid = (start + end) // 2
    update_range(node * 2, start, mid, left, right, value)
    update_range(node * 2 + 1, mid + 1, end, left, right, value)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

def update_range2(node, start, end, left, right, value):
    propagate(node, start, end)
    if left > end or right < start: 
        return
    if left <= start and end <= right:
        segment_tree[node] *= 2
        if start != end:
            lazy[node * 2] *= 2
            lazy[node * 2 + 1] *= 2
        return
    mid = (start + end) // 2
    update_range(node * 2, start, mid, left, right, value)
    update_range(node * 2 + 1, mid + 1, end, left, right, value)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]
build_tree()

def minser(start, end):
    pass

q = int(input())
for i in range(q):
    data = input().rstrip()
    if data[0] == '1':
        a, b = map(int, data.split())
        
    if data[0] == '2':
        a = data[1]
        get_sum(1, 0, treesize//2 - 1, a - 1)
        # print(segment_tree[treesize//2 + i])