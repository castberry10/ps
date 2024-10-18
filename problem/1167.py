from collections import deque
import sys
input = sys.stdin.readline
v = int(input())
# tree = [[] * v+1]
tree = {}
for i in range(v):
    data = list(map(int, input().split()))
    if data[0] not in tree:
        tree[data[0]] = []
    for i in range((len(data) - 2) // 2):
        tree[data[0]].append(list((data[2 * i + 1], data[2 * i + 2])))

queue = deque()
temp = list(tree.keys())
queue.append(temp[0]) # 노드 아무거나 하나 잡기 
# visit = set()
visit_and_time = {}
# visit
distent_node = [-1, -1] # 첫번째가 노드 두번째가 거리 
visit_and_time[temp[0]] = 0

# tree = {node : [[node, time], . . . ],[[..], ..], . . .}
while queue:
    bfs_node = queue.popleft()

    for dnode_and_time in tree[bfs_node]:
        if dnode_and_time[0] not in visit_and_time: # 방문한 적이 없다면 
            visit_and_time[dnode_and_time[0]] = visit_and_time[bfs_node] + dnode_and_time[1]
            if visit_and_time[dnode_and_time[0]] > distent_node[1]:
                distent_node[1] = visit_and_time[dnode_and_time[0]]
                distent_node[0] = dnode_and_time[0]
            queue.append(dnode_and_time[0])

answer_node = [-1, -1] # 첫번째가 노드 두번째가 거리 

visit_and_time = {}
queue.append(distent_node[0])
visit_and_time[distent_node[0]] = 0

while queue:
    bfs_node = queue.popleft()
    for dnode_and_time in tree[bfs_node]:
        if dnode_and_time[0] not in visit_and_time: # 방문한 적이 없다면 
            visit_and_time[dnode_and_time[0]] = visit_and_time[bfs_node] + dnode_and_time[1]
            if visit_and_time[dnode_and_time[0]] > answer_node[1]:
                answer_node[1] = visit_and_time[dnode_and_time[0]]
                answer_node[0] = dnode_and_time[0]
            queue.append(dnode_and_time[0])

print(answer_node[1])   