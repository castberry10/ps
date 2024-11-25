import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

size = n
mod_value = 1000000007
treesize = 1 
while treesize < size:
    treesize *= 2
treesize *= 2

segment_tree = [1] * (treesize + 1)

for i in range(n):
    segment_tree[treesize//2 + i] = int(input())

def build_tree(i):
    while i > 1: 
        segment_tree[i//2] = segment_tree[i//2] * segment_tree[i] % mod_value
        i -= 1 
        
def get_product(start, end):
    value_product = 1
    start += treesize // 2
    end += treesize // 2
    while start <= end:
        if start % 2 == 1: # 시작이 오른쪽 자식이라면
            value_product = (segment_tree[start] * value_product) % mod_value
            start += 1
        if end % 2 == 0:
            value_product = (segment_tree[end] * value_product) % mod_value
            end -= 1
        start = start // 2
        end = end // 2
    return value_product
    
def change_value(index, value):
    index += treesize // 2
    segment_tree[index] = value
    while index > 1:
        index //= 2
        segment_tree[index] = (segment_tree[index * 2] * segment_tree[index * 2 + 1]) % mod_value 

build_tree(treesize - 1)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1: # 값 갱신
        change_value(b - 1, c)
    if a == 2: # 값 구하기
        start = b - 1 
        end = c - 1
        print(get_product(start, end))
