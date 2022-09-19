#링크드 리스트 구현 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data): 
        point = self.head
        while point.next != None:
            point = point.next
        point.next = Node(data)

    def get_node(self, index):
        cnt = 0
        point = self.head
        while cnt < index:
            cnt += 1
            point = point.next
        return point
    
    def pop(self, index): #삭제하며 동시에 꺼내기 
        if index == 0:
            popdata = self.head.data
            self.head = self.head.next
            return popdata
        point = self.get_node(index - 1)
        popdata = point.next.data
        point.next = point.next.next
        return popdata
    
    def all_print(self):
        point = self.head
        index = 0
        print("LINKEDLIST >", point.data , '(i', index, ')/ ->',end = '')
        while point.next != None:
            point = point.next
            index += 1
            print(point.data , '(i', index, ')/  ->   ', end = '')
        print()
        
    # def nextK(self, K):
    #     pass
        
    # def delete(self, index):
    #     node
    # def pop(self, )
#7 3
#0 1 2 3 4 5 6 
#1 2 3 4 5 6 7
#3   1   2
answer = []
N, K = map(int, input().split()) # (1 ≤ K ≤ N ≤ 5,000) 
c = N
link = LinkedList(1)
for i in range(2, N + 1):
    link.append(i)
    
index = K - 1 # 처음은 K가 N보다 작거나 같다. 
# print(link.all_print())
while link.head != None:
    index %= N # N이 작아진다는 것을 계산
    answer.append(link.pop(index))
    N -= 1 
    index += K -1 

print('<', end = '')
for i in range(c - 1):
    # pass
    print(answer[i],', ', end = '', sep = '')
print(answer[c-1],'>',sep = '')

# --------------
# memo
# --------------
#
# 노드 한개 삭제 감안 