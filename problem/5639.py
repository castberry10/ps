# 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
# 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.
# 전위 순위를 받아서 후위순위로 반환해야함 
# ----------------------------------------------
#전위 순회 preorder traversal 노드 -> 왼 -> 오
#중위 순회 inorder traversal 왼 -> 노드 -> 오
#후위 순회 postorder traversal 왼 -> 오 -> 노드 
answer = []
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
        
    def add(self, data):
        if self.root == None:
            self.root = Node(data) 
            return
        
        cur = self.root 
        while True:
            if cur.data < data:# 
                if cur.right.data == None:
                    cur.right.data = Node(data)
                    return
                else: #비어있지않다면 
                    cur = cur.right
            else:#작다면[ cur.data > data ]
                if cur.left.data == None:
                    cur.left.data = Node(data)
                    return
                else:
                    cur = cur.left
    
    def postorder(self, node = None):
        if node == None:
            node = self.root
        if node.left != None:
            self.postorder(node.left)
        if node.right != None:
            self.postorder(node.right)
        # print(node.data)
        answer.append(node.data)
        
        
tree = Tree()

while True:
    try:
        a = int(input())
        tree.add(a)
    except:
        break

tree.postorder()
for i in answer:
    print(i)