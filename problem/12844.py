import sys 
input = sys.stdin.readline # 인풋
n = int(input()) # 받기

size = n # 사이즈

treesize = 1 
while treesize < size:
    treesize *= 2 # 트리 사이즈
treesize *= 2 # 트리 + 데이터 사이즈

segment_tree = [0] * treesize
lazy = [0] * treesize # 레이지 배열
data = list(map(int, input().split()))
for i in range(n):
    segment_tree[treesize//2 + i] = data[i] #값 넣기
    
m = int(input())

def build_tree():
    for i in range(treesize // 2 - 1, 0, -1):
        segment_tree[i] = segment_tree[i * 2] ^ segment_tree[i * 2 + 1] # 트리 빌드

def propagate(node, start, end): # 레이지 전파
    if lazy[node]: # 레이지 값이 있으면
        segment_tree[node] += (end - start + 1) * lazy[node] # 현재 노드에 값 더하기
        if start != end:  # 자식 노드가 있으면
            lazy[node * 2] ^= lazy[node] # 자식 노드에 레이지 값 더하기
            lazy[node * 2 + 1] ^= lazy[node] # 자식 노드에 레이지 값 더하기
        lazy[node] = 0 # 현재 노드 레이지 값 초기화

def get_xor(node, start, end, left, right): # 구간 XOR 구하기
    propagate(node, start, end)  # 레이지 전파
    if left > end or right < start:  # 구간이 겹치지 않으면
        return 0 # 0 반환
    if left <= start and end <= right: # 구간이 완전히 포함되면 
        return segment_tree[node] # 현재 노드 값 반환
    mid = (start + end) // 2 # 중간 인덱스
    left_sum = get_xor(node * 2, start, mid, left, right) # 왼쪽 자식 노드 합
    right_sum = get_xor(node * 2 + 1, mid + 1, end, left, right) # 오른쪽 자식 노드 합
    return left_sum ^ right_sum # 합 반환

def update_range(node, start, end, left, right, value): # 구간 업데이트
    propagate(node, start, end) # 레이지 전파
    if left > end or right < start: # 구간이 겹치지 않으면
        return # 종료
    if left <= start and end <= right: # 구간이 완전히 포함되면
        segment_tree[node] += (end - start + 1) * value # 현재 노드 값 업데이트
        if start != end: # 자식 노드가 있으면
            lazy[node * 2] += value # 자식 노드에 레이지 값 더하기
            lazy[node * 2 + 1] += value     # 자식 노드에 레이지 값 더하기
        return # 종료
    mid = (start + end) // 2 # 중간 인덱스
    update_range(node * 2, start, mid, left, right, value) # 왼쪽 자식 노드 업데이트
    update_range(node * 2 + 1, mid + 1, end, left, right, value) # 오른쪽 자식 노드 업데이트
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1] # 현재 노드 값 업데이트

build_tree() # 트리 빌드
for i in range(m): 
    data = input().rstrip() #
    if data[0] == '1':
        a, b, c, d = map(int, data.split())
        update_range(1, 0, treesize//2 - 1, b - 1, c - 1, d)
    if data[0] == '2':
        a, b, c = map(int, data.split())
        print(get_xor(1, 0, treesize//2 - 1, b - 1, c - 1))
