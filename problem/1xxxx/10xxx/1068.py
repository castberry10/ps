from collections import deque
n = int(input())
# for i in range()
data = list(map(int, input().split()))
tree = {} # 자식을 담는 딕셔너리
root = 0
for i in range(n):
    if data[i] == -1:
        root = i
    else:
        if data[i] not in tree:
            tree[data[i]] = []
        tree[data[i]].append(i)
deleteNode = int(input())
# tree[deleteNode] = []
visit = set()
visit.add(deleteNode)
queue = deque()
if root != deleteNode:
    queue.append(root)
visit.add(root)
answer = 0
while queue:
    temp = queue.popleft()
    isleef = True
    if temp not in tree:
        answer += 1
        continue
    for i in tree[temp]:
        if i not in visit:
            isleef = False
            visit.add(i)
            queue.append(i)
    if isleef:
        answer += 1

        
        
print(answer)
